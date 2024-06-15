# ------------------------------------------------------------------------------------------------- #
# Title: Application Classes Testing Module
# # Description: Testing the data classes
# ChangeLog: (Who, When, What)
# Jennifer Hernandez-Mora, 06/10/2024,Created Script
# ---------------------------------------------------------------------------------------------------#
import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person(self):
        person = Person("<NAME>", "<NAME>")
        self.assertEqual(person.name, "<NAME>")
        self.assertEqual(last_name, "<NAME>")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("<NAME>", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "Doe")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2024-05-07")
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")

    def test_review_date(self):
        with self.assertRaises(ValueError):
            Employee("Bob", "Johnson", "2024-05-07")

    def test_review_rating(self):
        with self.assertRaises(ValueError):
            Employee("Bob", "Johnson", "2024-05-07")

if __name__ == '__main__':
    unittest.main()



