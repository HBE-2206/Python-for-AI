"""Reference solutions for Python Part 2 exercises.
Try the exercises independently before reading this file.
"""
import json
from pathlib import Path


def is_even(number):
    return number % 2 == 0


def calculate_discount(price, percentage=10):
    if price < 0:
        raise ValueError("price must be non-negative")
    if not 0 <= percentage <= 100:
        raise ValueError("percentage must be between 0 and 100")
    return price * (1 - percentage / 100)


def count_vowels(text):
    return sum(character.lower() in "aeiou" for character in text)


def positive_evens(numbers):
    return [number for number in numbers if number > 0 and number % 2 == 0]


def parse_score(value):
    try:
        score = float(value)
    except (TypeError, ValueError):
        return None
    return score if 0 <= score <= 100 else None


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 50


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


def save_records(records, path):
    Path(path).write_text(json.dumps(records, indent=2), encoding="utf-8")


def load_records(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    assert is_even(8) is True
    assert is_even(7) is False
    assert calculate_discount(100) == 90
    assert calculate_discount(100, 25) == 75
    assert count_vowels("Python") == 1
    assert positive_evens([-2, 0, 1, 2, 4]) == [2, 4]
    assert parse_score("87.5") == 87.5
    assert parse_score("bad") is None
    assert parse_score(101) is None
    assert Student("Mona", 80).passed() is True
    assert Dog().speak() == "Woof!"
    print("All reference checks passed.")
