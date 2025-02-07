class User:
    """Represents a user in the WELLNESS app."""

    def __init__(self, user_id: str, name: str, email: str, password: str, location: str):
        """Initializes a new user.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): User's full name.
            email (str): User's email address.
            password (str): User's password.
            location (str): User's current location.
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.location = location

    def register(self) -> str:
        """Registers a new user.

        Returns:
            str: Confirmation message for successful registration.
        """
        return f"User {self.name} registered successfully."

    def login(self, email: str, password: str) -> str:
        """Logs the user into the system.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            str: Success message if login is correct, otherwise an error message.
        """
        if self.email == email and self.password == password:
            return "Login successful."
        return "Invalid credentials."

    def search_fitness_classes(self, location: str) -> str:
        """Searches for fitness classes in a given location.

        Args:
            location (str): The location to search for classes.

        Returns:
            str: Message indicating where classes are being searched.
        """
        return f"Searching for fitness classes in {location}."

    def book_class(self, class_id: str) -> str:
        """Books a fitness class.

        Args:
            class_id (str): The ID of the class to be booked.

        Returns:
            str: Confirmation message for booking.
        """
        return f"Class {class_id} booked successfully."

    def view_bookings(self) -> str:
        """Displays all booked fitness classes.

        Returns:
            str: Message indicating booked classes are being displayed.
        """
        return "Displaying all booked classes."
