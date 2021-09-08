import json 

def store_num(filename):
    """Store a number in a JSON format file."""
    number= input("What is your favorite number? ")
    with open(filename, "w") as f:
        json.dump(int(number), f)

def show_num(filename):
    """Print a number stored in a JSON format file."""
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        store_num(filename)
        print("We'll remember your number when you come back!")
    else:
        print(f"This is your favorite number: {number}!")

def upgrade_num(filename):
    """
    Let the user choose to upgrade the number stored in a JSON format file.
    """
    active = input("Enter \"yes\" if you want to upgrade your favorite number. ")
    if active == "yes":
        store_num(filename)

filename = "favorite_number.json"
show_num(filename)
upgrade_num(filename)