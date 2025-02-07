import unittest
from src.fitness_class import FitnessClass
from src.user import User

class TestFitnessClass(unittest.TestCase):
    def setUp(self):
        """Set up a sample fitness class for testing."""
        self.fitness_class = FitnessClass(class_id="F001", name="Yoga", instructor="Emma", location="Studio", capacity=2)
        self.user = User(user_id="U001", name="Julia", email="julia@example.com", password="secure123", location="California")

    def test_get_class_details(self):
        """Test retrieving class details."""
        self.assertEqual(self.fitness_class.get_class_details(), "Yoga by Emma at Studio.")

    def test_enroll_user(self):
        """Test user enrollment in a class."""
        self.assertEqual(self.fitness_class.enroll_user(self.user), "User Julia enrolled in Yoga.")
        self.assertEqual(self.fitness_class.enroll_user(self.user), "User Julia enrolled in Yoga.")  # Should still allow

    def test_enroll_full_class(self):
        """Test enrollment when class is full."""
        user2 = User(user_id="U002", name="John", email="john@example.com", password="pass123", location="California")
        self.fitness_class.enroll_user(self.user)
        self.fitness_class.enroll_user(user2)
        user3 = User(user_id="U003", name="Mike", email="mike@example.com", password="pass456", location="California")
        self.assertEqual(self.fitness_class.enroll_user(user3), "Class is full.")

if __name__ == '__main__':
    unittest.main()
