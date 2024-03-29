import uuid
from django.test import TestCase
from accounts.models import Recipe, User, UserProfile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


class TestRecipeModel(TestCase):
    def test_recipe_count(self):
        recipe1 = Recipe.objects.create(
            description="Test recipe", category="Main", title="Recipe Title"
        )
        self.assertEqual(Recipe.objects.count(), 1)
        recipe2 = Recipe.objects.create(
            description="Test recipe 2", category="Main", title="recipe2"
        )
        self.assertEqual(Recipe.objects.count(), 2)

    def test_recipe_id_field(self):
        recipe = Recipe.objects.create(
            description="Test recipe", category="Main", title="Recipe Title"
        )
        self.assertIsInstance(recipe.id, uuid.UUID)
        self.assertEqual(Recipe.objects.first().id, recipe.id)

    def test_recipe_description_field(self):
        recipe = Recipe.objects.create(
            description="Test recipe description", category="Main", title="Recipe Title"
        )
        self.assertEqual(Recipe.objects.first().description, "Test recipe description")

    def test_recipe_category_field(self):
        recipe = Recipe.objects.create(
            description="Test recipe", category="Main", title="Recipe Title"
        )
        self.assertEqual(Recipe.objects.first().category, "Main")

    def test_recipe_title_field(self):
        recipe = Recipe.objects.create(
            description="Test recipe", category="Main", title="Recipe Title"
        )
        self.assertEqual(Recipe.objects.first().title, "Recipe Title")


class TestUserModel(TestCase):

    def test_user_id_field(self):
        user = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        self.assertIsInstance(user.id, uuid.UUID)
        self.assertEqual(User.objects.first().id, user.id)

    def test_user_permissions(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )

        self.assertEqual(User.objects.first().is_staff, False)
        self.assertEqual(User.objects.first().is_superuser, False)

    def test_user_first_name_field(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        self.assertEqual(User.objects.first().first_name, "John")

    def test_user_last_name_field(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        self.assertEqual(User.objects.first().last_name, "Doe")

    def test_user_username_field(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        self.assertEqual(User.objects.first().username, "johndoe")

    def test_user_email_field(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        self.assertEqual(User.objects.first().email, "johndoe@example.com")


class TestUserProfileModel(TestCase):

    def test_user_profile_user_field(self):
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        profile = UserProfile.objects.create(user=user)
        self.assertEqual(UserProfile.objects.first().user, user)

    def test_user_profile_picture_field(self):
        user = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="12345",
        )
        profile = UserProfile.objects.create(user=user, picture="test.jpg")
        self.assertEqual(UserProfile.objects.first().picture.name, "test.jpg")
        
class TestJWTToken(TestCase):
    def test_access_token():
        pass
