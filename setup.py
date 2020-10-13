"""

setup.py for Flask-Api-Usage

"""

__author__ = '@c3b5aw'
__email__ = 'hello@c3b5aw.dev'
__copyright__ = 'Copyright do whatever you want it is open sourced.'
__version__ = '0.0.1'

import os

from setuptools import setup, find_packages

requirements = filter(None, open(
	os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')
).read().splitlines())

setup(
	name='flask-api-usage',
	author=__author__,
	author_email=__email__,
	license=None,
	url='https://github.com/c3b5aw/flask-api-usage',
	zip_safe=False,
	version=__version__,
	description='Gather statistics on your app usage.',
	packages=find_packages(),
	python_requires='>=3.6',
	install_requires=list(requirements)
)