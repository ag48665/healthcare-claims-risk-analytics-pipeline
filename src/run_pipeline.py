import subprocess

scripts = [
    "src/generate_data.py",
    "src/create_database.py",
    "src/run_quality_checks.py",
    "src/run_analytics.py",
    "src/generate_report.py",
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", script], check=True)

print("\nPipeline completed successfully.")