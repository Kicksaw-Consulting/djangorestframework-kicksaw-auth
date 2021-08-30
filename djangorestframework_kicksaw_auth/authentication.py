import boto3

from django.conf import settings
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
            response["items"][0]["name"] == userid
            and response["items"][0]["value"] == password
        ):
            return FakeUser(), None

        raise exceptions.AuthenticationFailed("Invalid login attempt")


class BasicSettingsAuth(BasicAuthentication):
    """
    Pull username and password from plain ol' django settings
    """

    def authenticate_credentials(
        self, username: str, password: str, request: HttpRequest
    ):
        # if the key value does not match, deny access
        if (
            username == settings.DRF_KICKSAW_AUTH_USERNAME
            and password == settings.DRF_KICKSAW_AUTH_PASSWORD
        ):
            return FakeUser(), None

        raise exceptions.AuthenticationFailed("Invalid login attempt")
