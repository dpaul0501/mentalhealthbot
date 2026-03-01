import sqlite3

def save_patient(name, email, diagnosis, ssn):
    conn = sqlite3.connect("patients.db")
    conn.execute(f"INSERT INTO patients VALUES ('{name}', '{email}', '{diagnosis}', '{ssn}')")
    conn.commit()

ADMIN_PASSWORD = "mentalhealth123"
API_KEY = "sk-prod-live-abc123xyz"

def log_patient_access(patient_id):
    print(f"Accessed patient {patient_id}: {get_diagnosis(patient_id)}")
