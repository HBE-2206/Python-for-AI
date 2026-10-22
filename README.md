# HAZEM ELSHAFEY | Python for AI

<p align="center">
  <strong>A practical, notebook-first learning path from Python fundamentals to AI-ready data skills.</strong><br/>
  Learn a concept → inspect the code → predict the output → run it → practice → build something.
</p>

<p align="center">
  <a href="#learning-roadmap">Roadmap</a> •
  <a href="#quick-start">Quick start</a> •
  <a href="#repository-map">Repository map</a> •
  <a href="#how-to-study">How to study</a>
</p>

---

## Welcome

This repository is a structured learning resource by **Hazem Elshafey**. It brings together detailed Jupyter notebooks, runnable Python examples, practice exercises, reference solutions, and learning guides. The goal is not only to read Python, but to understand it and apply it to data analysis and Artificial Intelligence.

> **Learning principle:** every topic should connect explanation, working code, expected output, practice, and an application.

## Learning roadmap

| Stage | Focus | Status / next step |
|---|---|---|
| **Part 1 — Core Python** | Syntax, variables, data types, operators, strings, collections, conditions, loops | Study notes and practice materials available |
| **Part 2 — Professional Python** | Functions, comprehensions, exceptions, files, JSON, OOP, modules, testing, environments | Study notebook, exercises, and mini-project available |
| **Part 3A — NumPy** | Arrays, shapes, indexing, vectorized operations, statistics, random values | Library notebook available |
| **Part 3B — Pandas** | Series/DataFrames, loading data, filtering, cleaning, missing values, grouping, merging | Library notebook available |
| **Part 3C — Matplotlib** | Choosing charts, labels, legends, subplots, saving figures, plotting tabular data | **Current library topic** |
| **Next — Machine Learning foundations** | Preparing features and labels, splitting data, baselines, model evaluation | Follow after the library sequence |

The library order is intentional: **NumPy → Pandas → Matplotlib**. Together, they prepare you to manipulate, inspect, and communicate data before moving into Machine Learning.

## Quick start

### 1. Get the repository

```bash
git clone https://github.com/HBE-2206/Python-for-AI.git
cd Python-for-AI
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install learning dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Open the notebooks

```bash
jupyter notebook
```

You can also upload a notebook to **Google Colab**. Run cells from top to bottom, and restart the kernel and run all cells if results become inconsistent.

## Repository map

```text
Python-for-AI/
├── README.md
├── requirements.txt
├── CONTRIBUTING.md
├── code/
│   ├── Python_Part1_Study_Notes.ipynb
│   ├── Python_Part1_Practice.ipynb
│   ├── python_part1_examples.py
│   ├── Python_Part2_Study_Notes.ipynb
│   └── python_part2_examples.py
├── exercises/
│   ├── README.md
│   ├── solutions.py
│   └── part2_exercises.md
├── part-1/
│   ├── README.md
│   ├── Python_Part1_Study_Notes.ipynb
│   └── Python_Part1_Practice.ipynb
├── part-2/
│   ├── README.md
│   ├── Python_Part2_Study_Notes.ipynb
│   └── solutions.py
├── libraries/
│   ├── README.md
│   ├── numpy/NumPy_for_AI_Study_Notes.ipynb
│   ├── pandas/Pandas_for_AI_Study_Notes.ipynb
│   └── matplotlib/Matplotlib_for_AI_Study_Notes.ipynb
├── docs/
│   └── LEARNING_PATH.md
└── slides/
    ├── DESIGN_GUIDE.md
    └── slide upload notes
```

## Start learning

### Python foundations
- [Part 1 folder and guide](part-1/README.md)
- [Part 1 study notes](part-1/Python_Part1_Study_Notes.ipynb)
- [Part 1 practice notebook](part-1/Python_Part1_Practice.ipynb)
- [Part 1 runnable examples](code/python_part1_examples.py)

### Professional Python
- [Part 2 detailed notebook](part-2/Python_Part2_Study_Notes.ipynb)
- [Part 2 runnable examples](code/python_part2_examples.py)
- [Part 2 guide](part-2/README.md)
- [Part 2 exercises](exercises/part2_exercises.md)
- [Reference solutions](part-2/solutions.py)

### Python libraries for AI
- [Library learning hub and current topic](libraries/README.md)
- [NumPy — detailed notebook](libraries/numpy/NumPy_for_AI_Study_Notes.ipynb)
- [Pandas — detailed notebook](libraries/pandas/Pandas_for_AI_Study_Notes.ipynb)
- [Matplotlib — detailed notebook](libraries/matplotlib/Matplotlib_for_AI_Study_Notes.ipynb)

## How to study

1. Read the learning objectives and concept explanation.
2. Predict what the code will do before running it.
3. Run the code cell and compare the actual output with the expected result.
4. Change one value or parameter and observe what changes.
5. Solve the exercises without opening the solutions first.
6. Complete the mini-project or practical task.
7. Write down errors you encountered and how you fixed them.

## Quality and scope

- Notebooks are the detailed technical learning material; the slide/post identity belongs in the presentation assets, not as notebook decoration.
- Code examples should be small, readable, and accompanied by explanations and expected outputs where useful.
- Dataset examples should use reproducible, clearly described data or document where a file must be supplied.
- A file being present does not automatically mean every cell has been executed in every environment. Run notebooks from top to bottom to validate local results.
- Slides/PDFs are only available in the repository when the actual exported files have been uploaded; a note about pending uploads is not the slide file itself.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions used to add or improve lessons, notebooks, exercises, and projects.

## Author

**Hazem Elshafey**  
- GitHub: [HBE-2206](https://github.com/HBE-2206)
- LinkedIn: [Hazem Elshafey](https://www.linkedin.com/in/hazem-el-shafey-b56405331/)
- Email: [hm2502630@gmail.com](mailto:hm2502630@gmail.com)
- WhatsApp: [Contact on WhatsApp](https://wa.me/201552694877)

---

<p align="center"><sub>HBE_2206 • Python Learning Series • Learn by understanding, practice, and application.</sub></p>
