from services.auth_service import register, login

def handle_signup(username, password):
    return register(username, password)

def handle_login(username, password):
    return login(username, password)
