import requests

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import LoginSerializer
from accounts.models import User
from accounts.functions import Google, Meta

class Login(APIView):
    """
    API used to login/create user account using Google/Facebook.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        providers = {
            LoginSerializer.PROVIDER_GOOGLE: Google,
            LoginSerializer.PROVIDER_META: Meta
        }
        provider_obj = providers[serializer.validated_data['provider']]()
        try:
            access_token = provider_obj.get_access_token(serializer.validated_data['code'])
            user_data = provider_obj.get_user_data(access_token)

        except requests.HTTPError:
            return Response({
                "message": "Failed to get details from Google."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user_obj = User.objects.filter(
            Q(email__iexact=user_data['email']) |
            Q(social_id=user_data.get('sub') or user_data.get('id'))
        ).first()
        if not user_obj:
            user_obj = User.objects.create(
                first_name=user_data.get('given_name') or user_data.get('name').split()[0],
                last_name=user_data.get('family_name') or user_data.get('name').split()[1],
                email=user_data['email'],
                social_id=user_data.get('sub') or user_data.get('id')
            )
            response_messages = "Account created successfully."

        else:
            response_messages = "Login successful."

        return Response({
            'message': response_messages
        }, status=status.HTTP_200_OK)
