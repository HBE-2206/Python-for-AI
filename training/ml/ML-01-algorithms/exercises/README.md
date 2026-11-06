# ML-01 — Exercises

Work through these tasks after studying the matching section in the guide. Write your reasoning before checking documentation or examples.

## A. Foundations
1. Explain Machine Learning in your own words.
2. Classify each task as classification, regression, clustering, or anomaly detection: spam filtering, house-price prediction, customer grouping, unusual transaction detection.
3. Compare supervised and unsupervised learning. Give one example of each.
4. Explain the difference between a feature and a target.

## B. Data and preprocessing
5. List three possible data sources and give one risk for each.
6. A dataset contains missing ages and repeated customer rows. What would you inspect before choosing how to handle them?
7. Explain the difference between one-hot encoding and ordinal encoding.
8. Why can scaling matter for KNN and SVM? Why is it usually less important for a decision tree?
9. What is an outlier? Give two reasons not to delete one automatically.

## C. EDA
10. Which plot would you use to inspect one numerical feature's distribution?
11. Which plot would help inspect the relationship between two numerical features?
12. What does a correlation heatmap show, and what does it not prove?
13. Explain mean, median, standard deviation, and percentile.

## D. Algorithms
14. Choose regression or classification for predicting a delivery time and for predicting whether a delivery will be late. Explain.
15. Explain the role of the sigmoid function in Logistic Regression.
16. What is the difference between a Decision Tree and a Random Forest?
17. Explain support vectors and margin in SVM.
18. Describe the KNN prediction process. What happens when K is very small?
19. Describe the K-Means iteration process.
20. Compare K-Means and DBSCAN in terms of cluster shape, noise, and parameters.

## E. Evaluation and projects
21. Why can accuracy be misleading on imbalanced data?
22. When might recall matter more than precision? Give a real example.
23. Explain MAE versus MSE.
24. Outline an end-to-end project from problem statement to monitoring.
25. Write a README outline for a model project, including data source, setup, evaluation, and limitations.

## Practical tasks
- [ ] Train Linear Regression on a small regression dataset and report MAE, RMSE, and R².
- [ ] Train Logistic Regression and a Decision Tree on a classification dataset; compare precision, recall, F1, and confusion matrices.
- [ ] Scale features and compare KNN performance before and after scaling.
- [ ] Run K-Means for several K values; inspect inertia and silhouette score.
- [ ] Explain one failure mode or limitation for each model.

## Reflection
For each experiment, record: problem type, target, split strategy, preprocessing, baseline, metric choice, result, limitation, and next experiment.
