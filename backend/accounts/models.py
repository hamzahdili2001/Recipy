"""
This module is about the models of the app accounts
"""
import uuid
from django.db import models


class Recipe(models.Model):
    """Recipe model definition"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "recipies"


class User(models.Model):
    """User model definition"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    mail = models.EmailField()
    password = models.TextField()
    # relationships
    recipes = models.ManyToManyField(Recipe)
