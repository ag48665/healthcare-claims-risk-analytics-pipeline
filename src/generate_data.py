import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

patients = pd.DataFrame({
    "patient_id": range(1, 11),
    "age": [72, 64, 45, 58, 29, 81, 67, 52, 39, 75],
    "sex": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
    "bmi": [31.2, 28.5, 24.1, 33.8, 22.4, 30.6, 27.9, 35.1, 26.3, 32.4],
    "diabetes": [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    "hypertension": [1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    "chronic_disease": [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
})

claims = pd.DataFrame({
    "claim_id": range(1001, 1011),
    "patient_id": range(1, 11),
    "hospital": [
        "Amsterdam UMC", "Erasmus MC", "UMC Utrecht", "Amsterdam UMC",
        "Leiden UMC", "Erasmus MC", "UMC Utrecht", "Amsterdam UMC",
        "Leiden UMC", "Radboud UMC"
    ],
    "diagnosis": [
        "Heart Failure", "COPD", "Pneumonia", "Diabetes Complication",
        "Minor Infection", "Stroke", "Hypertension Crisis",
        "Respiratory Failure", "Appendicitis", "Heart Failure"
    ],
    "claim_cost": [12500, 7800, 3200, 15200, 2100, 23000, 6900, 16800, 5400, 19700],
    "icu_admission": [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    "length_of_stay": [7, 5, 2, 9, 2, 12, 5, 7, 3, 10],
    "readmitted_30_days": [1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

patients.to_csv(DATA_DIR / "patients.csv", index=False)
claims.to_csv(DATA_DIR / "claims.csv", index=False)

print("Synthetic healthcare claims data generated successfully.")