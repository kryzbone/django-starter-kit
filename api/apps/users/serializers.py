from django.contrib.auth import get_user_model
from djoser.serializers import UserCreatePasswordRetypeSerializer
from rest_framework import serializers

User = get_user_model()


class UserCreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = UserCreatePasswordRetypeSerializer.Meta.fields + ("uuid",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uuid", "username", "email", "created_at")
        ref_name = "custom_user"
