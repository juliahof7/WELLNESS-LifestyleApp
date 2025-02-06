class Reservation:
    """Handles class reservations for users."""

    def __init__(self, reservation_id: str, user: User, fitness_class: FitnessClass):
        self.reservation_id = reservation_id
        self.user = user
        self.fitness_class = fitness_class

    def confirm_booking(self):
        """Confirms the user's booking for a class."""
        return f"Reservation {self.reservation_id} confirmed for {self.user.name} in {self.fitness_class.name}."
