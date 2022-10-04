"""
10.8 Cats and Dogs: Make two files, cats.txt and dogs.txt.
Store at least three names of cats in the first file and
three names of dogs in the second file. Write a program
that tries to read these files and print the contents of
the file to the screen. Wrap your code in a try-except
block to catch the FileNotFound error, and print a friendly
message if a file is missing. Move one of the files to a
different location on your system, and make sure the code
in the except block executes properly.
"""

try:
    with open("cats.txt") as cats_file:
        lines = cats_file.readlines()
        for line in lines:
            print(line.rstrip())

    with open("dogs.txt") as dogs_file:
        lines = dogs_file.readlines()
        for line in lines:
            print(line.rstrip())
except FileNotFoundError:
    print("The file doesn't exist.")

"""
10.9 Silent Cats and Dogs: Modify your except block in
Exercise 10.8 to fail silently if either file is missing.
"""

try:
    with open("cats.txt") as cats_file:
        lines = cats_file.readlines()
        for line in lines:
            print(line.rstrip())

    with open("dogs.txt") as dogs_file:
        lines = dogs_file.readlines()
        for line in lines:
            print(line.rstrip())
except FileNotFoundError:
    pass
