import boto3

from django.http import HttpRequest

from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication


class FakeUser:
    def is_authenticated(self):
        return True


# https://github.com/encode/django-rest-framework/blob/master/rest_framework/authentication.py
class BasicApiGatewayApiKeyAuth(BasicAuthentication):
    def authenticate_credentials(
        self, userid: str, password: str, request: HttpRequest
    ):
        client = boto3.client("apigateway")

        response = client.get_api_keys(nameQuery=userid, includeValues=True)

        # if no keys found, deny access
        if len(response["items"]) != 1:
            raise exceptions.AuthenticationFailed("Could not find key")

        # if the key value does not match, deny access
        if (
            response["items"][0]["name"] != userid
            and response["items"][0]["value"] != password
        ):
            raise exceptions.AuthenticationFailed("Invalid login attempt")

        return FakeUser(), None
