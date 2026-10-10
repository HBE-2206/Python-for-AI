"""HBE_2206 | Python Part 1 — Exercise Solutions
These are reference solutions; other correct approaches may exist.
"""

# 1
model_name = "baseline"
sample_count = 120
accuracy = 0.91
print(type(model_name), type(sample_count), type(accuracy))

# 2 — Run interactively:
# number = int(input("Enter an integer: "))
# print(number ** 2)

# 3
text = "  Machine Learning  "
print(text.strip().lower())

# 4
scores = [0.70, 0.85, 0.92]
scores.append(0.96)
scores[0] = 0.75
print(scores)

# 5
metrics = {"accuracy": 0.92, "recall": 0.88}
print(metrics.get("precision", 0.0))

# 6
number = -3
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# 7
for number in range(-5, 6):
    print(number)

# 8
confidence_scores = [0.92, 0.45, 0.87, 0.31, 0.96]
print([score for score in confidence_scores if score >= 0.80])

# 9
labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
print(counts)

# 10
numbers = [1, 2, 3, 4]
squares = {number: number ** 2 for number in numbers}
print(squares)

# 11
scores = [0.70, 0.85, 0.92, 0.96]
summary = {
    "count": len(scores),
    "min": min(scores),
    "max": max(scores),
    "average": sum(scores) / len(scores),
}
print(summary)

# 12
values = ["AI", " ", "Python", "", "Data"]
clean_values = [value.strip() for value in values if value.strip()]
print(clean_values)

# 13
keys = ["name", "accuracy"]
values = ["baseline", 0.91]
combined = dict(zip(keys, values))
print(combined)

# 14 — Run interactively:
# while True:
#     command = input("Enter a command (q to quit): ").strip().lower()
#     if command == "q":
#         print("Goodbye!")
#         break
#     print("You entered:", command)

# 15
# list: ordered mutable sequence; tuple: fixed ordered record;
# set: unique values; dict: key-value lookup.
