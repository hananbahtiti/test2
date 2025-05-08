from rest_framework import serializers
from . models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
