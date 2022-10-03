from car import Car
from battery import Battery


"""
9.9 Battery Upgrade: Use the final version of electric_car.py
from this section. Add a method to the Battery class called
upgrade_battery(). This method should check the battery size and
set the capacity to 100 if it isn't already.
"""


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = Battery()
