# Poll users about the reason the they like programming

with open("programming_poll.txt", "w") as file_object:
    print("Enter \"quit\" at any time to finish the program:\n")
    while True:
        reason = input("Why do you like programming? ")
        if reason == "quit":
            break
        else:
            print("That's a great reason!")
            file_object.write(reason.lower())
