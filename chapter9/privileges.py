"""
9.8 Privileges: Write a separate Privileges class. The
class should have one attribute, privileges, that stores
a list of strings as described in Exercise 9.7. Move
the show_privileges() method to this class. Make a Privileges
instance as an attribute in the Admin class.
"""


class Privileges():
    def __init__(self, privileges: list[str] = [
            "can add post",
            "can delete post",
            "can ban user"
    ]) -> None:
        self.privileges = privileges

    def show_privileges(self) -> None:
        print("The admin privileges are: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")
