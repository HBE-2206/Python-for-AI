# K-Means — Exercises

## Concept questions
1. Why is K-Means considered unsupervised learning?
2. What does K represent?
3. What is a centroid?
4. List the main steps of the K-Means algorithm in order.
5. What condition can stop the iterative process?
6. What does WCSS measure?
7. Why does inertia usually decrease when K increases?
8. Why can features with large numeric ranges dominate Euclidean distance?
9. Explain one advantage and two limitations of K-Means.
10. Give three practical use cases for clustering.

## Parameters
11. What does `n_clusters` control?
12. What is the purpose of `init='k-means++'`?
13. Why might you set `random_state`?
14. What does `max_iter` limit?
15. Why can running multiple initializations help?

## Interpretation
16. An inertia plot decreases smoothly with no obvious elbow. What should you do next?
17. What does a negative silhouette score suggest for a point?
18. Why is a high silhouette score not enough to prove that clusters are useful?
19. Why might K-Means struggle with two crescent-shaped clusters?
20. How can outliers influence centroid positions?

## Practical tasks
- [ ] Run the notebook and inspect the generated synthetic clusters.
- [ ] Fit K-Means for K values from 2 to 8.
- [ ] Plot inertia and silhouette score.
- [ ] Compare results with and without feature scaling on a dataset with differently scaled features.
- [ ] Change `random_state` and compare cluster assignments.
- [ ] Write a short profile for each cluster using original feature units.

## Reflection
Record the chosen K, why you chose it, cluster sizes, feature profiles, one limitation, and one next experiment.
