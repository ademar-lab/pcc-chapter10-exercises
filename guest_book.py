# Promt the user for his name and store their vist in guest_book.txt

with open("guest_book.txt", "w") as file_object:
    print("Enter \"quit\" at any point to finish the program.\n")
    while True:
        user_name = input("What is your name? ")
        if user_name == "quit":
            break
        else:
            print(f"Welcome {user_name.title()}!")
            file_object.write(f"{user_name.title()} visited the site.\n")