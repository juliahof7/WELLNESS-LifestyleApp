from flask import Flask, jsonify, request
from src.user import User
from src.fitness_class import FitnessClass
from src.reservation import Reservation

app = Flask(__name__)

# Dummy data for testing
users = {}
fitness_classes = {
    "F001": FitnessClass(class_id="F001", name="Morning Yoga", instructor="Emma", location="Beach Studio", capacity=10)
}
reservations = {}

@app.route('/')
def home():
    """Home route for API.

    Returns:
        str: Simple confirmation message.
    """
    return "WELLNESS-LifestyleApp Backend is Running!"

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user.

    Expects JSON data with user details.

    Returns:
        JSON: Confirmation message.
    """
    data = request.json
    user_id = data.get("user_id")
    user = User(user_id=user_id, name=data["name"], email=data["email"], password=data["password"], location=data["location"])
    users[user_id] = user
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user by checking credentials.

    Expects JSON with email and password.

    Returns:
        JSON: Success or error message.
    """
    data = request.json
    email = data["email"]
    password = data["password"]
    for user in users.values():
        if user.email == email and user.password == password:
            return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/fitness_classes', methods=['GET'])
def get_fitness_classes():
    """Retrieves all available fitness classes.

    Returns:
        JSON: A dictionary of class details.
    """
    return jsonify({class_id: cls.get_class_details() for class_id, cls in fitness_classes.items()})

@app.route('/book_class', methods=['POST'])
def book_class():
    """Books a fitness class for a user.

    Expects JSON with user ID and class ID.

    Returns:
        JSON: Confirmation message or error message.
    """
    data = request.json
    user_id = data["user_id"]
    class_id = data["class_id"]
    if user_id in users and class_id in fitness_classes:
        reservation_id = f"R00{len(reservations) + 1}"
        reservation = Reservation(reservation_id=reservation_id, user=users[user_id], fitness_class=fitness_classes[class_id])
        reservations[reservation_id] = reservation
        return jsonify({"message": "Class booked successfully!", "reservation_id": reservation_id})
    return jsonify({"error": "Invalid user or class ID"}), 400

if __name__ == '__main__':
    app.run(debug=True)
