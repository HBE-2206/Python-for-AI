# ML-01 — Mini Project: Compare Models on a Real Dataset

## Goal
Build a reproducible machine-learning experiment that demonstrates the complete workflow and compares models fairly.

## Dataset
Choose a public, permitted dataset with a clear target. Suitable options:
- A regression dataset with a numerical target.
- A classification dataset with a categorical target.

Record the dataset name, source URL, license/usage terms, row count, feature descriptions, and target definition. Do not upload private or restricted data.

## Required workflow
1. Define the problem and a measurable success criterion.
2. Load the data and inspect shape, types, missing values, duplicates, and target distribution.
3. Perform EDA and document at least three findings.
4. Split into train and test sets before fitting preprocessing steps.
5. Build a simple baseline.
6. Train at least two suitable algorithms.
7. Use a validation strategy or cross-validation for model selection.
8. Evaluate once on the held-out test set with suitable metrics.
9. Inspect errors and explain at least two limitations.
10. Save the reproducible code and write a clear README.

## Suggested comparisons
- Regression: DummyRegressor vs Linear Regression vs Random Forest Regressor.
- Classification: DummyClassifier vs Logistic Regression vs Decision Tree / Random Forest.
- Clustering extension: K-Means with multiple K values, silhouette score, and a visual inspection where dimensionality permits.

## Deliverables
- Notebook with explanations and outputs.
- Source code or a clean project structure.
- README with problem, data source, setup, methodology, metrics, results, and limitations.
- Short conclusion: what worked, what did not, and what you would try next.

## Evaluation rubric (100 points)
| Criterion | Points |
|---|---:|
| Problem definition and data understanding | 15 |
| Preprocessing and leakage prevention | 20 |
| Baseline and model comparison | 20 |
| Appropriate evaluation and error analysis | 20 |
| Reproducibility and code organization | 15 |
| Documentation and communication | 10 |

## Completion checklist
- [ ] Dataset provenance and license documented.
- [ ] Train/test split is reproducible.
- [ ] Preprocessing is fitted only on training data (prefer a Pipeline).
- [ ] Baseline included.
- [ ] Metrics match the task.
- [ ] Limitations and errors discussed.
- [ ] Notebook runs top-to-bottom in a clean environment.
