"""
This module is about the serializers of the models
https://www.django-rest-framework.org/tutorial/1-serialization/
"""
from accounts.models import User, Recipe
from typing import Dict
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    fullname = serializers.CharField(required=True, max_length=100)
    username = serializers.CharField(required=True, max_length=50)
    mail = serializers.EmailField(required=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data: Dict[str, str]):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance: User, validated_data: Dict[str, str]):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.fullname = validated_data.get("fullname", instance.fullname)
        instance.username = validated_data.get("username", instance.username)
        instance.mail = validated_data.get("mail", instance.mail)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance


class RecipeSerializer(serializers.Serializer):
    def create(self, validated_data: Dict[str, str]):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)
