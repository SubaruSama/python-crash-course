import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
            return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name?: ')
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)

    return username

def greet_user():
    """Gree the user bt name."""
    username = get_stored_username()
    if username:
        print (f'Welcome back {username}!')
    else:
        username = get_new_username()
        print(f'We\'ll remember when you come back {username}!')

greet_user()