# Python Part 2 — Exercises

Try these exercises before opening `part-2/solutions.py`. Each task is intended to reinforce a topic from the study notebook.

## A. Functions
1. Write `is_even(number)` that returns True when a number is even.
2. Write `calculate_discount(price, percentage=10)` and return the final price.
3. Write `count_vowels(text)` and return the number of vowels, ignoring case.

## B. Comprehensions and built-ins
4. Given a list of numbers, create a list containing only positive even numbers.
5. Use `enumerate()` to print each item in a list with a 1-based number.
6. Use `zip()` to combine a list of names and a list of scores into pairs.

## C. Exceptions and validation
7. Write `parse_score(value)` that converts a value to float and returns None if conversion fails or the score is outside 0–100.
8. Explain the difference between SyntaxError, ValueError, and IndexError.

## D. Files and JSON
9. Write a dictionary with a student's name and score to a JSON file.
10. Load that file and print the student's name. Handle a missing file gracefully.

## E. OOP
11. Create a `Student` class with name and score attributes and a `passed()` method that returns True when score >= 50.
12. Create an `Animal` parent class and a `Dog` child class that overrides `speak()`.

## F. Testing
13. Write at least four assertions for a function you created.
14. Include normal, boundary, and invalid input cases.

## Mini-project: Student Record Manager
Build a command-line program that can add records, validate scores, calculate an average, save/load JSON, and handle invalid data. Split the program into functions and add tests.

## Submission checklist
- [ ] Code runs without syntax errors.
- [ ] Functions have clear names and docstrings where useful.
- [ ] Invalid input is handled intentionally.
- [ ] JSON data can be saved and loaded.
- [ ] At least five meaningful tests are included.
