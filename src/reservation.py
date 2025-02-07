from src.fitness_class import FitnessClass
from src.user import User

class Reservation:
    """Handles class reservations for users."""

    def __init__(self, reservation_id: str, user: User, fitness_class: FitnessClass):
        """Initializes a reservation.

        Args:
            reservation_id (str): Unique identifier for the reservation.
            user (User): The user making the reservation.
            fitness_class (FitnessClass): The fitness class being reserved.
        """
        self.reservation_id = reservation_id
        self.user = user
        self.fitness_class = fitness_class

    def confirm_booking(self) -> str:
        """Confirms the user's booking for a class.

        Returns:
            str: Confirmation message including reservation details.
        """
        return f"Reservation {self.reservation_id} confirmed for {self.user.name} in {self.fitness_class.name}."
