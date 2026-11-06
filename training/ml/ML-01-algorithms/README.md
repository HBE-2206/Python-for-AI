# ML-01 — Machine Learning Algorithms & Practical Foundations

**Track:** Machine Learning  
**Author:** Hazem Elshafey | HBE_2206  
**Status:** Learning module draft — notebook execution and review pending

> This module organizes the handwritten Machine Learning notes into a practical study guide. It follows the topics in the supplied 20-page reference: fundamentals, data preparation, EDA, algorithms, projects, current directions, and interview preparation. Explanations below preserve that scope while adding practical learning structure.

## Learning outcomes

By the end, you should be able to:
- Explain what ML is and distinguish supervised, unsupervised, reinforcement, and semi-supervised learning.
- Identify data sources, formats, features, targets, and common preprocessing needs.
- Perform basic EDA and interpret summary statistics and visualizations.
- Select a baseline algorithm for regression, classification, or clustering.
- Explain Linear/Logistic Regression, Decision Trees, Random Forest, SVM, KNN, and K-Means at a practical level.
- Evaluate models with task-appropriate metrics and recognize common limitations.
- Organize an end-to-end project and explain it in an interview.

## Contents

| Section | Topics |
|---|---|
| 1. ML foundations | Definition, workflow, applications, problem types |
| 2. Learning paradigms | Supervised, unsupervised, reinforcement, semi-supervised |
| 3. Data collection | Sources, structured/unstructured/semi-structured, common formats |
| 4. Data preprocessing | Missing values, duplicates, outliers, categorical encoding |
| 5. EDA | Summary statistics, univariate, bivariate, multivariate analysis |
| 6. Algorithm overview | Regression, classification, clustering and choosing an algorithm |
| 7. Regression | Linear, multiple linear, polynomial, Ridge, Lasso, Elastic Net, SVR, tree ensembles |
| 8. Classification | Logistic Regression, Decision Tree, Random Forest, SVM, KNN, Naive Bayes |
| 9. Clustering | K-Means, hierarchical clustering, DBSCAN, Gaussian Mixture Models |
| 10. Model evaluation | MAE, MSE, RMSE, R², accuracy, precision, recall, F1, confusion matrix, silhouette |
| 11. End-to-end projects | Problem statement → data → preparation → training → evaluation → deployment → monitoring |
| 12. Current directions | LLMs, multimodal models, PEFT/LoRA, quantization, pruning, distillation, RAG, agents |
| 13. Interview preparation | DSA, ML concepts, project explanations, system design, behavioral questions |

## 1. What is Machine Learning?

Machine Learning is a subset of Artificial Intelligence that enables systems to learn patterns from data and use those patterns to make predictions or decisions, rather than relying only on explicitly written rules.

A simplified workflow:

`Input data → learning algorithm → learned patterns/model → prediction or decision`

Examples include spam detection, house-price prediction, image recognition, and recommendation systems.

### Main problem types

- **Classification:** predict a category, such as spam / not spam.
- **Regression:** predict a continuous numerical value, such as a house price.
- **Clustering:** group similar observations without known labels.
- **Anomaly detection:** identify unusual observations that differ from normal patterns.

## 2. Types of Machine Learning

| Type | Data / feedback | Typical use |
|---|---|---|
| Supervised | Labeled input-output examples | Classification and regression |
| Unsupervised | Unlabeled input data | Clustering and dimensionality reduction |
| Reinforcement | Agent interacts with an environment and receives rewards/penalties | Robotics and game-playing |
| Semi-supervised | A small labeled set plus a larger unlabeled set | Learning when labels are expensive |

## 3. Data Collection and Understanding

### Sources
- Internal databases and application data.
- External public datasets, APIs, and websites.
- Manual collection through surveys, forms, and sensors.
- Open datasets such as Kaggle, UCI, and government portals.

### Data forms
- **Structured:** rows and columns.
- **Unstructured:** text, images, audio, and video.
- **Semi-structured:** JSON, XML, and logs.
- **Labeled / unlabeled:** whether a target/output label is available.

### Common formats
CSV, Excel, JSON, SQL tables, and Parquet. Choose formats based on data size, workflow, and storage needs.

Before modeling, inspect shape, data types, missing values, feature meanings, basic statistics, and unusual values.

## 4. Data Preprocessing

A common sequence is:

