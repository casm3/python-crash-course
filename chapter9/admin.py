from users import User
from privileges import Privileges


"""
9.7 Admin: An administrator is a special kind of user.
Write a class called Admin that inherits from the user
class you wrote in Exercise 9.3 or Exercise 9.5. Add an
attribute, privileges, that stores a list of strings
like "can add post", "can delete post", "can ban user",
and so on. Write a method called show_privileges() that
lists the administrator's set of privileges.
"""


class Admin(User):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: int,
        login_attempts: int = 0,
    ) -> None:
        super().__init__(first_name, last_name, email, age, login_attempts)
        self.privileges = Privileges()
