#flask-api-usage

```python
from flask import Flask
from flask_api_usage import Usage
flask_app = Flask(__name__)

db = 'mongoDB_db_name'
mongoURI = 'mongodb://localhost:1234/'

flask_app.config['USAGE_MONGODB_SETTINGS'] = {
    'db': db,
    'host': mongoURI
}

# === Way 1 ===

usage = Usage()
Usage.init_app(flask_app)

# === Way 2 ===

Usage(flask_app)
```
