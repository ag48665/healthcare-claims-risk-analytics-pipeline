import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

patients = pd.read_csv(DATA_DIR / "patients.csv")
claims = pd.read_csv(DATA_DIR / "claims.csv")

quality_results = {
    "patients_rows": len(patients),
    "claims_rows": len(claims),
    "patients_missing_values": int(patients.isna().sum().sum()),
    "claims_missing_values": int(claims.isna().sum().sum()),
    "duplicate_patient_ids": int(patients["patient_id"].duplicated().sum()),
    "duplicate_claim_ids": int(claims["claim_id"].duplicated().sum()),
    "negative_claim_costs": int((claims["claim_cost"] < 0).sum())
}

quality_df = pd.DataFrame([quality_results])

quality_df.to_csv(OUTPUT_DIR / "data_quality_report.csv", index=False)

print("Data quality checks completed successfully.")
print(quality_df)