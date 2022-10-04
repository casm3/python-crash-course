"""
10.6 Addition: One common problem when prompting for numerical
input occurs when people provide text instead of numbers. When
you try to convert the input to an int, you'll get a ValueError.
Write a Program that prompts for two numbers. Add them together
and print the result. Catach the ValueError if either input
value is not a number, and print a friendly error message. Test
your program by entering two numbers and then by entering some
text instead of a number.
"""

"""
10.7 Addition Calculator: Wrap your code from exercise 10.6
in a while loop so the user can continue entering numbers even
if they make a mistake and enter text instead of a number.
"""
while True:
    num1 = input("Enter the first number: ")
    if num1 == 'quit':
        break
    num2 = input("Enter the second number: ")
    if num2 == 'quit':
        break
    try:
        print(int(num1) + int(num2))
    except ValueError:
        print("You should enter a number not some text.")
