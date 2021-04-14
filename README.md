# Installation

```
pip install djangorestframework-api-gateway-auth
```

Or with poetry

```
poetry add djangorestframework-api-gateway-auth
```

# Usage

## BasicApiGatewayApiKeyAuth

This authenticator reads basic auth and ensures the username and password
match an API Gateway key

```
curl -u username:password -v localhost:8000/api/your/endpoint
```

Where `username` is the name of your API key and `password` is the API key
