"""Runnable examples for Python for AI — Part 2.
Author: Hazem Elshafey

Run with: python code/python_part2_examples.py
Examples are intentionally small and use the Python standard library.
"""
import json
from pathlib import Path


# 1. Functions
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def greet(name, message="Welcome"):
    """Return a greeting with an optional message."""
    return f"{message}, {name}!"


def square(number):
    """Return the square of a number."""
    return number ** 2


print("FUNCTIONS")
print(add(4, 6))
print(greet("Hazem"))
print(square(5))

# 2. Comprehensions and built-ins
print("\nCOMPREHENSIONS")
scores = [0.92, 0.45, 0.87, 0.31]
print([score for score in scores if score >= 0.80])

print("\nENUMERATE")
for index, feature in enumerate(["age", "fare"]):
    print(index, feature)

# 3. Exception handling
print("\nEXCEPTIONS")
try:
    value = int("42")
except ValueError:
    print("Invalid number")
else:
    print(value)
finally:
    print("Finished")

# 4. File handling and JSON
print("\nFILES AND JSON")
demo_path = Path("student_record_demo.json")
student = {"name": "Hazem", "score": 92}
demo_path.write_text(json.dumps(student, indent=2), encoding="utf-8")
loaded_student = json.loads(demo_path.read_text(encoding="utf-8"))
print(loaded_student["name"], loaded_student["score"])
demo_path.unlink(missing_ok=True)

# 5. OOP
print("\nOOP")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}; I am {self.age}."


print(Student("Harry", 23).introduce())

# 6. Inheritance / polymorphism
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


print(Dog().speak())

# 7. Basic tests
print("\nTESTS")
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert square(5) == 25
print("Basic tests passed")
