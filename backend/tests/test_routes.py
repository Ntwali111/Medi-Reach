"""
Unit tests for Medi-Reach API routes
Tests authentication, medicine, and order endpoints
"""

import pytest
import json
from app import create_app, db
from app.models import User, Medicine, Order


@pytest.fixture
def app():
    """Create and configure a test application instance"""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client"""
    return app.test_client()


@pytest.fixture
def auth_headers(client):
    """Create authenticated user and return auth headers"""
    # Register user
    response = client.post('/api/signup', 
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        }
    )
    data = json.loads(response.data)
    token = data['access_token']
    
    return {'Authorization': f'Bearer {token}'}


@pytest.fixture
def admin_headers(client, app):
    """Create admin user and return auth headers"""
    with app.app_context():
        admin = User(
            username='admin',
            email='admin@test.com',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
    
    response = client.post('/api/login',
        json={
            'email': 'admin@test.com',
            'password': 'admin123'
        }
    )
    data = json.loads(response.data)
    token = data['access_token']
    
    return {'Authorization': f'Bearer {token}'}


class TestAuthentication:
    """Test authentication endpoints"""
    
    def test_signup_success(self, client):
        """Test successful user registration"""
        response = client.post('/api/signup',
            json={
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password': 'password123'
            }
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert 'access_token' in data
        assert data['user']['email'] == 'newuser@example.com'
    
    def test_signup_missing_fields(self, client):
        """Test signup with missing fields"""
        response = client.post('/api/signup',
            json={
                'username': 'testuser'
            }
        )
        assert response.status_code == 400
    
    def test_signup_duplicate_email(self, client):
        """Test signup with duplicate email"""
        client.post('/api/signup',
            json={
                'username': 'user1',
                'email': 'duplicate@example.com',
                'password': 'password123'
            }
        )
        
        response = client.post('/api/signup',
            json={
                'username': 'user2',
                'email': 'duplicate@example.com',
                'password': 'password123'
            }
        )
        assert response.status_code == 400
    
    def test_login_success(self, client):
        """Test successful login"""
        # First register
        client.post('/api/signup',
            json={
                'username': 'loginuser',
                'email': 'login@example.com',
                'password': 'password123'
            }
        )
        
        # Then login
        response = client.post('/api/login',
            json={
                'email': 'login@example.com',
                'password': 'password123'
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'access_token' in data
    
    def test_login_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        response = client.post('/api/login',
            json={
                'email': 'nonexistent@example.com',
                'password': 'wrongpassword'
            }
        )
        assert response.status_code == 401
    
    def test_get_current_user(self, client, auth_headers):
        """Test getting current user info"""
        response = client.get('/api/me', headers=auth_headers)
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'user' in data


class TestMedicines:
    """Test medicine endpoints"""
    
    def test_get_medicines(self, client, app):
        """Test getting all medicines"""
        # Add sample medicine
        with app.app_context():
            medicine = Medicine(
                name='Test Medicine',
                category='Test',
                description='Test description',
                price=100.0,
                stock=10
            )
            db.session.add(medicine)
            db.session.commit()
        
        response = client.get('/api/medicines')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'medicines' in data
        assert len(data['medicines']) > 0
    
    def test_get_medicine_by_id(self, client, app):
        """Test getting a single medicine"""
        with app.app_context():
            medicine = Medicine(
                name='Specific Medicine',
                category='Test',
                description='Test description',
                price=150.0,
                stock=5
            )
            db.session.add(medicine)
            db.session.commit()
            medicine_id = medicine.id
        
        response = client.get(f'/api/medicines/{medicine_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['medicine']['name'] == 'Specific Medicine'
    
    def test_create_medicine_admin(self, client, admin_headers):
        """Test creating medicine as admin"""
        response = client.post('/api/medicines',
            headers=admin_headers,
            json={
                'name': 'New Medicine',
                'category': 'Analgesic',
                'description': 'New medicine description',
                'price': 200.0,
                'stock': 20
            }
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['medicine']['name'] == 'New Medicine'
    
    def test_create_medicine_non_admin(self, client, auth_headers):
        """Test creating medicine as non-admin (should fail)"""
        response = client.post('/api/medicines',
            headers=auth_headers,
            json={
                'name': 'New Medicine',
                'category': 'Analgesic',
                'description': 'New medicine description',
                'price': 200.0,
                'stock': 20
            }
        )
        assert response.status_code == 403


class TestOrders:
    """Test order endpoints"""
    
    def test_create_order(self, client, auth_headers, app):
        """Test creating a new order"""
        # First create a medicine
        with app.app_context():
            medicine = Medicine(
                name='Order Medicine',
                category='Test',
                description='Test description',
                price=100.0,
                stock=10
            )
            db.session.add(medicine)
            db.session.commit()
            medicine_id = medicine.id
        
        response = client.post('/api/orders',
            headers=auth_headers,
            json={
                'medicine_id': medicine_id,
                'quantity': 2,
                'delivery_address': '123 Test St',
                'city': 'Test City',
                'phone': '+1234567890'
            }
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert 'order' in data
        assert data['order']['quantity'] == 2
    
    def test_create_order_insufficient_stock(self, client, auth_headers, app):
        """Test creating order with insufficient stock"""
        with app.app_context():
            medicine = Medicine(
                name='Low Stock Medicine',
                category='Test',
                description='Test description',
                price=100.0,
                stock=1
            )
            db.session.add(medicine)
            db.session.commit()
            medicine_id = medicine.id
        
        response = client.post('/api/orders',
            headers=auth_headers,
            json={
                'medicine_id': medicine_id,
                'quantity': 10,
                'delivery_address': '123 Test St',
                'city': 'Test City',
                'phone': '+1234567890'
            }
        )
        assert response.status_code == 400
    
    def test_get_user_orders(self, client, auth_headers):
        """Test getting user's orders"""
        response = client.get('/api/orders', headers=auth_headers)
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'orders' in data
    
    def test_track_order(self, client, auth_headers, app):
        """Test tracking an order"""
        # Create order first
        with app.app_context():
            medicine = Medicine(
                name='Track Medicine',
                category='Test',
                description='Test description',
                price=100.0,
                stock=10
            )
            db.session.add(medicine)
            db.session.commit()
            medicine_id = medicine.id
        
        # Place order
        response = client.post('/api/orders',
            headers=auth_headers,
            json={
                'medicine_id': medicine_id,
                'quantity': 1,
                'delivery_address': '123 Test St',
                'city': 'Test City',
                'phone': '+1234567890'
            }
        )
        data = json.loads(response.data)
        order_number = data['order']['order_number']
        
        # Track order
        response = client.get(f'/api/orders/track/{order_number}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['order']['order_number'] == order_number


class TestErrorHandling:
    """Test error handling"""
    
    def test_404_error(self, client):
        """Test 404 error handling"""
        response = client.get('/api/nonexistent')
        assert response.status_code == 404
    
    def test_unauthorized_access(self, client):
        """Test unauthorized access to protected route"""
        response = client.get('/api/me')
        assert response.status_code == 401
    
    def test_invalid_json(self, client):
        """Test invalid JSON in request"""
        response = client.post('/api/login',
            data='invalid json',
            content_type='application/json'
        )
        assert response.status_code in [400, 500]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
