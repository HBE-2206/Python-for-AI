# HBE_2206 — AI Engineering Learning Roadmap

**Owner:** Hazem Elshafey  
**Repository:** [Python-for-AI](https://github.com/HBE-2206/Python-for-AI)

This is the agreed learning sequence. It is a curriculum map, not a claim that every topic has been mastered or every notebook has been executed.

## Stage 1 — Python & Data Foundations

1. [Core Python — Part 1](../part-1/README.md)
2. [Professional Python — Part 2](../part-2/README.md)
3. [NumPy](../libraries/numpy/NumPy_for_AI_Study_Notes.ipynb)
4. [Pandas](../libraries/pandas/Pandas_for_AI_Study_Notes.ipynb)
5. [Data Visualization](training/python-for-ai/visualization/README.md)

## Stage 2 — Mathematics & Machine Learning

1. [Math & Statistics for ML](training/ml/math-statistics/README.md)
2. [ML Fundamentals & Workflow](training/ml/ML-00-fundamentals/README.md)
3. [Regression](training/ml/regression/README.md)
4. [Classification](training/ml/classification/README.md)
5. [Decision Trees & Ensembles](training/ml/decision-trees-ensembles/README.md)
6. [Clustering](training/ml/clustering/README.md)
7. [ML Algorithms overview](training/ml/ML-01-algorithms/README.md)

## Stage 3 — Deep Learning

1. [Deep Learning Foundations](training/deep-learning/deep-learning/README.md)
2. [Convolutional Neural Networks](training/deep-learning/cnn/README.md)

## Stage 4 — Computer Vision

1. [Computer Vision](training/computer-vision/computer-vision/README.md)
2. Practice path: image classification → object detection → segmentation → video understanding → edge deployment.

## Stage 5 — Sequence Learning & Language

1. [RNN & LSTM](training/deep-learning/rnn-lstm/README.md)
2. [Natural Language Processing](training/nlp/nlp/README.md)

## Stage 6 — Transformers & LLM Engineering

1. [Transformers & LLMs](training/llm/transformers-llms/README.md)
2. Embeddings and semantic search.
3. Retrieval-Augmented Generation (RAG), chunking and source-grounded answers.
4. Tool calling and agent workflows.
5. Evaluation, safety, privacy, latency, cost and deployment.

## Study loop for every module

- Read the guide.
- Run the notebook from top to bottom in a fresh runtime.
- Complete the exercises.
- Build the project.
- Document the result, setup, data provenance, metrics and limitations.
- Add a short reflection on what to improve next.

## Readiness gates

| Gate | Evidence required |
|---|---|
| Foundations | Comfortable Python, NumPy, Pandas and plotting |
| ML | Can build baselines, avoid leakage, choose metrics and explain errors |
| Deep Learning | Can train and debug a PyTorch model |
| Computer Vision | Can prepare images, evaluate detection/classification and analyze failures |
| NLP/LLMs | Can prepare text, explain transformer basics and evaluate model outputs |
| AI Engineering | Can build a reproducible, tested, documented application with responsible data handling |

## Status policy

- **Added:** files exist in the repository.
- **Notebook starter:** introductory code is included.
- **Run-verified:** only use this label after executing all cells in a clean runtime.
- **Project complete:** only use this label after the deliverables and evaluation checklist are met.

At the time of this roadmap update, the newly added topic notebooks are starter labs. Their execution and expected outputs still need clean-runtime verification.