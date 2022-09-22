from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from decimal import Decimal


class ModelTests(TestCase):
    def test_creat_user(self):
        email = 'test@example.com'
        password = "testpwd"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, test_email in emails:
            user = get_user_model().objects.create_user(email, '#')
            self.assertEqual(user.email, test_email)

    def test_user_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '#')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com', '#'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'mypassword'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            recipe_name='Test Recipe',
            price=Decimal(6.6),
            detail_text='Test Text',
        )
        self.assertEqual(str(recipe), recipe.recipe_name)