`Raw data → cleaning → transformation → feature engineering → model-ready data`

### Missing values
Possible approaches include removing rows/columns when justified, imputing with mean/median/mode, using a constant, or forward/backward filling for appropriate ordered data. The choice depends on why values are missing and the feature's meaning.

### Duplicates
Check whether repeated records are genuine or accidental before removing them. In pandas, `drop_duplicates()` can remove duplicate rows.

### Outliers
Inspect extreme values with plots such as boxplots. Depending on context, investigate, retain, cap, transform, or use robust methods. Do not remove an outlier automatically: it may be a valid and important event.

### Categorical encoding
- Label/ordinal encoding when categories have a meaningful order or when appropriate for the model.
- One-hot encoding for nominal categories without a natural order.

### Scaling
Scaling is important for distance- and margin-based algorithms such as KNN and SVM. Tree-based models generally do not require feature scaling.

## 5. Exploratory Data Analysis (EDA)

EDA helps understand structure, distributions, relationships, patterns, and possible data-quality issues before modeling.

### Summary statistics
Count, mean, median, standard deviation, minimum, maximum, and percentiles.

### Analysis levels
- **Univariate:** one feature; histogram, boxplot, KDE.
- **Bivariate:** relationship between two variables; scatter, line, or suitable bar plots.
- **Multivariate:** several variables together; pair plots and correlation heatmaps.

EDA should help identify missingness, skew, outliers, relationships, candidate features, and questions that need further investigation. Correlation alone does not establish causation.

## 6. Algorithm map

| Task | Algorithms to learn |
|---|---|
| Regression | Linear Regression, Polynomial Regression, Ridge, Lasso, Elastic Net, SVR, Decision Tree / Random Forest Regressor, Gradient Boosting |
| Classification | Logistic Regression, Decision Tree, Random Forest, SVM, KNN, Naive Bayes, Gradient Boosting, Neural Networks |
| Clustering | K-Means, Hierarchical, DBSCAN, Gaussian Mixture Model, Mean Shift, Spectral Clustering |

Choose an algorithm based on the target type, dataset size, feature properties, interpretability needs, validation results, and deployment constraints—not from a fixed popularity ranking.

## 7. Regression

Regression predicts a continuous numerical target.

### Linear Regression
Models a linear relationship between features and a target. For one feature:

`y = mx + b`

For multiple features:

`y = β₀ + β₁x₁ + β₂x₂ + … + βₙxₙ`

Parameters can be estimated analytically or with optimization methods such as gradient descent. Evaluate residuals and use a baseline.

### Polynomial Regression
Adds polynomial feature terms to represent curved relationships. Higher degree increases flexibility and can overfit.

### Regularization
- **Ridge (L2):** penalizes large coefficients.
- **Lasso (L1):** can shrink some coefficients to zero.
- **Elastic Net:** combines L1 and L2 penalties.

### Other regression families
Support Vector Regression, Decision Tree Regression, Random Forest Regression, and Gradient Boosting Regression.

### Regression metrics
- MAE: average absolute error.
- MSE: average squared error; larger errors receive more weight.
- RMSE: square root of MSE, in the target's units.
- R²: relative goodness-of-fit measure; interpret in context and do not treat it as a complete measure of model quality.

## 8. Classification

Classification predicts a categorical class.

### Logistic Regression
Uses a sigmoid function to estimate a probability:

`σ(z) = 1 / (1 + e⁻ᶻ)`

A decision threshold converts probabilities into predicted classes. The default threshold of 0.5 is not always optimal; choose it based on the application and error costs.

### Decision Tree
Splits data using feature-based rules. Classification splits can use criteria such as Gini impurity or entropy / information gain. Trees are interpretable but can overfit if not controlled.

### Random Forest
Trains multiple decision trees using randomized samples and feature subsets, then aggregates their predictions. Classification commonly uses voting; regression commonly averages predictions.

### Support Vector Machine (SVM)
Finds a separating boundary with a large margin. Kernel functions can model non-linear boundaries. Important parameters include C, kernel, and gamma. Scaling is usually important.

### K-Nearest Neighbors (KNN)
Predicts from the labels or target values of nearby training examples. Key choices include K, distance metric, and feature scaling. It can be expensive at prediction time for large datasets.

### Naive Bayes
Uses Bayes' theorem with a conditional-independence assumption. It is often useful as a fast baseline, especially for some text-classification tasks.

