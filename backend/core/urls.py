"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import accounts.views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", accounts.views.status),
    path("api/user/register", accounts.views.signup),
    path("api/user/info", accounts.views.user_info),
    path("api/user/update_data", accounts.views.update_data),
    path("api/user/update_email", accounts.views.update_email),
    path("api/user/update_picture", accounts.views.update_picture),
    path("api/user/profil", accounts.views.user_profile, name="get user profil"),
    path("api/user/update_password", accounts.views.update_password),
    path("api/user/delete", accounts.views.delete_user),
    path("api/user/login", accounts.views.login),
    path("api/token/refresh", accounts.views.refresh_token),
    path("api/recipe/bookmark", accounts.views.store_recipe_as_bookmark),
    path("api/recipe/remove_bookmark", accounts.views.remove_recipe_bookmark),
    path("api/recipe/get_bookmarks", accounts.views.user_recipe_bookmark),
    path("admin/", admin.site.urls),
    path("api/doc/", include("rest_framework.urls")),
]
