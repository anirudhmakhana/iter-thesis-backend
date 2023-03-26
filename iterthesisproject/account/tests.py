from django.test import TestCase
from .models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            firstname='John',
            lastname='Doe',
            tc=True,
            password='password'
        )
        self.admin_user = User.objects.create_superuser(
            email='admin@example.com',
            firstname='Admin',
            lastname='User',
            tc=True,
            password='password'
        )

    def test_user_creation(self):
        """Test user creation"""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.firstname, 'John')
        self.assertEqual(self.user.lastname, 'Doe')
        self.assertEqual(self.user.tc, True)
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_admin, False)

    def test_superuser_creation(self):
        """Test superuser creation"""
        self.assertEqual(self.admin_user.email, 'admin@example.com')
        self.assertEqual(self.admin_user.firstname, 'Admin')
        self.assertEqual(self.admin_user.lastname, 'User')
        self.assertEqual(self.admin_user.tc, True)
        self.assertEqual(self.admin_user.is_active, True)
        self.assertEqual(self.admin_user.is_admin, True)

    def test_user_str_method(self):
        """Test User __str__ method"""
        self.assertEqual(str(self.user), 'test@example.com')

    def test_user_has_perm(self):
        """Test User has_perm method"""
        self.assertEqual(self.user.has_perm('test_perm'), False)
        self.assertEqual(self.admin_user.has_perm('test_perm'), True)

    def test_user_has_module_perms(self):
        """Test User has_module_perms method"""
        self.assertEqual(self.user.has_module_perms('test_module'), True)
        self.assertEqual(self.admin_user.has_module_perms('test_module'), True)