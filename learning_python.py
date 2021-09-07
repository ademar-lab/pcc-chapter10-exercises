# Use the with block to print the same file, but read differently 

print("Read the entire file and store the string in a variable to work with it "
    "outside the with block:")
with open("learning_python.txt") as file_object:
    contents = file_object.read()
print(f"{contents}\n")

print("Loop over the file object:")
with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line.rstrip())
# Print an empty string to space the output
print("")

print("Store the lines in a list and work with them outside the with block:")
with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

    

