from flask_login import UserMixin

# Dummy user store for now (replace with real DB later)
users = {
    "admin": {"password": "admin123"}
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

def get_user(username):
    if username in users:
        user = User(username)
        return user
    return None

def validate_login(username, password):
    return username in users and users[username]["password"] == password
