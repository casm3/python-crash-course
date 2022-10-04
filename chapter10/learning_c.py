"""
10.2 Learning C: You can use the replace() method to replace any
word in a string with a different word. Here's a quick example
showing how to replace 'dog' with 'cat' in a sentence:

message = 'I really like dogs.'
message.replace('dog', 'cat')

Read each line from the file you just created, learning_python.txt
and replace the word Python with the name of another language, such as C.
Print each modified line to the screen.
"""


def read_file(path: str):
    with open(path) as text_file:
        lines = text_file.readlines()

    for line in lines:
        print(line.replace("Python", "C").strip())


read_file("learning_python.txt")
