import json
import bcrypt
import os

USER_FILE = "users.json"


def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return {}
        return json.loads(content)


def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())


# ========== REGISTER ==========
def register(username, password):
    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": hash_password(password),
        "role": "user"
    }

    save_users(users)
    return True


# ========== LOGIN ==========
def login(username, password):
    users = load_users()

    if username in users:
        if check_password(password, users[username]["password"]):
            return users[username]["role"]

    return None
