import json 

# Ask the user about their favorite number
fav_num = input("What is your favorite number? ")
filename = "favorite_number.json"
with open(filename, "w") as f:
    json.dump(fav_num, f)