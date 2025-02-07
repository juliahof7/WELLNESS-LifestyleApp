from src.user import User
from src.fitness_class import FitnessClass
from src.reservation import Reservation

# Create a user
user1 = User(user_id="U001", name="Julia", email="julia@example.com", password="secure123", location="California")

print("🔹 User Registration:")
print(user1.register())  # Test registration

print("\n🔹 User Login:")
print(user1.login("julia@example.com", "secure123"))  # Test successful login
print(user1.login("wrong@example.com", "wrongpass"))  # Test failed login

# Create a fitness class
yoga_class = FitnessClass(class_id="F001", name="Morning Yoga", instructor="Emma", location="Beach Studio", capacity=10)

print("\n🔹 Fitness Class Details:")
print(yoga_class.get_class_details())

# Book a class
reservation1 = Reservation(reservation_id="R001", user=user1, fitness_class=yoga_class)

print("\n🔹 Booking Confirmation:")
print(reservation1.confirm_booking())

# Check class enrollment
print("\n🔹 Enrolling User in Class:")
print(yoga_class.enroll_user(user1))
print(yoga_class.enroll_user(user1))  # Attempt to enroll again

