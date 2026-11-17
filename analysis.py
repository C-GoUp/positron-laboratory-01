# POSITRON LABORATORY 01
# Python Cross-Language Regression Validation

import csv
from pathlib import Path

import numpy as np

# 1. Locate the shared R-exported dataset
data_path = Path(__file__).resolve().parent / "mtcars.csv"

# 2. Read the observations
with data_path.open(newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

weight = np.array([float(row["wt"]) for row in rows])
mpg = np.array([float(row["mpg"]) for row in rows])

# 3. Fit ordinary least squares
X = np.column_stack((np.ones(len(weight)), weight))
coefficients = np.linalg.lstsq(X, mpg, rcond=None)[0]

intercept, slope = coefficients

# 4. Calculate R-squared
predicted = X @ coefficients
rss = np.sum((mpg - predicted) ** 2)
tss = np.sum((mpg - mpg.mean()) ** 2)
r_squared = 1 - rss / tss

# 5. Compare against verified R results
assert len(rows) == 32
assert np.isclose(intercept, 37.2851, atol=0.0001)
assert np.isclose(slope, -5.3445, atol=0.0001)
assert np.isclose(r_squared, 0.7528, atol=0.0001)

# 6. Report results
print("Python regression validation")
print("----------------------------")
print(f"Observations: {len(rows)}")
print(f"Intercept: {intercept:.4f}")
print(f"Weight coefficient: {slope:.4f}")
print(f"R-squared: {r_squared:.4f}")
print("Cross-language validation: PASSED")


# ============================================================
# 7. Full-Precision Cross-Language Validation
# ============================================================

# Locate the R reference file
reference_path = Path(__file__).resolve().parent / "r_reference.csv"

# Read the exported R statistics
with reference_path.open(
    newline="", encoding="utf-8-sig"
) as file:
    reference_rows = list(csv.DictReader(file))

r_reference = {
    row["metric"]: float(row["value"])
    for row in reference_rows
}

# Independently calculated Python statistics
python_results = {
    "intercept": float(intercept),
    "slope": float(slope),
    "r_squared": float(r_squared)
}

# Define numerical tolerance
tolerance = 1e-10

# Validate all three statistics
assert len(reference_rows) == 3
assert set(r_reference) == set(python_results)

print("\nFull-Precision Cross-Language Validation")
print("-" * 45)

for metric, python_value in python_results.items():
    r_value = r_reference[metric]
    difference = abs(python_value - r_value)

    passed = np.isfinite(difference) and difference <= tolerance

    print(f"\nMetric: {metric}")
    print(f"R result:      {r_value:.17g}")
    print(f"Python result: {python_value:.17g}")
    print(f"Difference:    {difference:.12e}")
    print(f"Status:        {'PASS' if passed else 'FAIL'}")

    assert passed, f"Validation failed for {metric}"

print("\nFull-precision validation: PASSED")

