def count_text(word, filename):
    """Count how many times a word appears in a file."""
    appearances = 0
    try:
        with open(filename) as f:
            for line in f:
                appearances += line.lower().count(word)
    except FileNotFoundError:
        print(f"The file {filename} wasn't found.")
    else:
        return(appearances)

filenames = ["alice.txt", "wizard_of_oz.txt", "the_little_prince.txt"]

# Count how many times "the" appears in the files
print("\"the\" appears:")
for filename in filenames:
    the_times = count_text("the", filename)
    if the_times:
        print(f"\t{the_times} times in {filename}.")
print("")

# Count how many times "the " appears in the files
print("\"the \" appears:")
for filename in filenames:
    the_times = count_text("the ", filename)
    if the_times:
        print(f"\t{the_times} times in {filename}.")
print("")

# Count how many times "the " appears in the files
print("\" the \" appears:")
for filename in filenames:
    the_times = count_text(" the ", filename)
    if the_times:
        print(f"\t{the_times} times in {filename}.")