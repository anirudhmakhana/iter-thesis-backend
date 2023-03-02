from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            firstname='John',
            lastname='Doe',
            tc=True,
            password='password123',
            password2='password123'
        )

    def test_create_user(self):
        """Test creating a new user"""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.firstname, 'John')
        self.assertEqual(self.user.lastname, 'Doe')
        self.assertEqual(self.user.tc, True)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            firstname='Admin',
            lastname='User',
            tc=True,
            password='password123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.firstname, 'Admin')
        self.assertEqual(admin_user.lastname, 'User')
        self.assertEqual(admin_user.tc, True)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)