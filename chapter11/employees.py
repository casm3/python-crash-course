"""
11.3 Employee: Write a class called Employee. The __init__()
method should take in a first name, a last name, and an
annual salary, and store each of these as attributes. Write
a method called give_raise() that adds $5_000 to the annual
salary by default, but also accepts a different raise amount.

Write a test case for Employee. Write two test methods,
test_give_default_raise() and test_given_custom_raise().
Use the setUp() method so you don't have to create a new
employee instance in each test method. Run your test case,
and make sure both tests pass.
"""


class Employee:
    def __init__(self, first_name: str, last_name: str, annual_salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise: float = 5_000):
        self.annual_salary += salary_raise
