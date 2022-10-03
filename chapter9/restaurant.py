"""
9.1 Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
"""


class Restaurant():
    def __init__(
        self, restaurant_name: str,
        cuisine_type: str,
        number_served: int = 0
    ) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    """
    9.4 Number Served: Start with your program from Exercise 9.1. Add an
    attributed called number_served with a default value of 0.
    """

    def describe_restaurant(self) -> None:
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self) -> None:
        print(f"The {self.restaurant_name} is open.")

    """
    9.4 Add a method called set_number_served() that lets you set the number
    of customers that have been served.
    """
    def set_number_served(self, new_number_served: int) -> None:
        self.number_served = new_number_served

    """
    9.4 Add a method called increment_number_served() that lets you increment
    the number of customers who'have been served.
    """
    def increment_number_served(self, served_in_day: int) -> None:
        self.number_served += served_in_day
