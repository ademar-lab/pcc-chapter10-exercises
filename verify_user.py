import json

def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username

def greet_user(filename):
    username = get_stored_username(filename)
    # Ask if the stored username is the right username
    if username:
        active = input("Enter \"yes\" to confirm.\n"
            f"Is this: {username} your username? ")
        if active == "yes":
            print(f"Welcome back {username}!")
        else:
            get_new_username(filename)
    # Store a new user name if the file didn't exist         
    else:
        get_new_username(filename)

def get_new_username(filename):
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

filename = "username.json"
greet_user(filename)