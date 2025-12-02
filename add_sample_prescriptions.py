#!/usr/bin/env python
import os
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtualclinic.settings')
django.setup()

from server.models import Prescription, Account

# Get a doctor and patient to create a prescription
doctors = Account.objects.filter(role=Account.ACCOUNT_DOCTOR)
patients = Account.objects.filter(role=Account.ACCOUNT_PATIENT)

if doctors.exists() and patients.exists():
    doctor = doctors.first()
    patient = patients.first()
    
    # Create sample prescriptions
    prescriptions_data = [
        {
            'medication': 'Aspirin',
            'strength': '500mg',
            'instruction': 'Take twice daily after meals',
            'refill': 3,
        },
        {
            'medication': 'Amoxicillin',
            'strength': '250mg',
            'instruction': 'Take three times daily for 7 days',
            'refill': 0,
        },
        {
            'medication': 'Metformin',
            'strength': '1000mg',
            'instruction': 'Take once daily in the morning',
            'refill': 5,
        },
        {
            'medication': 'Lisinopril',
            'strength': '10mg',
            'instruction': 'Take once daily in the morning',
            'refill': 12,
        },
    ]
    
    for data in prescriptions_data:
        prescription = Prescription(
            patient=patient,
            doctor=doctor,
            date=date.today(),
            medication=data['medication'],
            strength=data['strength'],
            instruction=data['instruction'],
            refill=data['refill'],
            active=True
        )
        prescription.save()
        print(f"✅ Created prescription: {data['medication']} for {patient}")
    
    print(f"\n✅ Successfully added {len(prescriptions_data)} sample prescriptions!")
else:
    print("❌ No doctors or patients found in the database.")
    print("Please create a doctor and patient account first.")
