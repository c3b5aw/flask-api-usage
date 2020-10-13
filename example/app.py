from flask import Flask
from extensions import usage, cache

def create_app():
	app = Flask(__name__)
	app.config['DEBUG'] = True

	app.config['USAGE_MONGODB_SETTINGS'] = {
		'db': 'flask',
		'host': 'mongodb://localhost:27017/'
	}

	usage.init_app(app)
	cache.init_app(app, config={
		'DEBUG': True,
		'CACHE_TYPE': 'redis',
		'CACHE_REDIS_URL': 'redis://192.168.1.16:6379',
		"CACHE_DEFAULT_TIMEOUT": 300
	})

	@app.route('/cached')
	@cache.cached()
	def home_page():
		return {'msg': '/cached'}

	@app.route('/')
	def cache_page():
		return {'msg': '/'}

	return app