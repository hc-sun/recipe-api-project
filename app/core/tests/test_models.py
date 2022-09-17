from django.test import TestCase
from django.contrib.auth import get_user_model

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