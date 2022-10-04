"""
10.10 Common Words: Visit Project Gutenberg (https://gutenberg.org/)
and find a few texts you'd like to analyze. Download the text files
for these works, or copy the raw text from your browser into a text
file on your computer.

You can use count() method to find out how many times a word or phrase
appears in a string. For example, the following code counts the number
of times 'row' appears in a string.

line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')

Notice that converting the string to lowercase using lower()
catches all appearances of the word you're looking for,
regardless of how it's formatted.

Write a Program that reads the files you found at Project
Gutenberg and determines how many times the word 'the' appears
in each text. This will be an approximation because it will also
count words such as 'then' and 'there'. Try couting 'the ' with
a space in the string, and see how much lower your count is.
"""

with open("2641-0.txt") as file_text:
    lines = file_text.readlines()
    count_the, count_the_with_space = 0, 0
    for line in lines:
        count_the += line.lower().count('the')
        count_the_with_space += line.lower().count('the ')
    print(count_the, count_the_with_space)
