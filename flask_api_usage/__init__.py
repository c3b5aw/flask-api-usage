import time
import datetime
import logging

from flask import Flask, g, Response, request
from mongoengine import connect, Document, DictField, DateTimeField, StringField, IntField


class C:
	ENABLED = 'USAGE_ENABLED'
	STORAGE_URI = 'USAGE_STORAGE_URI'
	METHODS = ('GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH')


class APIUse(Document):
	meta = {'collection': 'api-usage'}

	date = DateTimeField()
	exception = StringField()
	method = StringField(max_length=7, choices=C.METHODS)
	path = StringField()
	url = StringField()
	status_code = IntField(default=500, max_length=3)

	response = DictField()
	client = DictField()
	request = DictField()


class Usage:
	def __init__(self, app: Flask = None, enabled=True):

		self.app = app
		self.logger = logging.getLogger('flask-api-usage')

		self.enabled = enabled
		self.initialized = False
		self.db = None

		if app:
			self.init_app(app)

	def init_app(self, app: Flask = None) -> None:
		config = app.config

		self.enabled = config.setdefault(C.ENABLED, self.enabled)
		if not self.enabled:
			return

		self.db = connect('usage', **config.get('USAGE_MONGODB_SETTINGS'))

		self.app = app
		self.app.before_request(self.before_request)
		self.app.after_request(self.after_request)
		self.app.teardown_request(self.teardown_request)

	def before_request(self) -> None:
		g.use = APIUse()

		g.start_time = time.time()
		g.use.date = datetime.datetime.utcnow()

	def after_request(self, response: Response) -> Response:
		g.use.status_code = response.status_code

		g.use.response['content_length'] = response.content_length
		g.use.response['mimetype'] = response.mimetype
		g.use.response['headers'] = response.headers
		g.use.response['body'] = response.get_json()

		return response

	def teardown_request(self, exception: Exception = None) -> None:
		try:
			g.use.exception = repr(exception) if Exception is not None else None
			g.use.path = request.path
			g.use.url = request.url
			g.use.method = request.method

			g.use.request['elapsed_time'] = time.time() - g.start_time
			g.use.request['content_length'] = request.content_length
			g.use.request['mimetype'] = request.mimetype
			g.use.request['body'] = request.get_json()
			g.use.request['headers'] = request.headers
			g.use.request['args'] = request.args


			g.use.client['referer'] = request.referrer
			g.use.client['authorization'] = request.authorization
			g.use.client['origin'] = request.origin
			g.use.client['remote_address'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
			g.use.client['user_agent'] = request.user_agent.string
			g.use.client['platform'] = request.user_agent.platform
			g.use.client['browser'] = f'{request.user_agent.browser} {request.user_agent.version}'

			g.use.save()

		except Exception as e:
			self.logger.warning('Error in flask-api-usage teardown: ' + str(e))