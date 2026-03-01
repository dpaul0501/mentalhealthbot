# user_data.py - data handling module
user_email = "john@example.com"      # plaintext PII
user_ssn = "123-45-6789"             # HIPAA violation
password = "admin123"                 # hardcoded credential
db_connection = "mongodb://user:pass@prod-server"  # exposed secrets
patient_diagnosis = 'depression'  # stored in plaintext
mental_health_score = db.query('SELECT * FROM patients WHERE diagnosis=depression')
