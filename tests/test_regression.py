
# POSITRON LABORATORY 01
# Automated Regression Validation Tests

import csv
from pathlib import Path

import numpy as np
import pytest

PROJECT = Path(__file__).resolve().parents[1]
TOLERANCE = 1e-10


@pytest.fixture
def regression_results():
    with (PROJECT / "mtcars.csv").open(
        newline="", encoding="utf-8-sig"
    ) as file:
        rows = list(csv.DictReader(file))

    weight = np.array(
        [float(row["wt"]) for row in rows]
    )
    mpg = np.array(
        [float(row["mpg"]) for row in rows]
    )

    X = np.column_stack(
        (np.ones(len(weight)), weight)
    )

    coefficients = np.linalg.lstsq(
        X, mpg, rcond=None
    )[0]

    predicted = X @ coefficients

    rss = np.sum((mpg - predicted) ** 2)
    tss = np.sum((mpg - mpg.mean()) ** 2)

    return {
        "observations": len(rows),
        "intercept": float(coefficients[0]),
        "slope": float(coefficients[1]),
        "r_squared": float(1 - rss / tss),
    }


@pytest.fixture
def r_reference():
    with (PROJECT / "r_reference.csv").open(
        newline="", encoding="utf-8-sig"
    ) as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 3
    metrics = [row["metric"] for row in rows]
    assert len(set(metrics)) == 3

    return {
        row["metric"]: float(row["value"])
        for row in rows
    }


def test_observation_count(regression_results):
    assert regression_results["observations"] == 32


def test_expected_metrics(r_reference):
    assert set(r_reference) == {
        "intercept",
        "slope",
        "r_squared",
    }


@pytest.mark.parametrize(
    "metric",
    ["intercept", "slope", "r_squared"]
)
def test_cross_language_agreement(
    regression_results, r_reference, metric
):
    actual = regression_results[metric]
    expected = r_reference[metric]

    assert np.isfinite(actual)
    assert np.isfinite(expected)
    assert abs(actual - expected) <= TOLERANCE


def test_negative_weight_relationship(regression_results):
    assert regression_results["slope"] < 0


def test_r_squared_range(regression_results):
    assert 0 <= regression_results["r_squared"] <= 1
