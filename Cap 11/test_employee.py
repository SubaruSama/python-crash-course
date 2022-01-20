import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self) -> None:
        self.employee = Employee('John', 'Doe', 3000)

    def test_give_default_raise(self) -> bool:
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 8000)

    def test_give_custom_raise(self) -> bool:
        self.employee.give_raise(7000)
        self.assertEqual(self.employee.salary, 10000)

unittest.main()