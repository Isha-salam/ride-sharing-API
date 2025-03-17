from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()  # Correct way to use the custom user model

class RideSharingTests(TestCase):
    def setUp(self):
        """Create test data before each test."""
        self.user = User.objects.create_user(
            username="rider1", password="testpass"
        )  # Ensure this works with CustomUser

    def test_create_driver(self):
        """Test driver creation logic"""
        driver = User.objects.create_user(
            username="driver1", password="testpass", is_driver=True
        )
        self.assertTrue(driver.is_driver)


