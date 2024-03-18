"""
This module is about the serializers of the models
https://www.django-rest-framework.org/tutorial/1-serialization/
"""

from accounts.models import User, Recipe, UserProfile
from typing import Dict
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "username", "email", "password"]
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["picture"]


class RecipeSerializer(serializers.Serializer):
    def create(self, validated_data: Dict[str, str]):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)
