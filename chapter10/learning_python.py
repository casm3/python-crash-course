"""
10.1 Learning Python: Open a blank file in your text editor
and write a few lines summarizing what you've learned about
Python so far. Start each line with the prase In Python you
can.... Save the file as learning_python.txt in the same
directory as your exercises from this chapter. Write a program
that reads the file and prints what you wrote three times.
Print the contents once by reading in reding in the entire
file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside with
the with block,
"""


def read_file(path: str):
    with open(path) as text_file:
        print(text_file.read())

    with open(path) as text_file:
        for line in text_file:
            print(line)

    with open(path) as text_file:
        lines = text_file.readlines()

    for line in lines:
        print(line.strip())


read_file("learning_python.txt")
