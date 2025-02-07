import unittest
from src.user import User
from src.fitness_class import FitnessClass
from src.reservation import Reservation

class TestReservation(unittest.TestCase):
    def setUp(self):
        """Set up a user, class, and reservation for testing."""
        self.user = User(user_id="U001", name="Julia", email="julia@example.com", password="secure123", location="California")
        self.fitness_class = FitnessClass(class_id="F001", name="Yoga", instructor="Emma", location="Studio", capacity=10)
        self.reservation = Reservation(reservation_id="R001", user=self.user, fitness_class=self.fitness_class)

    def test_confirm_booking(self):
        """Test reservation confirmation."""
        self.assertEqual(self.reservation.confirm_booking(), "Reservation R001 confirmed for Julia in Yoga.")

if __name__ == '__main__':
    unittest.main()
