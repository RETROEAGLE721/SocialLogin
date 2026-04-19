from rest_framework import serializers


class GoogleRequestSerializer(serializers.Serializer):
    """
    Serializer used to validate input data for GoogleLogin API.
    """
    code = serializers.CharField(
        error_messages={
            'required': 'The `code` field is required.',
            'blank': 'The `code` field cannot be blank.',
            'null': 'The `code` field cannot be null.'
        }
    )
