"""
10.11 Favorite Number: Write a program that prompts for the
user's favorite number. Use json.dump() to store this number
in a file. Write a separate program that reads in this value
and prints the message, "I know your favorite number!  It's
_____."
"""
import json


favorite_number = int(input("Enter your favorite number: "))
user_favorite_number = {"favorite_number": favorite_number}
with open("fav_number.json", mode="w") as json_file:
    json.dump(user_favorite_number, json_file)

with open("fav_number.json", mode="r") as json_file:
    dict_object = json.load(json_file)
    print(
        f"I know your favorite number! It's {dict_object['favorite_number']}."
    )

"""
10.12 Favorite Number Remembered: Combine the two programs
from exercise 10.11 into one file. If the number is already
stored, report the favorite number to the user. If not,
prompt for the user's favorite number and store it in a
file. Run the program twice to see that it works.
"""

with open("fav_number.json", mode="r") as json_file:
    dict_object = json.load(json_file)
    if dict_object.get('favorite_number'):
        print(
            f"I know your favorite number!\n"
            f"It's {dict_object['favorite_number']}."
        )
    else:
        favorite_number = int(input("Enter your favorite number: "))
        user_favorite_number = {"favorite_number": favorite_number}
        json.dump(user_favorite_number, json_file)
