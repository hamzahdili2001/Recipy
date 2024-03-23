"""
This module is about the permissions of the users
"""
from accounts.models import User
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import AccessToken


class IsValidJWTAccessToken(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return False

        try:
            token_type, token = auth_header.split()
        except ValueError:
            return False

        if token_type.lower() != 'bearer':
            return False

        access_token = AccessToken(token)
        user_id = access_token.payload.get("user_id")
        if not user_id:
            return False
        elif not User.objects.filter(id=user_id).first():
            return False
        else:
            try:
                access_token.verify()
            except AccessToken.ExpiredToken:
                return False

        return True
