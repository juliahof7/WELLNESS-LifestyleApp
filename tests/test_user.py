import unittest
from src.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Create a sample user for testing."""
        self.user = User(user_id="U001", name="Julia", email="julia@example.com", password="secure123", location="California")

    def test_register(self):
        """Test user registration."""
        self.assertEqual(self.user.register(), "User Julia registered successfully.")

    def test_login_success(self):
        """Test successful login."""
        self.assertEqual(self.user.login("julia@example.com", "secure123"), "Login successful.")

    def test_login_failure(self):
        """Test login with incorrect credentials."""
        self.assertEqual(self.user.login("wrong@example.com", "wrongpass"), "Invalid credentials.")

if __name__ == '__main__':
    unittest.main()
