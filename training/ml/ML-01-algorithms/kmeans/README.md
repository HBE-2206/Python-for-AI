# ML-01.1 — K-Means Clustering

**Track:** Machine Learning  
**Author:** Hazem Elshafey | HBE_2206  
**Status:** Practical learning module — notebook execution pending

## Learning objectives

By the end of this module, you should be able to:
- Explain why K-Means is an unsupervised learning algorithm.
- Describe centroids, cluster assignment, and the iterative update process.
- Explain the Within-Cluster Sum of Squares (WCSS) objective.
- Use Euclidean distance to understand nearest-centroid assignment.
- Configure the main scikit-learn KMeans parameters.
- Interpret inertia and silhouette score with appropriate limitations.
- Identify when K-Means is and is not a suitable choice.

## 1. What is K-Means Clustering?

K-Means is an unsupervised machine-learning algorithm used for clustering. It groups similar data points into K clusters based on feature similarity.

The algorithm aims to minimize the distance between data points and their respective cluster centroids. Each point is assigned to the cluster with the nearest centroid.

## 2. How K-Means works

1. Choose the number of clusters, K.
2. Initialize K centroids.
3. Assign each data point to the nearest centroid.
4. Recalculate each centroid as the mean of all points assigned to that cluster.
5. Repeat assignment and centroid recalculation until the centroids stop changing, assignments stabilize, or the maximum iteration count is reached.

### Process diagram

`Choose K → Initialize centroids → Assign points → Recalculate centroids → Check convergence → Final clusters`

## 3. Objective function

K-Means minimizes the Within-Cluster Sum of Squares (WCSS), also called inertia in scikit-learn:

`J = Σ(i=1 to K) Σ(x ∈ Cᵢ) ||x − μᵢ||²`

Where:
- K: number of clusters.
- Cᵢ: set of points in cluster i.
- x: one data point.
- μᵢ: centroid of cluster i.
- The squared Euclidean distance measures the point's squared distance from its assigned centroid.

A smaller inertia means points are closer to their assigned centroids. Inertia normally decreases as K increases, so it should not be used alone to choose K.

## 4. Distance metric

K-Means commonly uses Euclidean distance:

`d(x, μ) = √(Σ(j=1 to n) (xⱼ − μⱼ)²)`

Features with larger numeric scales can dominate this distance. Standardize or otherwise scale features when their units and ranges make distances incomparable.

## 5. Important parameters in scikit-learn

| Parameter | Meaning | Common default |
|---|---|---|
| `n_clusters` | Number of clusters K | 8 |
| `init` | Centroid initialization strategy | `'k-means++'` |
| `n_init` | Number of initializations with different centroid seeds | `'auto'` in current scikit-learn |
| `max_iter` | Maximum iterations for one run | 300 |
| `random_state` | Controls randomness for reproducibility | `None` |

Defaults can vary by scikit-learn version. Set parameters explicitly in learning experiments when reproducibility matters.

## 6. Advantages and disadvantages

| Advantages | Disadvantages |
|---|---|
| Simple and easy to implement | Must choose K in advance |
| Can work efficiently on large datasets | Sensitive to initialization |
| Computationally efficient for many datasets | Can be affected by outliers |
| Works well for compact, well-separated, roughly spherical clusters | May perform poorly for non-spherical or varying-density clusters |
| Centroids are easy to inspect | Distance-based results are sensitive to feature scaling |

## 7. Use cases

- Customer segmentation.
- Image compression / color quantization.
- Document clustering.
- Grouping similar products.
- Exploratory market analysis.
- Anomaly detection as a possible preprocessing or exploratory step; K-Means itself is not a dedicated anomaly detector.

## 8. Choosing K

### Elbow method
Fit K-Means for several K values and plot inertia. Look for a bend where adding more clusters gives diminishing improvement. The elbow can be subjective and may not be clear.

### Silhouette score
The silhouette score compares how close a point is to its own cluster versus other clusters. It ranges from -1 to 1; higher values generally indicate better-separated clusters. It is not a universal measure of business usefulness.

Use both quantitative scores and domain understanding. Do not select K based only on a single plot.

## 9. Practical workflow

1. Select relevant numeric features.
2. Inspect missing values and data quality.
3. Scale features where appropriate.
4. Fit K-Means for a range of K values.
5. Compare inertia and silhouette score.
6. Inspect cluster sizes and feature profiles.
7. Visualize clusters when possible.
8. Describe what the clusters mean in the application context.
9. Record limitations and sensitivity to initialization.

## 10. Quality and source note

This module follows the concepts visible in the supplied handwritten K-Means reference page: definition, iterative steps, WCSS objective, Euclidean distance, key parameters, advantages/disadvantages, and use cases. The elbow method, silhouette score, scaling workflow, and practical notebook are additional learning context added to make the topic actionable.

The accompanying notebook is a draft. Run all cells top-to-bottom in Colab or Jupyter before treating its outputs as validated.
