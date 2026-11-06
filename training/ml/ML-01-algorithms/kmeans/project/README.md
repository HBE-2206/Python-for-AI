# K-Means Mini Project — Customer Segmentation

## Objective
Use K-Means to explore customer groups from a permitted tabular dataset. The goal is to demonstrate a careful clustering workflow, not to claim that a particular number of customer types is objectively correct.

## Dataset
Choose a public dataset with numeric customer features such as annual income, spending score, or purchase behavior. Document:
- Dataset title and source URL.
- License or permitted use.
- Number of rows and selected features.
- Meaning and units of each feature.

Do not upload private customer information.

## Workflow
1. Define the segmentation question.
2. Load and inspect the dataset.
3. Check missing values, duplicates, and feature units.
4. Select meaningful numeric features.
5. Scale features where appropriate.
6. Fit K-Means across several candidate K values.
7. Compare inertia and silhouette score.
8. Inspect cluster sizes and feature summaries.
9. Visualize clusters (PCA may be used for a 2D view, with a note that projection can distort distances).
10. Translate clusters into cautious, evidence-based descriptions.
11. Document limitations and reproducibility details.

## Deliverables
- Notebook with code, plots, and explanations.
- README with dataset provenance, feature choices, method, results, and limitations.
- Cluster profile table.
- Short recommendation describing whether the segmentation is useful for the stated question.

## Evaluation rubric (100 points)
| Criterion | Points |
|---|---:|
| Dataset understanding and question | 15 |
| Preprocessing and feature scaling rationale | 20 |
| Correct K-Means implementation | 20 |
| K selection and evaluation discussion | 20 |
| Cluster interpretation and limitations | 15 |
| Reproducibility and documentation | 10 |

## Completion checklist
- [ ] Data source and license recorded.
- [ ] Features and units explained.
- [ ] Scaling decision justified.
- [ ] Multiple K values compared.
- [ ] Inertia and silhouette interpreted cautiously.
- [ ] Cluster profiles created.
- [ ] Limitations documented.
- [ ] Notebook runs top-to-bottom.
