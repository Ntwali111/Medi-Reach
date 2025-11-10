# Medi-Reach Backend

This directory is a placeholder for the backend API implementation.

## Planned Features

- User authentication and authorization
- Medicine catalog management
- Order processing and tracking
- Pharmacy management
- Prescription verification
- Payment integration
- Real-time delivery tracking

## Technology Stack (Planned)

- **Framework**: Flask or Django
- **Database**: PostgreSQL or MongoDB
- **Authentication**: JWT tokens
- **File Storage**: AWS S3 or local storage for prescriptions
- **API Documentation**: Swagger/OpenAPI

## Setup (When Implemented)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

## API Endpoints (Planned)

### Authentication
- POST `/api/auth/signup` - User registration
- POST `/api/auth/login` - User login
- POST `/api/auth/logout` - User logout

### Medicines
- GET `/api/medicines` - Get all medicines
- GET `/api/medicines/:id` - Get medicine by ID
- GET `/api/medicines/search` - Search medicines

### Orders
- POST `/api/orders` - Create new order
- GET `/api/orders/:id` - Get order by ID
- GET `/api/orders/my-orders` - Get user's orders
- PATCH `/api/orders/:id/status` - Update order status

### Pharmacies
- GET `/api/pharmacies` - Get all pharmacies
- GET `/api/pharmacies/:id` - Get pharmacy by ID
- GET `/api/pharmacies/nearby` - Get nearby pharmacies

## Notes

The frontend is currently using mock data. Once the backend is implemented, update the API base URL in `frontend/src/services/api.js`.
