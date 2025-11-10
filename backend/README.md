# Medi-Reach Backend API

A complete Flask-based RESTful API for the Medi-Reach medicine delivery platform. This backend handles user authentication, medicine catalog management, order processing, and delivery tracking.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)
![JWT](https://img.shields.io/badge/JWT-Auth-red)

## 🎯 Features

- ✅ **User Authentication** - JWT-based authentication with secure password hashing
- ✅ **Medicine Management** - Full CRUD operations for medicine catalog
- ✅ **Order System** - Place, track, and manage medicine orders
- ✅ **Role-Based Access** - Admin and user role separation
- ✅ **Order Tracking** - Real-time order status updates
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Input Validation** - Comprehensive request validation
- ✅ **Error Handling** - Proper HTTP status codes and error messages
- ✅ **Database Seeding** - Auto-populate with sample data

## 🛠️ Technology Stack

- **Framework**: Flask 3.0.0
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-JWT-Extended
- **CORS**: Flask-CORS
- **Testing**: Pytest
- **Password Hashing**: Werkzeug Security

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py          # Application factory
│   ├── config.py            # Configuration settings
│   ├── models.py            # Database models
│   ├── auth.py              # Authentication routes
│   ├── medicine_routes.py   # Medicine CRUD routes
│   ├── order_routes.py      # Order management routes
│   └── utils.py             # Helper functions
├── tests/
│   ├── __init__.py
│   └── test_routes.py       # Unit tests
├── instance/
│   └── medi_reach.db        # SQLite database (auto-created)
├── requirements.txt
├── run.py                   # Application entry point
├── .env.example             # Environment variables template
└── README.md
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the backend directory:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URI=sqlite:///medi_reach.db
FRONTEND_URL=http://localhost:3000
```

### 3. Run the Application

```bash
python run.py
```

The API will be available at `http://localhost:5000`

### 4. Access the API

- **Root**: http://localhost:5000/
- **Health Check**: http://localhost:5000/health
- **API Base**: http://localhost:5000/api/

## 📚 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Authentication Endpoints

#### 1. User Signup
```http
POST /api/signup
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "phone": "+1234567890",
  "date_of_birth": "1990-01-01",
  "country": "USA"
}
```

**Response (201 Created):**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "is_admin": false
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### 2. User Login
```http
POST /api/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "user": { ... },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### 3. Get Current User
```http
GET /api/me
Authorization: Bearer {access_token}
```

**Response (200 OK):**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe"
  }
}
```

#### 4. Refresh Token
```http
POST /api/refresh
Authorization: Bearer {refresh_token}
```

#### 5. Logout
```http
POST /api/logout
Authorization: Bearer {access_token}
```

---

### Medicine Endpoints

#### 1. Get All Medicines
```http
GET /api/medicines?page=1&per_page=20&category=Analgesic&search=para
```

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `per_page` (int): Items per page (default: 20)
- `category` (string): Filter by category
- `search` (string): Search in name/description
- `requires_prescription` (boolean): Filter by prescription requirement

**Response (200 OK):**
```json
{
  "medicines": [
    {
      "id": 1,
      "name": "Paracetamol 500mg",
      "category": "Analgesic",
      "description": "Pain reliever and fever reducer",
      "price": 2500.0,
      "stock": 50,
      "requires_prescription": false,
      "dosage": "1-2 tablets every 4-6 hours",
      "side_effects": "Rare: nausea, stomach pain",
      "manufacturer": "PharmaCorp Ltd."
    }
  ],
  "total": 8,
  "page": 1,
  "per_page": 20,
  "pages": 1
}
```

#### 2. Get Single Medicine
```http
GET /api/medicines/{id}
```

**Response (200 OK):**
```json
{
  "medicine": {
    "id": 1,
    "name": "Paracetamol 500mg",
    ...
  }
}
```

#### 3. Create Medicine (Admin Only)
```http
POST /api/medicines
Authorization: Bearer {admin_token}
Content-Type: application/json

{
  "name": "Aspirin 100mg",
  "category": "Analgesic",
  "description": "Pain reliever",
  "price": 3000.0,
  "stock": 100,
  "dosage": "1 tablet daily",
  "side_effects": "Stomach upset",
  "manufacturer": "HealthCorp",
  "requires_prescription": false
}
```

**Response (201 Created):**
```json
{
  "message": "Medicine created successfully",
  "medicine": { ... }
}
```

#### 4. Update Medicine (Admin Only)
```http
PUT /api/medicines/{id}
Authorization: Bearer {admin_token}
Content-Type: application/json

{
  "price": 3500.0,
  "stock": 150
}
```

#### 5. Delete Medicine (Admin Only)
```http
DELETE /api/medicines/{id}
Authorization: Bearer {admin_token}
```

#### 6. Get Categories
```http
GET /api/medicines/categories
```

**Response (200 OK):**
```json
{
  "categories": ["Analgesic", "Antibiotic", "Antihistamine", "Antidiabetic", "Digestive", "Supplement"]
}
```

---

### Order Endpoints

#### 1. Create Order
```http
POST /api/orders
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "medicine_id": 1,
  "quantity": 2,
  "delivery_address": "123 Main Street",
  "city": "New York",
  "phone": "+1234567890",
  "pharmacy_name": "Central Pharmacy",
  "payment_method": "Cash on Delivery",
  "notes": "Please call before delivery",
  "prescription_url": "https://example.com/prescription.pdf"
}
```

**Response (201 Created):**
```json
{
  "message": "Order placed successfully",
  "order": {
    "id": 1,
    "order_number": "ORD-ABC123",
    "medicine_id": 1,
    "quantity": 2,
    "total_price": 5000.0,
    "status": "Pending",
    "delivery_address": "123 Main Street",
    "estimated_delivery": "2024-11-13T10:00:00",
    "medicine": { ... }
  }
}
```

#### 2. Get User Orders
```http
GET /api/orders?status=Pending&page=1
Authorization: Bearer {access_token}
```

**Query Parameters:**
- `status` (string): Filter by order status
- `page` (int): Page number
- `per_page` (int): Items per page

**Response (200 OK):**
```json
{
  "orders": [ ... ],
  "total": 5,
  "page": 1,
  "per_page": 20,
  "pages": 1
}
```

#### 3. Get Single Order
```http
GET /api/orders/{id}
Authorization: Bearer {access_token}
```

#### 4. Track Order (Public)
```http
GET /api/orders/track/{order_number}
```

**Response (200 OK):**
```json
{
  "order": {
    "order_number": "ORD-ABC123",
    "status": "In Transit",
    "estimated_delivery": "2024-11-13T10:00:00",
    ...
  }
}
```

#### 5. Update Order Status (Admin Only)
```http
PUT /api/orders/{id}/status
Authorization: Bearer {admin_token}
Content-Type: application/json

{
  "status": "Delivered"
}
```

**Valid Statuses:**
- `Pending`
- `Processing`
- `Confirmed`
- `In Transit`
- `Delivered`
- `Cancelled`

#### 6. Cancel Order
```http
DELETE /api/orders/{id}
Authorization: Bearer {access_token}
```

#### 7. Get All Orders (Admin Only)
```http
GET /api/orders/all?status=Pending
Authorization: Bearer {admin_token}
```

#### 8. Get Order Statistics (Admin Only)
```http
GET /api/orders/stats
Authorization: Bearer {admin_token}
```

**Response (200 OK):**
```json
{
  "total_orders": 150,
  "pending": 20,
  "processing": 15,
  "delivered": 100,
  "cancelled": 15,
  "total_revenue": 450000.0
}
```

---

## 🔐 Authentication

All protected routes require a JWT token in the Authorization header:

```http
Authorization: Bearer {access_token}
```

### Token Expiration
- **Access Token**: 24 hours
- **Refresh Token**: 30 days

### Admin Routes
The following routes require admin privileges:
- `POST /api/medicines`
- `PUT /api/medicines/{id}`
- `DELETE /api/medicines/{id}`
- `PUT /api/orders/{id}/status`
- `GET /api/orders/all`
- `GET /api/orders/stats`

---

## 🗄️ Database Models

### User
```python
- id (Integer, Primary Key)
- username (String)
- email (String, Unique)
- password (String, Hashed)
- full_name (String)
- phone (String)
- date_of_birth (Date)
- country (String)
- is_admin (Boolean)
- created_at (DateTime)
```

### Medicine
```python
- id (Integer, Primary Key)
- name (String)
- category (String)
- description (Text)
- dosage (String)
- side_effects (Text)
- manufacturer (String)
- price (Float)
- stock (Integer)
- requires_prescription (Boolean)
- image_url (String)
- created_at (DateTime)
- updated_at (DateTime)
```

### Order
```python
- id (Integer, Primary Key)
- order_number (String, Unique)
- user_id (Foreign Key)
- medicine_id (Foreign Key)
- quantity (Integer)
- total_price (Float)
- status (String)
- delivery_address (String)
- city (String)
- phone (String)
- pharmacy_name (String)
- payment_method (String)
- notes (Text)
- prescription_url (String)
- created_at (DateTime)
- updated_at (DateTime)
- estimated_delivery (DateTime)
- delivered_at (DateTime)
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_routes.py

# Run with coverage
pytest --cov=app tests/
```

---

## 🔧 CLI Commands

### Initialize Database
```bash
flask init-db
```

### Seed Database
```bash
flask seed-db
```

### Create Admin User
```bash
flask create-admin
```

---

## 📊 Default Data

When the application starts for the first time, it automatically seeds the database with:

### Admin User
- **Email**: admin@medireach.com
- **Password**: admin123
- **Role**: Admin

### Sample Medicines (8 items)
- Paracetamol 500mg
- Amoxicillin 250mg (Rx)
- Omeprazole 20mg
- Cetirizine 10mg
- Metformin 500mg (Rx)
- Ibuprofen 400mg
- Ciprofloxacin 500mg (Rx)
- Vitamin D3 1000IU

---

## ⚠️ Error Handling

All errors return JSON responses with appropriate HTTP status codes:

```json
{
  "error": "Error message description"
}
```

### Common Status Codes
- `200 OK` - Successful GET/PUT request
- `201 Created` - Successful POST request
- `400 Bad Request` - Invalid input data
- `401 Unauthorized` - Missing or invalid token
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

---

## 🔌 Frontend Integration

### Update Frontend API URL

In `frontend/src/services/api.js`, the base URL is already configured:

```javascript
baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api'
```

Create `frontend/.env`:
```env
VITE_API_URL=http://localhost:5000/api
```

### CORS Configuration

CORS is enabled for the frontend URL specified in `.env`:
```env
FRONTEND_URL=http://localhost:3000
```

---

## 🚀 Deployment

### Production Checklist

1. **Change Secret Keys**
   ```env
   SECRET_KEY=your-production-secret-key
   JWT_SECRET_KEY=your-production-jwt-secret-key
   ```

2. **Set Environment**
   ```env
   FLASK_ENV=production
   ```

3. **Use Production Database**
   ```env
   DATABASE_URI=postgresql://user:pass@host:port/dbname
   ```

4. **Configure CORS**
   ```env
   FRONTEND_URL=https://your-frontend-domain.com
   ```

5. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

---

## 📝 Notes

- Database is automatically created on first run
- Sample data is seeded automatically if database is empty
- JWT tokens are stored client-side (frontend responsibility)
- Prescription URLs should point to secure file storage (S3, etc.)
- Order numbers are auto-generated with format `ORD-XXXXXX`

---

## 🤝 Contributing

This is an academic project. For improvements:
1. Follow PEP 8 style guide
2. Add tests for new features
3. Update API documentation
4. Maintain backward compatibility

---

## 📄 License

This project is part of an academic assignment.

---

## 👥 Support

For questions or issues:
- **Email**: support@medireach.com
- **Documentation**: This README
- **API Testing**: Use Postman or curl

---

**Backend Status**: ✅ Complete and ready for frontend integration!
