"""
HBE_2206 | Python Part 1
Core Python Foundations — runnable examples.

Run with: python python_part1_examples.py
"""

# 1. Variables and data types
model_name = "baseline_classifier"
sample_count = 120
accuracy = 0.91
is_trained = True
print("Model:", model_name)
print("Samples:", sample_count)
print("Accuracy:", accuracy)
print("Trained:", is_trained)

# 2. Type conversion
raw_value = "42"
numeric_value = int(raw_value)
print(numeric_value + 8)  # 50

# 3. Operators
total_samples = 17
print(total_samples // 5)  # 3
print(total_samples % 5)   # 2

# 4. Strings
topic = "Machine Learning"
print(topic[0])       # M
print(topic[:7])      # Machine
print(topic.lower())  # machine learning
print("  data  ".strip())  # data

# 5. Lists
features = ["age", "fare", "class"]
features.append("sex")
print(features)
print(features[0])

# 6. Tuples
image_shape = (224, 224, 3)
height, width, channels = image_shape
print(height, width, channels)

# 7. Sets
labels = {"cat", "dog", "cat"}
print(len(labels))  # 2; set display order is not guaranteed

# 8. Dictionaries
metrics = {"accuracy": 0.92, "recall": 0.88}
print(metrics.get("precision", 0.0))
metrics["precision"] = 0.90
print(metrics)

# 9. Conditions
score = 0.83
if score >= 0.90:
    category = "excellent"
elif score >= 0.75:
    category = "good"
else:
    category = "needs review"
print(category)

# 10. Loops
for index, feature in enumerate(features):
    print(index, feature)

# 11. Comprehension
confidence_scores = [0.92, 0.45, 0.87, 0.31, 0.96]
high_confidence = [score for score in confidence_scores if score >= 0.80]
print(high_confidence)

# 12. Dataset summary challenge
average_score = sum(confidence_scores) / len(confidence_scores)
print("Count:", len(confidence_scores))
print("High confidence:", high_confidence)
print("Average:", round(average_score, 3))
