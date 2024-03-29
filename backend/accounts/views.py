from accounts.permissions import IsValidJWTAccessToken
from django.http import Http404, HttpResponse
import mimetypes
from rest_framework import status as st
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.request import Request
from accounts.models import User, UserProfile, Recipe
from accounts.serializers import (
    UserSerializer,
    UserProfileSerializer,
    LoginSerializer,
    RefreshTokenSerializer,
    RecipeBookmarkSerializer,
    RemoveRecipeBookmarkSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
import os


def get_user_id_from_access_token(request: Request):
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
    """Get user info handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")
    
    user_picture = None
    try:
        user_picture = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        pass

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
        "profil": ("api/user/profil" if user_picture else None),
        "last_login": str(user.last_login)
    }

    return Response(data=data)

@api_view()
@permission_classes([IsValidJWTAccessToken])
def user_recipe_bookmark(request: Request):
    """Get user bookmarked recipes handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")
    res = []
    
    data = {}
    for recipe in user.recipes.values():
        for k, v in recipe.items():
            data[k] = v
        res.append(data)
        data = {}
            
    return Response({"data": res})


@api_view(["POST"])
@parser_classes([JSONParser])
def signup(request: Request):
    """Create a new user handler"""
    user_serializer = UserSerializer(data=request.data)
    # profile_serializer = UserProfileSerializer(data=request.data)

    valid_user_data = user_serializer.is_valid()
    # valid_profile_data = profile_serializer.is_valid()

    if valid_user_data:
        user_instance: User = user_serializer.save()
        # profile_serializer.save(user=user_instance)
        response_data = {
            "id": user_instance.id,
            "username": user_instance.username,
            "email": user_instance.email,
            # "profile": profile_serializer.data
        }
        return Response(response_data, status=st.HTTP_201_CREATED)
    else:
        errors = {}
        if user_serializer.errors:
            errors.update(user_serializer.errors)
        # if profile_serializer.errors:
        #     errors.update(profile_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@parser_classes([JSONParser])
@permission_classes([IsValidJWTAccessToken])
def update_data(request: Request):
    """
    Update user data (first_name, last_name, username) handler
    """
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
    """Update user email handler"""
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
    """Update user password handler"""
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


@api_view(["GET"])
@permission_classes([IsValidJWTAccessToken])
def user_profile(request: Request):
    """Get user picture handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
        user_profile = UserProfile.objects.get(user=user)
        picture_path = user_profile.picture.path
    except (User.DoesNotExist, UserProfile.DoesNotExist):
        return Response({"error": "User profile picture not found"}, status=st.HTTP_404_NOT_FOUND)
    
    if not os.path.exists(picture_path):
        return Response({"message": None})

    mime_type, _ = mimetypes.guess_type(picture_path)
    if not mime_type or not mime_type.startswith('image'):
        return Response({"error": "Unsupported file type"}, status=st.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    with open(picture_path, "rb") as picture_file:
        response = HttpResponse(picture_file.read(), content_type=mime_type)
        response["Content-Disposition"] = "inline; filename='profile_picture'"
        return response
    
@api_view(["PUT"])
@parser_classes([MultiPartParser])
@permission_classes([IsValidJWTAccessToken])
def update_picture(request: Request):
    """Update user picture handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    profile_serializer = UserProfileSerializer(data=request.data)
    valid_profile_data = profile_serializer.is_valid()
    user_profile = UserProfile(user=user)
    if valid_profile_data:
        try:
            user_profile = UserProfile.objects.filter(user=user).get()
        except UserProfile.DoesNotExist:
            pass
        if user_profile:
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
    """Delete user handler"""
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
    """Make a new access token from refresh token handler"""
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
    
@api_view(["POST"])
@permission_classes([IsValidJWTAccessToken])
def store_recipe_as_bookmark(request: Request):
    """Bookmark recipe handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")
    recipe_bookmark_serializer = RecipeBookmarkSerializer(data=request.data)
    valid = recipe_bookmark_serializer.is_valid()
    if valid:
        try:
            recipe_instance = Recipe.objects.get(title=recipe_bookmark_serializer.validated_data.get("title"))
        except Recipe.DoesNotExist:
            recipe_instance = recipe_bookmark_serializer.save(user=user)
        if not user.recipes.contains(recipe_instance):
            user.recipes.add(recipe_instance)
            user.save()
            return Response({"message": "ok"})
        else:
            return Response({"error": "Recipe already bookmarked by user"}, status=st.HTTP_409_CONFLICT)
    else:
        errors = {}
        if recipe_bookmark_serializer.errors:
            errors.update(recipe_bookmark_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
@permission_classes([IsValidJWTAccessToken])
def remove_recipe_bookmark(request: Request):
    """Remove recipe bookmark from user bookmarks handler"""
    try:
        user = User.objects.get(
            id=get_user_id_from_access_token(request=request))
    except User.DoesNotExist:
        raise Http404("User does not exist")
    
    remove_recipe_bookmark_serializer = RemoveRecipeBookmarkSerializer(data=request.data)
    valid = remove_recipe_bookmark_serializer.is_valid()
    if valid:
        try:
            recipe_instance = Recipe.objects.get(
                title=remove_recipe_bookmark_serializer.validated_data.get("title")
            )
        except Recipe.DoesNotExist:
            return Response({"error": "Recipe not found"}, status=st.HTTP_404_NOT_FOUND)
        
        if user.recipes.filter(id=recipe_instance.id).exists():
            user.recipes.remove(recipe_instance)
            return Response({"message": "Bookmark removed successfully"})
        else:
            return Response({"error": "Recipe not bookmarked by the user"}, status=st.HTTP_204_NO_CONTENT)
    else:
        errors = {}
        if remove_recipe_bookmark_serializer.errors:
            errors.update(remove_recipe_bookmark_serializer.errors)
        return Response(errors, status=st.HTTP_400_BAD_REQUEST)
