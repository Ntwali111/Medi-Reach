"""
Medi-Reach Backend - Entry Point
Run this file to start the Flask application
"""

import os
from app import create_app, db

# Create Flask application
app = create_app()


@app.cli.command()
def init_db():
    """Initialize the database"""
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")


@app.cli.command()
def seed_db():
    """Seed the database with initial data"""
    from app.utils import seed_database
    with app.app_context():
        seed_database()


@app.cli.command()
def create_admin():
    """Create an admin user"""
    from app.models import User
    
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")
    username = input("Enter admin username: ")
    
    with app.app_context():
        # Check if user exists
        if User.query.filter_by(email=email).first():
            print("User with this email already exists!")
            return
        
        admin = User(
            username=username,
            email=email,
            full_name="Admin User",
            is_admin=True
        )
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        
        print(f"Admin user created successfully! Email: {email}")


if __name__ == '__main__':
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
