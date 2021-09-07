# Change the word Python to C

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line.strip())