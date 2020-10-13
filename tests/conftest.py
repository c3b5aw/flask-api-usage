import pytest

from flask import Flask
from flask_api_usage import Usage

@pytest.fixture
def extension_factory():
	def _build_app_and_extensions(config=None, **usage_args):
		if config is None:
			config = {}
		app = Flask(__name__)
		for k, v in config.items():
			app.config.setdefault(k, v)
		usage = Usage(app, **usage_args)
		return app, usage
	return _build_app_and_extensions()
