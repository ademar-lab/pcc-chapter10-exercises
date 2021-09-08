import json

# Print the favorite number introduced in favorite_number.py
filename = "favorite_number.json"
with open(filename) as f:
    fav_num = json.load(f)
print(f"This is your favorite number: {fav_num}!")