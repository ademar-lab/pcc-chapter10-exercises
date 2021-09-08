def show_lines(filename):
    """
    Print the lines in a file or a friendly error message if the file 
    was not found.
    """
    try:    
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.strip())

# Print cats.txt and dogs.txt
filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    show_lines(filename)