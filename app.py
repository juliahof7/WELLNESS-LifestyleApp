from user import User
from fitness_class import FitnessClass
from reservation import Reservation

# Create a user
user1 = User(user_id="U001", name="Julia", email="julia@example.com", password="secure123", location="California")

# User registers and logs in
print(user1.register())
print(user1.login("julia@example.com", "secure123"))

# Create a fitness class
yoga_class = FitnessClass(class_id="F001", name="Morning Yoga", instructor="Emma", location="Beach Studio", capacity=10)

# User searches for fitness classes
print(user1.search_fitness_classes(user1.location))

# User books a class
reservation1 = Reservation(reservation_id="R001", user=user1, fitness_class=yoga_class)
print(reservation1.confirm_booking())

# Display class details
print(yoga_class.get_class_details())
