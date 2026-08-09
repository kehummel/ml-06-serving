"""

A FastAPI service that loads
a trained penguin species classifier
and exposes a /predict endpoint.

Author: Kim Hummel, Denise Case
Date: 2026-06

Process:
    - Load a saved model from artifacts/.
    - Accept a POST request with penguin measurements.
    - Return the predicted species.

Data Source:
    - artifacts/model2.joblib (trained in the notebook or app_case.py)

Terminal commands to run this service from the root project folder:

uv run fastapi dev project06/serve_project06.py      # development (auto-reload)
uv run fastapi run project06/serve_project06.py      # production

- OR -

uv run uvicorn project06.serve_project06:app --reload    # development (auto-reload)
uv run uvicorn project06.serve_project06:app             # production

Then send a request - open a new terminal and run

If macOS or Linux, use \\ line continuation characters:

    curl -X POST http://127.0.0.1:8000/predict \
         -H "Content-Type: application/json" \
         -d '{"glucose": 117, "BMI": 32, "age": 29}'

If Windows (PowerShell), use ` instead of \\ for line continuation:

    curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 117, "BMI": 32, "age": 29}'
OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy if you want to experiment.
  Include your command to run it in the docstring and in README.md.
"""

# === Section 1. IMPORTS ===

import logging
from pathlib import Path
from typing import Any, Final

from datafun_toolkit.logger import get_logger, log_header
from fastapi import FastAPI, HTTPException
import joblib  # for serializing and deserializing the model
from sklearn.ensemble import RandomForestClassifier

__all__ = ["app", "predict_from_features", "predict"]

# === Section 2. CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("M06", level="DEBUG")
log_header(LOG, "M06")

# === Section 3. CONSTANTS AND CONFIGURATION ===

# The path to the saved model artifact.
MODEL_PATH: Final[Path] = Path("artifacts") / "model2.joblib"

# The feature columns the model was trained on.
# These must match exactly what was used during training.
FEATURE_COLS: Final[list[str]] = [
    "glucose",
    "BMI",
    "age",
]

# === Section 4. LOAD THE MODEL ===

LOG.info(f"Loading model from: {MODEL_PATH}")

if not MODEL_PATH.exists():
    LOG.error(f"Model file not found: {MODEL_PATH}")
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Run model_builder_project06.py first."
    )

MODEL = joblib.load(MODEL_PATH)
LOG.info("Model loaded successfully")

# === Section 5. CREATE THE APP ===

app = FastAPI(title="Diabetes Classifier")

# === Section 6. DEFINE THE PREDICT ENDPOINT ===


def predict_from_features(
    model: RandomForestClassifier, payload: dict[str, Any]
) -> dict[str, Any]:
    """Pure prediction function - testable outside the web framework."""
    try:
        features = [float(payload[c]) for c in FEATURE_COLS]
    except KeyError as exc:
        raise ValueError(f"Missing required feature: {exc}") from exc
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid feature value: {exc}") from exc

    label: str = str(model.predict([features])[0])

    proba = model.predict_proba([features])[0]
    probability: dict[str, float] = dict(
        zip(model.classes_, proba.tolist(), strict=False)
    )

    warnings: list[str] = []

    glucose_value = features[FEATURE_COLS.index("glucose")]
    if glucose_value < 70:
        LOG.warning("At risk for hypoglycemia")
        warnings.append("At risk for hypoglycimeia")

    BMI_value = features[FEATURE_COLS.index("BMI")]
    if BMI_value < 18:
        LOG.warning("Extremely low BMI")
        warnings.append("Extremely low BMI")
    elif BMI_value > 40:
        LOG.warning("Extremely high BMI")
        warnings.append("Extrememly high BMI")

    return {"prediction": label, "probability": probability, "warnings": warnings}


@app.post("/predict")
def predict(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        return predict_from_features(MODEL, payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
