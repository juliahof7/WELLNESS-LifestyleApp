class User:
    """Represents a user in the WELLNESS app."""

    def __init__(self, user_id: str, name: str, email: str, password: str, location: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.location = location

    def register(self):
        """Registers a new user."""
        return f"User {self.name} registered successfully."

    def login(self, email: str, password: str):
        """Logs the user into the system."""
        if self.email == email and self.password == password:
            return "Login successful."
        return "Invalid credentials."

    def search_fitness_classes(self, location: str):
        """Searches for fitness classes in the given location."""
        return f"Searching for fitness classes in {location}."

    def book_class(self, class_id: str):
        """Books a fitness class."""
        return f"Class {class_id} booked successfully."

    def view_bookings(self):
        """Displays all booked fitness classes."""
        return "Displaying all booked classes."
