"""
Utility functions for Medi-Reach backend
Helper functions for validation, decorators, and database seeding
"""

import re
import random
import string
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app import db
from app.models import User, Medicine


def validate_email(email):
    """
    Validate email format
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """
    Validate password strength
    
    Args:
        password (str): Password to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    return len(password) >= 6


def generate_order_number():
    """
    Generate a unique order number
    
    Returns:
        str: Unique order number (e.g., ORD-ABC123)
    """
    prefix = 'ORD-'
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return prefix + random_part


def admin_required(fn):
    """
    Decorator to require admin privileges
    
    Args:
        fn: Function to wrap
    
    Returns:
        Wrapped function that checks for admin status
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin privileges required'}), 403
        
        return fn(*args, **kwargs)
    
    return wrapper


def seed_database():
    """
    Seed the database with initial data if empty
    Creates admin user and sample medicines
    """
    # Check if database is already seeded
    if User.query.count() > 0 or Medicine.query.count() > 0:
        return
    
    print("Seeding database with initial data...")
    
    # Create admin user
    admin = User(
        username='admin',
        email='admin@medireach.com',
        full_name='Admin User',
        is_admin=True
    )
    admin.set_password('admin123')
    db.session.add(admin)
    
    # Create sample medicines
    sample_medicines = [
        {
            'name': 'Paracetamol 500mg',
            'category': 'Analgesic',
            'description': 'Effective pain reliever and fever reducer. Used for headaches, muscle aches, arthritis, backache, toothaches, colds, and fevers.',
            'dosage': '1-2 tablets every 4-6 hours as needed',
            'side_effects': 'Rare: nausea, stomach pain, loss of appetite',
            'manufacturer': 'PharmaCorp Ltd.',
            'price': 2500.0,
            'stock': 50,
            'requires_prescription': False
        },
        {
            'name': 'Amoxicillin 250mg',
            'category': 'Antibiotic',
            'description': 'Broad-spectrum antibiotic used to treat various bacterial infections including respiratory, ear, nose, throat, urinary tract, and skin infections.',
            'dosage': 'As prescribed by physician, typically 250-500mg every 8 hours',
            'side_effects': 'Nausea, vomiting, diarrhea, rash',
            'manufacturer': 'MediPharm International',
            'price': 13000.0,
            'stock': 30,
            'requires_prescription': True
        },
        {
            'name': 'Omeprazole 20mg',
            'category': 'Digestive',
            'description': 'Proton pump inhibitor used to treat gastroesophageal reflux disease (GERD), stomach ulcers, and other conditions involving excessive stomach acid.',
            'dosage': '20mg once daily before meals',
            'side_effects': 'Headache, nausea, diarrhea, stomach pain',
            'manufacturer': 'HealthCare Solutions',
            'price': 8000.0,
            'stock': 25,
            'requires_prescription': False
        },
        {
            'name': 'Cetirizine 10mg',
            'category': 'Antihistamine',
            'description': 'Antihistamine used to relieve allergy symptoms such as watery eyes, runny nose, itching eyes/nose, sneezing, hives, and itching.',
            'dosage': '10mg once daily',
            'side_effects': 'Drowsiness, dry mouth, fatigue',
            'manufacturer': 'AllergyRelief Inc.',
            'price': 3500.0,
            'stock': 40,
            'requires_prescription': False
        },
        {
            'name': 'Metformin 500mg',
            'category': 'Antidiabetic',
            'description': 'First-line medication for type 2 diabetes. Helps control blood sugar levels by improving insulin sensitivity.',
            'dosage': 'As prescribed, typically 500mg twice daily with meals',
            'side_effects': 'Nausea, diarrhea, stomach upset',
            'manufacturer': 'DiabetesCare Pharma',
            'price': 15000.0,
            'stock': 20,
            'requires_prescription': True
        },
        {
            'name': 'Ibuprofen 400mg',
            'category': 'Analgesic',
            'description': 'Nonsteroidal anti-inflammatory drug (NSAID) used to reduce fever and treat pain or inflammation.',
            'dosage': '400mg every 4-6 hours as needed',
            'side_effects': 'Upset stomach, mild heartburn, nausea',
            'manufacturer': 'PainRelief Pharmaceuticals',
            'price': 4000.0,
            'stock': 35,
            'requires_prescription': False
        },
        {
            'name': 'Ciprofloxacin 500mg',
            'category': 'Antibiotic',
            'description': 'Fluoroquinolone antibiotic used to treat various bacterial infections including urinary tract infections, respiratory infections, and skin infections.',
            'dosage': 'As prescribed by physician',
            'side_effects': 'Nausea, diarrhea, dizziness, headache',
            'manufacturer': 'Advanced Antibiotics Ltd.',
            'price': 18000.0,
            'stock': 15,
            'requires_prescription': True
        },
        {
            'name': 'Vitamin D3 1000IU',
            'category': 'Supplement',
            'description': 'Essential vitamin supplement for bone health, immune function, and overall wellness.',
            'dosage': '1 tablet daily with food',
            'side_effects': 'Rare: nausea, constipation',
            'manufacturer': 'VitaHealth Supplements',
            'price': 6000.0,
            'stock': 45,
            'requires_prescription': False
        }
    ]
    
    for med_data in sample_medicines:
        medicine = Medicine(**med_data)
        db.session.add(medicine)
    
    try:
        db.session.commit()
        print("Database seeded successfully!")
        print("Admin credentials: admin@medireach.com / admin123")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {str(e)}")


def format_error_response(error_message, status_code=400):
    """
    Format error response consistently
    
    Args:
        error_message (str): Error message
        status_code (int): HTTP status code
    
    Returns:
        tuple: JSON response and status code
    """
    return jsonify({'error': error_message}), status_code


def format_success_response(data, message=None, status_code=200):
    """
    Format success response consistently
    
    Args:
        data (dict): Response data
        message (str, optional): Success message
        status_code (int): HTTP status code
    
    Returns:
        tuple: JSON response and status code
    """
    response = data.copy() if isinstance(data, dict) else {'data': data}
    if message:
        response['message'] = message
    return jsonify(response), status_code
