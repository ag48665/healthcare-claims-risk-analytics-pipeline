# healthcare-claims-risk-analytics-pipeline

End-to-end healthcare claims and risk analytics pipeline using SQL, Python, SQLite, Docker, and automated reporting for healthcare KPI monitoring, anomaly detection, and predictive analytics.

---

# How to Run the Pipeline

```bash
pip install -r requirements.txt
python src/run_pipeline.py
```

---

# Docker

```bash
docker build -t healthcare-claims-risk-pipeline .
docker run healthcare-claims-risk-pipeline
```

---

# Pipeline Steps

1. Generate synthetic healthcare claims data  
2. Create SQLite database  
3. Run data quality checks  
4. Run healthcare claims analytics  
5. Generate automated HTML report  

---

# Outputs

The pipeline generates:

- `data/patients.csv`
- `data/claims.csv`
- `database/healthcare_claims.db`
- `outputs/data_quality_report.csv`
- `outputs/hospital_kpis.csv`
- `outputs/high_risk_patients.csv`
- `outputs/cost_by_diagnosis.csv`
- `reports/healthcare_risk_report.html`

---
