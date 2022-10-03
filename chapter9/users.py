"""
9.3 Users: Make a class called User. Create two attributes called
first_name and last_name, and then create several other attributes
that are typically stored in a user profile. Make a method called
describe_user() that prints a summary of the user's information.
Make another method called greet_user() that prints a summary of
the user's information. Make another method called greet_user()
that prints a personalized greeting to the user.
"""


class User():
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: int,
        login_attempts: int = 0
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = login_attempts
    """
    9.5 Login Attempts: Add an attribute called login_attempts to your User
    class from Exercise 9.3.
    """

    def describe_user(self):
        print(f"The user full name is {self.first_name} {self.last_name}.")
        print(f"He/she is {self.age} years old.")
        print(f"The electronic contact address is {self.email}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}. Nice to see you again.")

    """
    9.5 Write a method called increment_login_attempts()
    that increments the value of login_attempts by 1.
    """
    def increment_login_attempts(self):
        self.login_attempts += 1

    """
    9.5 Write another method called reset_login_attempts() that resets
    the value of login_attempts to 0.
    """
    def reset_login_attempts(self):
        self.login_attempts = 0
