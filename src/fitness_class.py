class FitnessClass:
    """Represents a fitness class in the system."""

    def __init__(self, class_id: str, name: str, instructor: str, location: str, capacity: int):
        """Initializes a fitness class.

        Args:
            class_id (str): Unique identifier for the class.
            name (str): Name of the fitness class.
            instructor (str): Name of the instructor.
            location (str): Location where the class takes place.
            capacity (int): Maximum number of participants.
        """
        self.class_id = class_id
        self.name = name
        self.instructor = instructor
        self.location = location
        self.capacity = capacity
        self.participants = []

    def enroll_user(self, user) -> str:
        """Enrolls a user in the class if space is available.

        Args:
            user (User): The user attempting to enroll.

        Returns:
            str: Confirmation message if enrollment is successful, otherwise an error message.
        """
        if len(self.participants) < self.capacity:
            self.participants.append(user)
            return f"User {user.name} enrolled in {self.name}."
        return "Class is full."

    def get_class_details(self) -> str:
        """Returns class details.

        Returns:
            str: A formatted string with class details.
        """
        return f"{self.name} by {self.instructor} at {self.location}."
