class FitnessClass:
    """Represents a fitness class in the system."""

    def __init__(self, class_id: str, name: str, instructor: str, location: str, capacity: int):
        self.class_id = class_id
        self.name = name
        self.instructor = instructor
        self.location = location
        self.capacity = capacity
        self.participants = []

    def enroll_user(self, user):
        """Enrolls a user in the class if capacity allows."""
        if len(self.participants) < self.capacity:
            self.participants.append(user)
            return f"User {user.name} enrolled in {self.name}."
        return "Class is full."

    def get_class_details(self):
        """Returns class details."""
        return f"{self.name} by {self.instructor} at {self.location}."
