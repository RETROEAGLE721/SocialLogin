from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    Serializer used to validate input data for GoogleLogin API.
    """
    PROVIDER_GOOGLE = 'google'
    PROVIDER_META = 'meta'
    code = serializers.CharField(
        error_messages={
            'required': 'The `code` field is required.',
            'blank': 'The `code` field cannot be blank.',
            'null': 'The `code` field cannot be null.'
        }
    )
    provider = serializers.ChoiceField(
        choices=[
            PROVIDER_GOOGLE,
            PROVIDER_META
        ],
        error_messages={
            'required': 'The `provider` field is required.',
            'blank': 'The `provider` field cannot be blank.',
            'null': 'The `provider` field cannot be null.',
            'invalid_choice': 'The `provider` field is invalid.'
        }
    )
