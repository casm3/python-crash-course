"""
10.3 Guest: Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt.
"""
user_name = input("Enter your name: ")
with open("guest.txt", mode="w") as text_file:
    text_file.writelines(user_name)

"""
10.4 Guest Book: Wrote a while loop that prompts users for their
name. When they enter their name, print a greeting to the screen
and add a line recording their visit in a file called guest_book.txt
make sure each entry appears on a new line in the file.
"""
user_name = input("Enter your name or type 'quit' to exit: ")

while user_name != 'quit':
    print(f"Welcome, {user_name}.")
    with open("guest_book.txt", mode="a") as text_file:
        text_file.writelines(user_name + "\n")
    user_name = input("Enter your name or type 'quit' to exit: ")

"""
10.5 Programming Poll: Write a while loop that asks people why they
like programing. Each time someone enters a reason, add their reason
to a file that stores all responses.
"""
poll_vote = input("Why do you like Programming? Type 'quit' to exit: ")

while poll_vote != 'quit':
    with open("votes.txt", mode="a") as text_file:
        text_file.writelines(poll_vote + "\n")
    poll_vote = input("Why do you like Programming? Type 'quit' to exit: ")
