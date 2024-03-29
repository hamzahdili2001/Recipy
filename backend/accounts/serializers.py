"""
This module is about the serializers of the models
https://www.django-rest-framework.org/tutorial/1-serialization/
"""
from accounts.models import User, Recipe, UserProfile
from datetime import datetime
from typing import Dict
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "username", "email", "password"]

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["picture"]
        
class RecipeBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["title", "recipe_id"]


class RecipeSerializer(serializers.Serializer):
    def create(self, validated_data: Dict[str, str]):
        """
        Create and return a new `Recipe` instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)
    
class UserMailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class UserPasswordSerializer(serializers.Serializer):
    password0 = serializers.CharField()
    password1 = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    last_login = serializers.DateTimeField(read_only=False, default=datetime.now())


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class RemoveRecipeBookmarkSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()