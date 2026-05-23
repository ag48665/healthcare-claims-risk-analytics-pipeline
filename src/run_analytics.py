import sqlite3
import pandas as pd
from pathlib import Path

# Paths
DB_PATH = Path("database/healthcare_claims.db")
OUTPUT_DIR = Path("outputs")

OUTPUT_DIR.mkdir(exist_ok=True)

# Connect database
conn = sqlite3.connect(DB_PATH)

# Query 1 — Hospital KPIs
hospital_kpis = pd.read_sql_query("""
SELECT
    hospital,
    COUNT(*) AS total_claims,
    ROUND(AVG(claim_cost), 2) AS avg_claim_cost,
    ROUND(AVG(length_of_stay), 2) AS avg_length_of_stay,
    ROUND(AVG(readmitted_30_days) * 100, 2) AS readmission_rate
FROM claims
GROUP BY hospital
ORDER BY avg_claim_cost DESC;
""", conn)

# Query 2 — High-risk patients
high_risk_patients = pd.read_sql_query("""
SELECT
    p.patient_id,
    p.age,
    p.diabetes,
    p.hypertension,
    p.chronic_disease,
    c.claim_cost,
    c.icu_admission,
    c.readmitted_30_days
FROM patients p
JOIN claims c
ON p.patient_id = c.patient_id
WHERE
    c.readmitted_30_days = 1
    AND c.icu_admission = 1
ORDER BY c.claim_cost DESC;
""", conn)

# Query 3 — Cost by diagnosis
cost_by_diagnosis = pd.read_sql_query("""
SELECT
    diagnosis,
    COUNT(*) AS total_cases,
    ROUND(AVG(claim_cost), 2) AS avg_cost
FROM claims
GROUP BY diagnosis
ORDER BY avg_cost DESC;
""", conn)

# Save outputs
hospital_kpis.to_csv(OUTPUT_DIR / "hospital_kpis.csv", index=False)
high_risk_patients.to_csv(OUTPUT_DIR / "high_risk_patients.csv", index=False)
cost_by_diagnosis.to_csv(OUTPUT_DIR / "cost_by_diagnosis.csv", index=False)

print("Healthcare analytics completed successfully.")

print("\nHospital KPIs:")
print(hospital_kpis)

print("\nHigh-risk patients:")
print(high_risk_patients)

print("\nCost by diagnosis:")
print(cost_by_diagnosis)

# Close
conn.close()