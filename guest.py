# Prompt the user for their name
guest = input("What is your name? ")

# Store the user's name in guest.txt
with open("guest.txt", "w") as file_object:
    file_object.write(guest.lower())