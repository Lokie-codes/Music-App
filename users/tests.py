from django.test import TestCase
from .user_manager import UserManager
from .models import CustomUser

# User tests here.
class UserTestCase(TestCase):
    def test_create_user(self):
        # Test creating a regular user
        User = CustomUser
        email = 'test@example.com'
        password = 'testpassword'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        # Test creating a superuser
        User = CustomUser
        email = 'admin@example.com'
        password = 'adminpassword'
        user = User.objects.create_superuser(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
