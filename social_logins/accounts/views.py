import requests

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from accounts.serializers import GoogleRequestSerializer
from accounts.models import User
from accounts.functions import Google

class GoogleLogin(APIView):
    """
    API used to login/create user account using Google.
    """
    def post(self, request):
        serializer = GoogleRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        google_obj = Google()
        try:
            access_token = google_obj.get_access_token(serializer.validated_data['code'])
            user_data = google_obj.get_user_data(access_token)

        except requests.HTTPError:
            return Response({
                "message": "Failed to get details from Google."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user_obj = User.objects.filter(
            Q(email__iexact=user_data['email']) |
            Q(social_id=user_data['sub'])
        ).first()
        if not user_obj:
            user_obj = User.objects.create(
                first_name=user_data['given_name'],
                last_name=user_data['family_name'],
                email=user_data['email'],
                social_id=user_data['sub']
            )
            response_messages = "Account created successfully."

        else:
            response_messages = "Login successful."

        return Response({
            'message': response_messages
        }, status=status.HTTP_200_OK)
