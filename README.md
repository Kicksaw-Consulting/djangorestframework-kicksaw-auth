# Installation

```
pip install djangorestframework-kicksaw-auth
```

Or with poetry

```
poetry add djangorestframework-kicksaw-auth
```

# Usage

## BasicApiGatewayApiKeyAuth

```python
from djangorestframework_kicksaw_auth import BasicApiGatewayApiKeyAuth

@authentication_classes([BasicApiGatewayApiKeyAuth])
def endpoint(request: HttpRequest):
    # ...
```

This authenticator reads basic auth and ensures the username and password
match an API Gateway key

```
curl -u username:password -v localhost:8000/api/your/endpoint
```

Where `username` is the name of your API key and `password` is the API key
