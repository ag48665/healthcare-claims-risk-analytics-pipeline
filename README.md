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

# Technologies Used

- Python
- SQL
- SQLite
- Pandas
- NumPy
- Docker
- GitHub Actions
- Automated Reporting

---

# Key Features

- End-to-end healthcare analytics pipeline
- Automated synthetic healthcare claims generation
- SQLite-based healthcare database
- SQL analytics for hospital KPIs and risk monitoring
- High-risk patient detection
- Readmission risk analysis
- Cost analysis by diagnosis
- Automated HTML reporting
- CI/CD workflow using GitHub Actions
- Dockerized execution environment

---

# SQL Analytics Included

The project demonstrates advanced SQL analytics techniques including:

- Common Table Expressions (CTEs)
- Window Functions
- Ranking Functions
- Aggregations
- CASE WHEN logic
- Risk segmentation
- Healthcare KPI calculations

---

# Example Analytics Questions

- Which patients are at highest readmission risk?
- Which diagnoses generate the highest hospitalization costs?
- What factors are associated with ICU admissions?
- Which patient groups generate the highest claims costs?
- What is the average hospital length of stay?

---

# Automation & DevOps

This project includes:

- Automated pipeline execution
- GitHub Actions CI/CD workflow
- Docker containerization
- Automated HTML report generation
- Reproducible analytics workflow

---

# Future Improvements

Potential future extensions include:

- Machine learning risk prediction models
- Power BI healthcare dashboards
- Cloud deployment on Azure or AWS
- Apache Airflow orchestration
- Real-world healthcare open datasets
- SHAP explainability analysis
- Healthcare anomaly detection models

---

# Author

Agata Gabara

Bioinformatics | Healthcare Analytics | SQL | Python | Machine Learning | Risk Analytics | Analytics Engineering
