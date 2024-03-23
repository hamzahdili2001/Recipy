from datetime import datetime
from accounts.permissions import IsValidJWTAccessToken
from django.http import Http404
from rest_framework import status as st
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.request import Request
from accounts.models import User, UserProfile
from accounts.serializers import (
    UserSerializer,
    UserProfileSerializer,
    LoginSerializer,
    RefreshTokenSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


def get_user_id_from_access_token(request: Request) -> (str | None):
    auth_header = request.headers.get("Authorization")
    token = auth_header.split()[1]
    access_token = AccessToken(token)
    id = access_token.payload.get("user_id")
    if not id:
        return None
    return id


@api_view(["GET"])
def status(request: Request):
    return Response(data={"status": "Working"})


@api_view()
@permission_classes([IsValidJWTAccessToken])
def user_info(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
        "last_login": str(user.last_login)
    }

    return Response(data=data)


@api_view(["POST"])
def signup(request: Request):
    user_serializer = UserSerializer(data=request.data)
    profile_serializer = UserProfileSerializer(data=request.data)

    valid_user_data = user_serializer.is_valid()
    valid_profile_data = profile_serializer.is_valid()

    if valid_user_data and valid_profile_data:
        user_instance = user_serializer.save()
        profile_serializer.save(user=user_instance)
        response_data = {
            "id": user_instance.id,
            "username": user_instance.username,
            "email": user_instance.email,
            "profile": profile_serializer.data
        }
        return Response(response_data, status=st.HTTP_201_CREATED)
    else:
        errors = {}
        if user_serializer.errors:
            errors.update(user_serializer.errors)
        if profile_serializer.errors:
            errors.update(profile_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@parser_classes([JSONParser])
@permission_classes([IsValidJWTAccessToken])
def update_data(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    data = {
        "first_name": request.data.get("first_name"),
        "last_name": request.data.get("last_name"),
        "username": request.data.get("username")
    }

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    user.save()
    return Response({"message": "ok"})


@api_view(["PUT"])
@parser_classes([JSONParser])
@permission_classes([IsValidJWTAccessToken])
def update_email(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    data = {
        "email": request.data.get("email")
    }

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    user.save()
    return Response({"message": "ok"})


@api_view(["PUT"])
@parser_classes([JSONParser])
@permission_classes([IsValidJWTAccessToken])
def update_password(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    data = {
        "password0": request.data.get("password0"),
        "password1": request.data.get("password1")
    }

    if not user.check_password(data.get("password0")):
        return Response({"error": "Old password is invalid"}, status=st.HTTP_400_BAD_REQUEST)
    elif not data.get("password1"):
        return Response({"error": "New password cannot be empty"}, status=st.HTTP_400_BAD_REQUEST)
    elif data.get("password0") == data.get("password1"):
        return Response({"error": "Password are the same"}, status=st.HTTP_400_BAD_REQUEST)
    else:
        setattr(user, "password", data.get("password1"))
    User.set_password(user, user.password)
    user.save()
    return Response({"message": "ok"})


@api_view(["PUT"])
@parser_classes([MultiPartParser])
@permission_classes([IsValidJWTAccessToken])
def update_picture(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    profile_serializer = UserProfileSerializer(data=request.data)
    valid_profile_data = profile_serializer.is_valid()
    if valid_profile_data:
        user_profile = UserProfile.objects.filter(user=user).get()
        if user_profile.picture:
            user_profile.picture.delete()
        user_profile.picture = request.data.get("picture")
        user_profile.save()
        return Response({"message": "ok"})
    else:
        errors = {}
        if profile_serializer.errors:
            errors.update(profile_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsValidJWTAccessToken])
def delete_user(request: Request):
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")
    user.delete()
    return Response({"message": "ok"})


@api_view(["POST"])
@parser_classes([JSONParser])
def login(request: Request):
    """
    Login a user through email/username and password
    Read more about jwt tokens here:
    https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
    """
    login_serializer = LoginSerializer(data=request.data)
    valid = login_serializer.is_valid()
    user = None
    if valid:
        user = User.objects.filter(
            email=login_serializer.data.get("username")).first()
        if not user:
            user = User.objects.filter(
                username=login_serializer.data.get("username")).first()
        if user is not None and user.check_password(login_serializer.data.get("password")):
            user.last_login = login_serializer.data.get("last_login")
            user.save()
            refresh: RefreshToken = RefreshToken.for_user(user)
            access_token: AccessToken = refresh.access_token
            return Response(
                {
                    "message": "ok",
                    "access": {
                        "token": str(access_token),
                        "exp": access_token.payload.get("exp")
                    },
                    "refresh": {
                        "token": str(refresh),
                        "exp": refresh.payload.get("exp")
                    },
                }
            )
        else:
            errors = {"error": "Invalid credentials"}
            return Response(errors, status=st.HTTP_401_UNAUTHORIZED)
    else:
        errors = {}
        if login_serializer.errors:
            errors.update(login_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([])
def refresh_token(request: Request):
    refresh_token_serializer = RefreshTokenSerializer(data=request.data)
    valid = refresh_token_serializer.is_valid()
    if valid:
        try:
            refresh = refresh_token_serializer.validated_data.get("refresh")
            refresh_token = RefreshToken(refresh)
            RefreshToken.verify(refresh_token)
        except Exception as e:
            return Response({"error": str(e)}, status=st.HTTP_403_FORBIDDEN)
        return Response({"access_token": str(refresh_token.access_token)})
    else:
        errors = {}
        if refresh_token_serializer.errors:
            errors.update(refresh_token_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)
