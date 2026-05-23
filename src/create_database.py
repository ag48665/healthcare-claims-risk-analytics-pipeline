import sqlite3
import pandas as pd
from pathlib import Path

# Paths
DATA_DIR = Path("data")
DB_DIR = Path("database")

DB_DIR.mkdir(exist_ok=True)

# Database path
db_path = DB_DIR / "healthcare_claims.db"

# Connect SQLite
conn = sqlite3.connect(db_path)

# Load CSV files
patients = pd.read_csv(DATA_DIR / "patients.csv")
claims = pd.read_csv(DATA_DIR / "claims.csv")

# Save tables
patients.to_sql("patients", conn, if_exists="replace", index=False)
claims.to_sql("claims", conn, if_exists="replace", index=False)

print("Healthcare database created successfully.")

# Close connection
conn.close()