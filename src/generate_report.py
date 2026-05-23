import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("outputs")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

hospital_kpis = pd.read_csv(OUTPUT_DIR / "hospital_kpis.csv")
high_risk_patients = pd.read_csv(OUTPUT_DIR / "high_risk_patients.csv")
cost_by_diagnosis = pd.read_csv(OUTPUT_DIR / "cost_by_diagnosis.csv")
quality_report = pd.read_csv(OUTPUT_DIR / "data_quality_report.csv")

html = f"""
<html>
<head>
    <title>Healthcare Claims Risk Analytics Report</title>
</head>
<body>
    <h1>Healthcare Claims Risk Analytics Report</h1>

    <h2>Data Quality Report</h2>
    {quality_report.to_html(index=False)}

    <h2>Hospital KPIs</h2>
    {hospital_kpis.to_html(index=False)}

    <h2>High-Risk Patients</h2>
    {high_risk_patients.to_html(index=False)}

    <h2>Cost by Diagnosis</h2>
    {cost_by_diagnosis.to_html(index=False)}

    <h2>Summary</h2>
    <p>This automated report summarizes healthcare claims, readmission risk, ICU cases, and hospital cost patterns.</p>
</body>
</html>
"""

report_path = REPORT_DIR / "healthcare_risk_report.html"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(html)

print(f"HTML report generated successfully: {report_path}")