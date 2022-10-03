from random import randint


"""
9.13 Dice: Make a class Die with one attribute called sizes,
which has a default value of 6. Write a method called roll_die()
that prints a random number between 1 and the number of sides the
die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""


class Die:
    def __init__(self, sizes: int = 6) -> None:
        self.sizes = sizes

    def roll_die(self):
        print(randint(1, self.sizes))
