# Healthcare Claims Risk Analytics Pipeline

![Healthcare Analytics Pipeline](https://github.com/ag48665/healthcare-claims-risk-analytics-pipeline/actions/workflows/pipeline.yml/badge.svg)

End-to-end healthcare claims and risk analytics pipeline using SQL, Python, SQLite, Docker, and automated reporting for healthcare KPI monitoring, anomaly detection, and predictive analytics.

---

## Project Overview

Healthcare organizations generate large volumes of claims and hospitalization data that can be leveraged for operational monitoring, cost analysis, and patient risk assessment.

This project demonstrates a complete healthcare analytics workflow that integrates data generation, database management, SQL analytics, risk stratification, automated reporting, and DevOps practices into a reproducible analytics pipeline.

The project combines healthcare analytics, data engineering, SQL development, and analytics engineering concepts within a single automated framework.

---

## Project Highlights

✔ End-to-end healthcare analytics pipeline

✔ Synthetic healthcare claims generation

✔ SQL-based risk analytics

✔ High-risk patient identification

✔ Readmission risk monitoring

✔ Healthcare KPI reporting

✔ Automated HTML reporting

✔ Dockerized deployment

✔ GitHub Actions CI/CD

✔ Reproducible analytics workflow

---

## Main Findings

### High-risk patients can be identified using claims patterns

The pipeline automatically flags patients with elevated hospitalization frequency, readmission risk, and healthcare utilization.

### Healthcare costs vary substantially across diagnoses

Cost analysis identifies diagnoses associated with the highest claims expenditure and resource utilization.

### Automated KPI monitoring supports operational reporting

The workflow generates reproducible healthcare KPIs suitable for hospital analytics and management reporting.

### Reproducible analytics pipelines improve scalability

The project demonstrates how SQL, Python, Docker, and CI/CD can be combined into an automated healthcare analytics workflow.

---

## Pipeline Architecture

```text
Synthetic Claims Data
          │
          ▼
     SQLite Database
          │
          ▼
   Data Quality Checks
          │
          ▼
   SQL Risk Analytics
          │
          ▼
 KPI & Cost Analysis
          │
          ▼
 Automated HTML Report
```

---

## Pipeline Steps

1. Generate synthetic healthcare claims data
2. Create SQLite database
3. Run data quality checks
4. Run healthcare claims analytics
5. Generate automated HTML report

---

## Main Outputs

The pipeline automatically generates:

- `data/patients.csv`
- `data/claims.csv`
- `database/healthcare_claims.db`
- `outputs/data_quality_report.csv`
- `outputs/hospital_kpis.csv`
- `outputs/high_risk_patients.csv`
- `outputs/cost_by_diagnosis.csv`
- `reports/healthcare_risk_report.html`

---

## Technologies Used

### Programming & Analytics

- Python
- SQL
- Pandas
- NumPy

### Database

- SQLite

### DevOps

- Docker
- GitHub Actions

### Reporting

- Automated HTML Reports

---

## How to Run the Pipeline

```bash
pip install -r requirements.txt

python src/run_pipeline.py
```

---

## Docker

Build the container:

```bash
docker build -t healthcare-claims-risk-pipeline .
```

Run the pipeline:

```bash
docker run healthcare-claims-risk-pipeline
```

---

## SQL Analytics Included

The project demonstrates advanced SQL analytics techniques including:

- Common Table Expressions (CTEs)
- Window Functions
- Ranking Functions
- Aggregations
- CASE WHEN logic
- Risk segmentation
- Healthcare KPI calculations

---

## Example Analytics Questions

The pipeline helps answer questions such as:

- Which patients are at highest readmission risk?
- Which diagnoses generate the highest hospitalization costs?
- What factors are associated with ICU admissions?
- Which patient groups generate the highest claims costs?
- What is the average hospital length of stay?
- Which diagnoses contribute most to healthcare expenditure?

---

## Automation & DevOps

This project includes:

- Automated pipeline execution
- GitHub Actions CI/CD workflow
- Docker containerization
- Automated HTML report generation
- Reproducible analytics workflow

---

## Repository Structure

```text
healthcare-claims-risk-analytics-pipeline/
│
├── data/
│   ├── patients.csv
│   └── claims.csv
│
├── database/
│   └── healthcare_claims.db
│
├── outputs/
│   ├── data_quality_report.csv
│   ├── hospital_kpis.csv
│   ├── high_risk_patients.csv
│   └── cost_by_diagnosis.csv
│
├── reports/
│   └── healthcare_risk_report.html
│
├── src/
│   └── run_pipeline.py
│
├── requirements.txt
│
├── Dockerfile
│
└── README.md
```

---

## Skills Demonstrated

### Healthcare Analytics

- Healthcare KPI reporting
- Risk stratification
- Readmission analysis
- Cost analytics
- Healthcare utilization analysis

### Data Engineering

- ETL pipeline development
- SQLite database design
- Data quality validation
- Automated reporting workflows

### Analytics Engineering

- SQL analytics
- Pipeline orchestration
- Reproducible workflows
- CI/CD integration

### DevOps

- Docker containerization
- GitHub Actions automation
- Workflow automation

### Tools

- Python
- SQL
- SQLite
- Pandas
- NumPy
- Docker
- GitHub Actions

---

## Future Improvements

Potential future extensions include:

- Machine learning risk prediction models
- Power BI healthcare dashboards
- Cloud deployment on Azure or AWS
- Apache Airflow orchestration
- Real-world healthcare datasets
- SHAP explainability analysis
- Healthcare anomaly detection models
- Predictive hospitalization risk scoring

---

## License

This repository is intended for educational, portfolio, and healthcare analytics learning purposes.

---

## Author

**Agata Gabara**

MSc Bioinformatics Student

Research Interests:

- Healthcare Analytics
- Clinical Informatics
- Data Engineering
- Machine Learning
- Risk Analytics

GitHub: https://github.com/ag48665

LinkedIn: https://www.linkedin.com/in/agatha-gabara-06494a37/
