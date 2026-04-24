from xmlrpc.client import ResponseError
import requests

from django.conf import settings

class Google:
    def get_access_token(self, code):
        data = {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "code": code,
            "grant_type": "authorization_code"
        }
        response = requests.post(
            settings.GOOGLE_AUTH_TOKEN_URL,
            data=data
        )
        response.raise_for_status()
        return response.json()['access_token']

    def get_user_data(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(
            settings.GOOGLE_USER_INFO_URL,
            headers=headers
        )
        response.raise_for_status()
        return response.json()


class Meta:
    def get_access_token(self, code):
        paraterms = {
            "client_id": settings.META_APP_ID,
            "client_secret": settings.META_APP_SECRET,
            "redirect_uri": settings.META_REDIRECT_URI,
            "code": code
        }
        response = requests.post(
            settings.META_AUTH_TOKEN_URL,
            params=paraterms
        )
        response.raise_for_status()
        return response.json()['access_token']

    def get_user_data(self, access_token):
        parameters = {
            "fields": "id,name,email",
            "access_token": access_token
        }
        response = requests.get(
            settings.META_USER_INFO_URL,
            params=parameters
        )
        response.raise_for_status()
        return response.json()
