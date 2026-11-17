
# Positron Laboratory 01
## Reproducible Statistical Analysis with R and Python

### Project Overview

This laboratory investigates the relationship between
vehicle weight and fuel efficiency using the mtcars dataset.

The project demonstrates statistical modeling, data
visualization, cross-language numerical validation,
automated testing, and reproducible scientific reporting.

### Research Question

How does vehicle weight relate to fuel efficiency,
measured in miles per gallon?

### Dataset

- Source: R mtcars dataset
- Observations: 32
- Predictor: wt (vehicle weight in 1,000 pounds)
- Response: mpg (miles per gallon)

### Methodology

Ordinary least squares regression was independently
implemented in R and Python.

Model:

mpg = intercept + slope × wt + error

R was used for statistical analysis and visualization.
Python and NumPy were used for independent numerical
estimation and automated validation.

### Results

| Metric | Result |
|---|---:|
| Intercept | 37.285126 |
| Weight coefficient | -5.344472 |
| R-squared | 0.752833 |

The model explains approximately 75.3% of the observed
variation in fuel efficiency.

This observational relationship does not independently
establish causation.

### Automated Validation

The pytest suite verifies:

- Dataset observation count
- Required reference metrics
- Intercept agreement
- Slope agreement
- R-squared agreement
- Expected negative weight coefficient
- Valid R-squared range

All seven tests passed using a numerical comparison
tolerance of 1e-10.

### Python Setup

Create a virtual environment:

```bash
python3 -m venv .venv
```

Install dependencies:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Run the Python analysis:

```bash
.venv/bin/python analysis.py
```

Run automated tests:

```bash
.venv/bin/python -m pytest -v
```

### R and Quarto

Install R and the required R package ggplot2.

From the R console:

```r
install.packages("ggplot2")
source("analysis.R")
```

The R analysis exports r_reference.csv, which is
used for Python cross-language validation.

Render the scientific report:

```bash
quarto render report.qmd --to html
```

The output is report.html.

### Project Files

- analysis.R: R regression and reference export
- analysis.py: Python regression and validation
- mtcars.csv: Shared analytical dataset
- r_reference.csv: Full-precision R reference
- tests/test_regression.py: Automated pytest suite
- report.qmd: Scientific report source
- report.html: Rendered scientific report
- requirements.txt: Python dependency inventory
- vehicle_analysis.png: Regression visualization

### Reproducibility

The laboratory was validated using R 4.5.1,
NumPy 2.2.6, and pytest 9.2.0.

Python dependencies are recorded in requirements.txt.

### Project Status

Statistical analysis: Complete
Cross-language validation: Passed
Automated tests: 7 passed
Quarto HTML report: Rendered and inspected
GitHub publication: Pending
