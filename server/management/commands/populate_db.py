import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from server.models import (
    Account, Profile, Hospital, Location, Speciality, Symptom,
    Appointment, Prescription, MedicalTest, MedicalInfo, Message,
    Notification, Action, Statistics
)

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population...')

        # Clear existing data (optional)
        # Account.objects.all().delete()
        # User.objects.all().delete()

        # Create Specialities
        self.stdout.write('Creating specialities...')
        specialties = [
            ('Cardiology', 'Heart and cardiovascular diseases'),
            ('Neurology', 'Brain and nervous system'),
            ('Orthopedics', 'Bones and joints'),
            ('Dermatology', 'Skin diseases'),
            ('Pediatrics', 'Child medicine'),
            ('Psychiatry', 'Mental health'),
            ('General Practice', 'General medical care'),
            ('Surgery', 'Surgical procedures'),
            ('ENT', 'Ear, nose, throat'),
            ('Ophthalmology', 'Eye care'),
        ]
        speciality_objs = []
        for name, desc in specialties:
            spec, _ = Speciality.objects.get_or_create(
                name=name,
                description=desc
            )
            speciality_objs.append(spec)

        # Create Symptoms
        self.stdout.write('Creating symptoms...')
        symptoms = [
            ('Headache', 'Persistent head pain'),
            ('Fever', 'High body temperature'),
            ('Cough', 'Persistent coughing'),
            ('Fatigue', 'General tiredness'),
            ('Chest Pain', 'Pain in chest area'),
            ('Dizziness', 'Feeling of lightheadedness'),
            ('Nausea', 'Feeling sick'),
            ('Vomiting', 'Ejecting stomach contents'),
            ('Joint Pain', 'Pain in joints'),
            ('Back Pain', 'Pain in back region'),
            ('Sore Throat', 'Throat pain'),
            ('Rash', 'Skin irritation'),
            ('Anxiety', 'Feeling nervous'),
            ('Insomnia', 'Sleep disorder'),
            ('Shortness of Breath', 'Difficulty breathing'),
        ]
        symptom_objs = []
        for name, desc in symptoms:
            sym, _ = Symptom.objects.get_or_create(
                name=name,
                description=desc
            )
            symptom_objs.append(sym)

        # Create Locations
        self.stdout.write('Creating locations...')
        cities = [
            ('Mumbai', '400001', 'Maharashtra'),
            ('Delhi', '110001', 'Delhi'),
            ('Bangalore', '560001', 'Karnataka'),
            ('Chennai', '600001', 'Tamil Nadu'),
            ('Kolkata', '700001', 'West Bengal'),
            ('Hyderabad', '500001', 'Telangana'),
            ('Pune', '411001', 'Maharashtra'),
            ('Ahmedabad', '380001', 'Gujarat'),
            ('Jaipur', '302001', 'Rajashtan'),
            ('Lucknow', '226001', 'Uttar Pradesh'),
        ]
        location_objs = []
        for i, (city, zip_code, state) in enumerate(cities):
            location, _ = Location.objects.get_or_create(
                city=city,
                zip=zip_code,
                state=state,
                country='India',
                defaults={'address': f'{i+1} Healthcare Street, {city}'}
            )
            location_objs.append(location)

        # Create Hospitals
        self.stdout.write('Creating hospitals...')
        hospital_names = [
            'Apollo Hospital', 'Fortis Hospital', 'Max Hospital',
            'Manipal Hospital', 'Medanta Hospital', 'AIIMS',
            'Ruby Hall Clinic', 'Lilavati Hospital', 'Jaslok Hospital',
            'Sir H.N. Reliance Foundation Hospital'
        ]
        hospital_objs = []
        for i, name in enumerate(hospital_names):
            location = location_objs[i % len(location_objs)]
            hospital, _ = Hospital.objects.get_or_create(
                name=name,
                phone=fake.numerify(text='##########')[:10],
                location=location
            )
            hospital_objs.append(hospital)

        # Create Accounts (Admin, Doctors, Patients, Lab, Chemist)
        self.stdout.write('Creating user accounts...')
        
        # Create 1 Admin
        admin_accounts = []
        admin_user = User.objects.create_user(
            username='admin_user',
            email='admin@clinic.com',
            password='admin123'
        )
        admin_profile = Profile.objects.create(
            firstname='Admin',
            lastname='User',
            sex='M',
            birthday=fake.date_of_birth(minimum_age=30, maximum_age=60),
            phone=fake.numerify(text='##########')[:10],
            allergies=''
        )
        admin_account = Account.objects.create(
            role=Account.ACCOUNT_ADMIN,
            profile=admin_profile,
            user=admin_user
        )
        admin_accounts.append(admin_account)

        # Create 50 Doctors
        self.stdout.write('Creating doctors...')
        doctor_accounts = []
        for i in range(50):
            user = User.objects.create_user(
                username=f'doctor_{i}',
                email=f'doctor{i}@clinic.com',
                password='doctor123'
            )
            profile = Profile.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                sex=random.choice(['M', 'F']),
                birthday=fake.date_of_birth(minimum_age=25, maximum_age=65),
                phone=fake.numerify(text='##########')[:10],
                allergies='',
                prefHospital=random.choice(hospital_objs),
                speciality=random.choice(speciality_objs)
            )
            account = Account.objects.create(
                role=Account.ACCOUNT_DOCTOR,
                profile=profile,
                user=user
            )
            doctor_accounts.append(account)

        # Create 150 Patients
        self.stdout.write('Creating patients...')
        patient_accounts = []
        for i in range(150):
            user = User.objects.create_user(
                username=f'patient_{i}',
                email=f'patient{i}@clinic.com',
                password='patient123'
            )
            profile = Profile.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                sex=random.choice(['M', 'F']),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=80),
                phone=fake.numerify(text='##########')[:10],
                allergies=random.choice(['Penicillin', 'Peanuts', 'None', 'Shellfish']),
                prefHospital=random.choice(hospital_objs),
                primaryCareDoctor=random.choice(doctor_accounts)
            )
            account = Account.objects.create(
                role=Account.ACCOUNT_PATIENT,
                profile=profile,
                user=user
            )
            patient_accounts.append(account)

        # Create 10 Lab Accounts
        self.stdout.write('Creating lab accounts...')
        lab_accounts = []
        for i in range(10):
            user = User.objects.create_user(
                username=f'lab_{i}',
                email=f'lab{i}@clinic.com',
                password='lab123'
            )
            profile = Profile.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                sex=random.choice(['M', 'F']),
                birthday=fake.date_of_birth(minimum_age=22, maximum_age=60),
                phone=fake.numerify(text='##########')[:10],
            )
            account = Account.objects.create(
                role=Account.ACCOUNT_LAB,
                profile=profile,
                user=user
            )
            lab_accounts.append(account)

        # Create 10 Chemist Accounts
        self.stdout.write('Creating chemist accounts...')
        chemist_accounts = []
        for i in range(10):
            user = User.objects.create_user(
                username=f'chemist_{i}',
                email=f'chemist{i}@clinic.com',
                password='chemist123'
            )
            profile = Profile.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                sex=random.choice(['M', 'F']),
                birthday=fake.date_of_birth(minimum_age=22, maximum_age=60),
                phone=fake.numerify(text='##########')[:10],
            )
            account = Account.objects.create(
                role=Account.ACCOUNT_CHEMIST,
                profile=profile,
                user=user
            )
            chemist_accounts.append(account)

        # Create Medical Info for Patients
        self.stdout.write('Creating medical information...')
        for patient in patient_accounts:
            MedicalInfo.objects.get_or_create(
                account=patient,
                defaults={
                    'bloodType': random.choice(['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']),
                    'allergy': random.choice(['Penicillin', 'Peanuts', 'None', 'Shellfish']),
                    'alzheimer': random.choice([True, False]),
                    'asthma': random.choice([True, False]),
                    'diabetes': random.choice([True, False]),
                    'stroke': random.choice([True, False]),
                    'comments': fake.text(max_nb_chars=200)
                }
            )

        # Create Appointments
        self.stdout.write('Creating appointments...')
        for i in range(200):
            doctor = random.choice(doctor_accounts)
            patient = random.choice(patient_accounts)
            start_time = fake.date_time_this_year()
            end_time = start_time + timedelta(minutes=30)

            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                description=fake.text(max_nb_chars=100),
                symptom=random.choice(symptom_objs),
                status=random.choice(['Active', 'Completed', 'Cancelled']),
                hospital=random.choice(hospital_objs),
                appointment_type=random.choice(['Offline', 'Online']),
                startTime=start_time,
                endTime=end_time
            )

        # Create Prescriptions
        self.stdout.write('Creating prescriptions...')
        medications = [
            'Aspirin', 'Ibuprofen', 'Paracetamol', 'Amoxicillin', 'Ciprofloxacin',
            'Metformin', 'Lisinopril', 'Atorvastatin', 'Vitamin D', 'Omeprazole'
        ]
        for i in range(200):
            doctor = random.choice(doctor_accounts)
            patient = random.choice(patient_accounts)

            Prescription.objects.create(
                patient=patient,
                doctor=doctor,
                date=fake.date_this_year(),
                medication=random.choice(medications),
                strength=random.choice(['250mg', '500mg', '1000mg', '5mg', '10mg']),
                instruction=random.choice(['Take twice daily', 'Take once daily', 'Take before food', 'Take after food']),
                refill=random.randint(0, 3),
                active=random.choice([True, False])
            )

        # Create Medical Tests
        self.stdout.write('Creating medical tests...')
        test_names = [
            'Blood Test', 'X-Ray', 'CT Scan', 'MRI', 'Ultrasound',
            'ECG', 'EEG', 'Endoscopy', 'Biopsy', 'Glucose Test'
        ]
        for i in range(150):
            doctor = random.choice(doctor_accounts)
            patient = random.choice(patient_accounts)

            MedicalTest.objects.create(
                name=random.choice(test_names),
                date=fake.date_this_year(),
                hospital=random.choice(hospital_objs),
                description=fake.text(max_nb_chars=150),
                doctor=doctor,
                patient=patient,
                private=random.choice([True, False]),
                completed=random.choice([True, False])
            )

        # Create Messages
        self.stdout.write('Creating messages...')
        all_accounts = admin_accounts + doctor_accounts + patient_accounts + lab_accounts + chemist_accounts
        for i in range(300):
            sender = random.choice(all_accounts)
            target = random.choice(all_accounts)
            
            # Avoid sending message to self
            while target == sender:
                target = random.choice(all_accounts)

            Message.objects.create(
                target=target,
                sender=sender,
                header=fake.sentence(nb_words=5),
                body=fake.text(max_nb_chars=500),
                timestamp=fake.date_time_this_year()
            )

        # Create Notifications
        self.stdout.write('Creating notifications...')
        for i in range(250):
            Notification.objects.create(
                account=random.choice(all_accounts),
                message=fake.sentence(nb_words=10),
                read=random.choice([True, False]),
                sent_timestamp=fake.date_time_this_year()
            )

        # Create Actions (Activity Log)
        self.stdout.write('Creating actions...')
        action_descriptions = [
            'Created new account',
            'Updated profile',
            'Created appointment',
            'Cancelled appointment',
            'Uploaded prescription',
            'Completed medical test',
            'Sent message',
            'Updated medical information',
            'Archived account',
            'Restored account'
        ]
        for i in range(300):
            Action.objects.create(
                type=random.choice(list(dict(Action.ACTION_TYPES).keys())),
                description=random.choice(action_descriptions),
                account=random.choice(all_accounts),
                timePerformed=fake.date_time_this_year()
            )

        # Create Statistics
        self.stdout.write('Creating statistics...')
        for i in range(12):
            start_date = datetime(2024, i+1, 1).date()
            end_date = start_date + timedelta(days=30)
            Statistics.objects.create(
                startDate=start_date,
                endDate=end_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))
        self.stdout.write(f'Created:')
        self.stdout.write(f'  - {Account.objects.count()} accounts')
        self.stdout.write(f'  - {Appointment.objects.count()} appointments')
        self.stdout.write(f'  - {Prescription.objects.count()} prescriptions')
        self.stdout.write(f'  - {MedicalTest.objects.count()} medical tests')
        self.stdout.write(f'  - {Message.objects.count()} messages')
        self.stdout.write(f'  - {Notification.objects.count()} notifications')
        self.stdout.write(f'  - {Action.objects.count()} actions')
