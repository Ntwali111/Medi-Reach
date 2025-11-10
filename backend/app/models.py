"""
Database models for Medi-Reach
Defines User, Medicine, and Order models using SQLAlchemy ORM
"""

from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    User model for authentication and user management
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)
    full_name = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    country = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Relationships
    orders = db.relationship('Order', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set user password"""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password against hash"""
        return check_password_hash(self.password, password)
    
    def to_dict(self, include_orders=False):
        """Convert user object to dictionary"""
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'country': self.country,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_admin': self.is_admin
        }
        if include_orders:
            data['orders'] = [order.to_dict() for order in self.orders.all()]
        return data
    
    def __repr__(self):
        return f'<User {self.username}>'


class Medicine(db.Model):
    """
    Medicine model for medicine catalog management
    """
    __tablename__ = 'medicines'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    category = db.Column(db.String(50), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(200))
    side_effects = db.Column(db.Text)
    manufacturer = db.Column(db.String(150))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    requires_prescription = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    orders = db.relationship('Order', backref='medicine', lazy='dynamic')
    
    def to_dict(self):
        """Convert medicine object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'dosage': self.dosage,
            'side_effects': self.side_effects,
            'manufacturer': self.manufacturer,
            'price': self.price,
            'stock': self.stock,
            'requires_prescription': self.requires_prescription,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Medicine {self.name}>'


class Order(db.Model):
    """
    Order model for order management and tracking
    """
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending', nullable=False)
    
    # Delivery information
    delivery_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    pharmacy_name = db.Column(db.String(150))
    payment_method = db.Column(db.String(50), default='Cash on Delivery')
    notes = db.Column(db.Text)
    
    # Prescription (if required)
    prescription_url = db.Column(db.String(255))
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estimated_delivery = db.Column(db.DateTime)
    delivered_at = db.Column(db.DateTime)
    
    def to_dict(self, include_user=False, include_medicine=False):
        """Convert order object to dictionary"""
        data = {
            'id': self.id,
            'order_number': self.order_number,
            'user_id': self.user_id,
            'medicine_id': self.medicine_id,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'status': self.status,
            'delivery_address': self.delivery_address,
            'city': self.city,
            'phone': self.phone,
            'pharmacy_name': self.pharmacy_name,
            'payment_method': self.payment_method,
            'notes': self.notes,
            'prescription_url': self.prescription_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'estimated_delivery': self.estimated_delivery.isoformat() if self.estimated_delivery else None,
            'delivered_at': self.delivered_at.isoformat() if self.delivered_at else None
        }
        
        if include_user and self.user:
            data['user'] = self.user.to_dict()
        
        if include_medicine and self.medicine:
            data['medicine'] = self.medicine.to_dict()
        
        return data
    
    def __repr__(self):
        return f'<Order {self.order_number}>'
