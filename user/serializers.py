from rest_framework import serializers

from user.models import User
# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'role', 'first_name', 'last_name', 'password', 'email')