### Classification metrics
- Accuracy: overall fraction correct.
- Precision: among predicted positives, how many are positive?
- Recall: among actual positives, how many were found?
- F1: harmonic mean of precision and recall.
- Confusion matrix: counts of true/false positives and negatives.

For imbalanced data, accuracy alone can be misleading.

## 9. Clustering

Clustering groups similar observations without labeled target values.

### K-Means

K-Means partitions observations into K clusters. Each observation is assigned to the nearest centroid, then centroids are recalculated until assignments/centroids stabilize or the iteration limit is reached.

Objective: minimize within-cluster sum of squares (WCSS).

Important parameters in scikit-learn:
- `n_clusters`: number of clusters.
- `init`: centroid initialization strategy.
- `n_init`: number of initializations.
- `max_iter`: maximum iterations.
- `random_state`: reproducibility.

Strengths: simple, efficient, and useful for compact, roughly spherical clusters. Limitations: requires K, is sensitive to initialization and outliers, and may perform poorly for irregularly shaped clusters.

### Other clustering algorithms
- **Hierarchical:** creates a hierarchy of clusters; agglomerative merges and divisive splits.
- **DBSCAN:** density-based; can identify noise and irregular cluster shapes. Key parameters: `eps` and `min_samples`.
- **Gaussian Mixture Model:** probabilistic/soft cluster assignments using a mixture of distributions.

### Evaluation
Silhouette score, Davies–Bouldin index, Calinski–Harabasz index, and the elbow method can help assess clustering, but use domain knowledge too. Internal scores do not prove that clusters are useful.

## 10. End-to-End ML Projects

A project workflow:

1. Define the problem and success criteria.
2. Collect data.
3. Prepare and inspect the data.
4. Train a baseline and candidate models.
5. Evaluate and tune using validation data.
6. Deploy through an API or application when appropriate.
7. Monitor behavior and improve the system.

Project ideas from the reference:
- Image classification.
- Object detection.
- Sentiment analysis.
- Document Q&A / RAG.
- Domain-specific chatbot using an LLM.

A useful repository structure:

```text
project/
├── data/
├── notebooks/
├── src/
├── models/
├── app/
├── requirements.txt
└── README.md
```

Document the problem, data source, setup, methodology, metrics, limitations, and results. Do not commit private or restricted datasets, credentials, or large model files.

## 11. Current Directions in AI

The reference highlights:
- Large Language Models (LLMs).
- Multimodal models combining text, images, audio, and video.
- Parameter-Efficient Fine-Tuning (PEFT), including LoRA and adapters.
- Quantization, pruning, and distillation for model efficiency.
- Retrieval-Augmented Generation (RAG).
- Agentic AI systems that plan, use tools, and take actions.
- Smaller efficient models and multimodal RAG.

These are evolving areas. Treat named model examples and tooling as time-sensitive rather than permanent recommendations.

## 12. Interview Preparation

Focus areas:
- Programming and DSA: arrays, strings, linked lists, stacks, queues, hashing, trees, graphs, dynamic programming, heaps.
- ML: problem types, algorithms, evaluation, tuning, RAG, and LLM basics.
- System design: scalability, caching, messaging, databases, availability.
- Projects: explain the problem, decisions, trade-offs, results, and lessons.
- Behavioral: communicate a challenge, your contribution, and what changed.

Preparation loop: revise concepts → practice problems → build end-to-end projects → explain design decisions → do mock interviews.

## Recommended study order

1. Review ML-00 fundamentals and workflow.
2. Data collection, preprocessing, and EDA.
3. Regression and its metrics.
4. Classification and its metrics.
5. K-Means and other clustering methods.
6. Compare algorithms on a shared dataset.
7. Build and document an end-to-end project.
8. Explore LLM/RAG/agent topics after core ML foundations.

## Quality checklist

- [ ] Explain each concept without reading the notes.
- [ ] Run every notebook from top to bottom.
- [ ] Compare at least one simple baseline with a more capable model.
- [ ] Use validation data for model selection and keep test data for final evaluation.
- [ ] Explain the selected metric and its limitations.
- [ ] Document project setup, results, and limitations.

**Important:** This guide is a structured learning draft based on the supplied reference pages. Practical code, expected outputs, and notebook execution checks are being added separately; do not consider the module fully validated until those checks are complete.
