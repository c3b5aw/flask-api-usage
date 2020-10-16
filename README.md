# flask-api-usage

```python
from flask import Flask
from flask_api_usage import Usage
flask_app = Flask(__name__)

db = 'mongoDB_db_name'
mongoURI = 'mongodb://localhost:1234/'

flask_app.config['USAGE_MONGODB_SETTINGS'] = {
    'db': db,
    'host': mongoURI,
    'alias': 'flask-usage'
}

# === Way 1 ===

usage = Usage()
Usage.init_app(flask_app)

# === Way 2 ===

Usage(flask_app)
```

## Addon available document
```
{
    "_id" : ObjectId,
    "date" : ISODate,
    "exception" : str,
    "method" : str,
    "path" : str,
    "url" : str,
    "status_code" : int,
    "response" : {
        "content_length" : int,
        "mimetype" : str,
        "headers" : dict,
        "body" : dict
    },
    "client" : {
        "referer" : str,
        "authorization" : str,
        "origin" : str,
        "remote_address" : str
        "user_agent" : str,
        "platform" : str,
        "browser" : str
    },
    "request" : {
        "elapsed_time" : float,
        "content_length" : int,
        "mimetype" : str,
        "body" : dict,
        "headers" : dict,
        "args" : dict
    }
}
```

## Exemple document created while fetching configuration before stripe request.

```
{
    "_id" : ObjectId("private"),
    "date" : ISODate("2020-10-10T22:45:35.944Z"),
    "exception" : "None",
    "method" : "GET",
    "path" : "/api/v0/pay/setup",
    "url" : "http://localhost:22222/api/v0/pay/setup",
    "status_code" : 200,
    "response" : {
        "content_length" : 638,
        "mimetype" : "application/json",
        "headers" : {
            "Content-Type" : "application/json",
            "Content-Length" : "638",
            "Access-Control-Allow-Origin" : "http://localhost:5000",
            "Vary" : "Origin"
        },
        "body" : {
            "publicKey" : "private",
            "products" : [ 
                {
                    "name" : "private",
                    "id" : "private",
                    "image" : "private",
                    "metadata" : {
                        "private" : "True"
                    },
                    "description" : "private",
                    "price" : {
                        "id" : "private",
                        "amount" : "private",
                        "currency" : "eur"
                    },
                    "unit" : "key"
                }
            ]
        }
    },
    "client" : {
        "referer" : "http://localhost:5000/",
        "authorization" : null,
        "origin" : "http://localhost:5000",
        "remote_address" : "127.0.0.1",
        "user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "platform" : "windows",
        "browser" : "chrome 85.0.4183.121"
    },
    "request" : {
        "elapsed_time" : 0.593111753463745,
        "content_length" : null,
        "mimetype" : "",
        "body" : null,
        "headers" : {
            "Host" : "localhost:22222",
            "Connection" : "keep-alive",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0 Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Accept" : "*/*",
            "Origin" : "http://localhost:5000",
            "Sec-Fetch-Site" : "same-site",
            "Sec-Fetch-Mode" : "cors",
            "Sec-Fetch-Dest" : "empty",
            "Referer" : "http://localhost:5000/",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
        },
        "args" : {}
    }
}
```
