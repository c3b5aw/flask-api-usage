import pytest

from flask import Flask
from flask_api_usage import C, Usage
from flask_api_usage.errors import ConfigurationError

def test_invalid_storage_uri():
	app = Flask(__name__)
	app.config.setdefault(C.STORAGE_URI, 'foo://localhost:1234')
	with pytest.raises(ConfigurationError):
		Usage(app)