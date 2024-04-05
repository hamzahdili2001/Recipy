"""
This module is about the models of the app accounts
"""
import uuid
# from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


def upload_to(instance, filename):
    return '/'.join(['images', str(instance.user.username), filename])

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Recipe(TimeStampMixin, models.Model):
    """Recipe model definition"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "recipies"
        ordering = ["created_at"]


class TheUserManager(UserManager):
    def _create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        username=None,
        first_name=None,
        last_name=None,
        email=None,
        password=None,
        **extra_fields
    ):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            username, first_name, last_name, email, password, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    """User model definition"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    objects = TheUserManager()
    # relationships
    recipes = models.ManyToManyField(Recipe, blank=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]


class UserProfile(models.Model):
    """User Profile"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
