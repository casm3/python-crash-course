from restaurant import Restaurant


"""
9.6 Ice Cream Stand: An ice cream stand is a specif kind of
restauran. Write a class called IceCreamStand that inherits
from the Restaurant class you wrote in Exercise 9.1 or
Exercise 9.4. Either version of the class will work; just
pick the one you like better. Add an attribute called flavors
that stores a list of ice cream flavors.
"""


class IceCreamStand(Restaurant):
    def __init__(
        self, restaurant_name: str,
        cuisine_type: str,
        flavors: list[str],
        number_served: int = 0,
    ) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    """
    9.6 Write a method that displays these flavors.
    """
    def show_flavors(self) -> None:
        print("The available flavors are: ")
        for flavor in self.flavors:
            print(f"\t{flavor}")
