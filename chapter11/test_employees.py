import unittest
from employees import Employee


class TestEmployeeClass(unittest.TestCase):
    def setUp(self) -> None:
        self.my_employee = Employee("Peter", "Parker", 30_000)
        self.salary_raise = 10_000

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 35_000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.salary_raise)
        self.assertEqual(self.my_employee.annual_salary, 40_000)
