# Medi-Reach Frontend-Backend Integration Guide

## ✅ Integration Complete

The React frontend and Flask backend are now fully integrated and working together seamlessly.

---

## 🔗 What Was Integrated

### 1. **API Connection**
- ✅ Frontend configured to connect to backend at `http://127.0.0.1:5000/api`
- ✅ Environment variables set up (`.env.example`)
- ✅ Axios instance with interceptors for auth tokens
- ✅ All API endpoints mapped to backend routes

### 2. **Authentication Flow**
- ✅ JWT token storage in localStorage
- ✅ AuthContext for global auth state management
- ✅ Protected routes with ProtectedRoute component
- ✅ Login/Signup pages connected to real API
- ✅ Automatic token refresh on API calls
- ✅ Logout functionality with token cleanup

### 3. **Data Flow**
- ✅ Medicines page fetches from backend API
- ✅ Real-time category filtering from backend
- ✅ Medicine details from database
- ✅ Order placement with backend validation
- ✅ Order tracking with real order data

### 4. **UI Updates**
- ✅ Navbar shows authenticated user info
- ✅ Logout button functional
- ✅ Error messages from API displayed
- ✅ Loading states during API calls
- ✅ Field name mapping (frontend ↔ backend)

---

## 🚀 How to Run the Full Application

### Step 1: Start the Backend

```bash
# Terminal 1 - Backend
cd backend
python run.py
```

**Backend will run at:** `http://127.0.0.1:5000`

### Step 2: Configure Frontend Environment

Create `frontend/.env` file:
```bash
cd frontend
cp .env.example .env
```

The `.env` file should contain:
```env
VITE_API_URL=http://127.0.0.1:5000/api
```

### Step 3: Start the Frontend

```bash
# Terminal 2 - Frontend
cd frontend
npm run dev
```

**Frontend will run at:** `http://localhost:3000`

### Step 4: Access the Application

Open your browser and navigate to: `http://localhost:3000`

---

## 🔐 Authentication Flow

### User Registration
1. Navigate to `/signup`
2. Fill in the registration form
3. Click "Submit Registration"
4. JWT token is automatically stored
5. User is redirected to home page
6. Navbar shows user info

### User Login
1. Navigate to `/login`
2. Enter credentials:
   - **Admin**: `admin@medireach.com` / `admin123`
   - **Or create new account**
3. Click "Sign In"
4. JWT token stored in localStorage
5. Redirected to home page

### Protected Routes
- `/order/:id` - Requires authentication
- Automatically redirects to `/login` if not authenticated
- Returns to intended page after login

### Logout
- Click "Logout" button in navbar
- Token removed from localStorage
- Redirected to login page

---

## 📡 API Integration Details

### Authentication Endpoints

#### Signup
```javascript
POST /api/signup
Body: {
  username, email, password,
  full_name, phone, date_of_birth, country
}
Response: { user, access_token, refresh_token }
```

#### Login
```javascript
POST /api/login
Body: { email, password }
Response: { user, access_token, refresh_token }
```

#### Get Current User
```javascript
GET /api/me
Headers: { Authorization: Bearer {token} }
Response: { user }
```

### Medicine Endpoints

#### Get All Medicines
```javascript
GET /api/medicines
Query: { page, per_page, category, search, requires_prescription }
Response: { medicines[], total, page, pages }
```

#### Get Single Medicine
```javascript
GET /api/medicines/{id}
Response: { medicine }
```

#### Get Categories
```javascript
GET /api/medicines/categories
Response: { categories[] }
```

### Order Endpoints

#### Create Order
```javascript
POST /api/orders
Headers: { Authorization: Bearer {token} }
Body: {
  medicine_id, quantity,
  delivery_address, city, phone,
  pharmacy_name, payment_method, notes,
  prescription_url (if required)
}
Response: { order }
```

#### Track Order
```javascript
GET /api/orders/track/{order_number}
Response: { order }
```

---

## 🔄 Data Field Mapping

### Frontend → Backend

| Frontend Field | Backend Field | Notes |
|----------------|---------------|-------|
| `requiresPrescription` | `requires_prescription` | Boolean |
| `image` | `image_url` | String (URL) |
| `fullName` | `full_name` | User field |
| `dateOfBirth` | `date_of_birth` | Date string |

### Component Updates Made

1. **MedicineCard.jsx**
   - Updated to use `requires_prescription`
   - Updated to use `image_url`

2. **Medicines.jsx**
   - Fetches from `medicineAPI.getAll()`
   - Fetches categories from `medicineAPI.getCategories()`
   - Uses real API data instead of mock data

3. **Login.jsx**
   - Uses `useAuth()` hook
   - Calls `authAPI.login()`
   - Displays API errors

4. **Signup.jsx**
   - Uses `useAuth()` hook
   - Calls `authAPI.signup()`
   - Maps form fields to API format

5. **Navbar.jsx**
   - Uses `useAuth()` hook
   - Shows user info when authenticated
   - Logout button functional

---

## 🎯 Testing the Integration

### Test 1: User Registration
1. Go to `/signup`
2. Fill form with:
   - Full Name: Test User
   - Email: test@example.com
   - Phone: +1234567890
   - Date of Birth: 1990-01-01
   - Country: USA
   - Password: password123
3. Submit
4. ✅ Should redirect to home
5. ✅ Navbar should show "Hi, test"

### Test 2: User Login
1. Go to `/login`
2. Enter:
   - Email: admin@medireach.com
   - Password: admin123
3. Click Sign In
4. ✅ Should redirect to home
5. ✅ Navbar should show "Hi, admin"

### Test 3: Browse Medicines
1. Go to `/medicines`
2. ✅ Should see 8 medicines from database
3. ✅ Categories dropdown should show real categories
4. Try search: "para"
5. ✅ Should filter medicines
6. Try category filter: "Analgesic"
7. ✅ Should show only analgesics

### Test 4: View Medicine Details
1. Click on any medicine card
2. ✅ Should show full details from database
3. ✅ Should show dosage, side effects, manufacturer
4. ✅ Prescription badge if required

### Test 5: Place Order (Protected)
1. Click "Order" on a medicine
2. If not logged in:
   - ✅ Should redirect to `/login`
   - ✅ After login, should return to order page
3. Fill order form
4. Click "Place Order"
5. ✅ Should create order in database
6. ✅ Should redirect to tracking page

### Test 6: Logout
1. Click "Logout" in navbar
2. ✅ Should clear token
3. ✅ Should redirect to login
4. ✅ Trying to access `/order/1` should redirect to login

---

## 🛠️ Technical Implementation

### AuthContext (`src/context/AuthContext.jsx`)
```javascript
- Manages global authentication state
- Provides login(), signup(), logout() methods
- Checks auth status on mount
- Stores JWT token in localStorage
- Provides user object to all components
```

### ProtectedRoute (`src/components/ProtectedRoute.jsx`)
```javascript
- Wraps protected components
- Checks isAuthenticated from AuthContext
- Redirects to /login if not authenticated
- Shows loader while checking auth
```

### API Service (`src/services/api.js`)
```javascript
- Axios instance with base URL
- Request interceptor: adds Bearer token
- Response interceptor: handles 401 errors
- Organized endpoint functions
- Matches backend API exactly
```

### App.jsx Updates
```javascript
- Wrapped in AuthProvider
- Protected routes use ProtectedRoute component
- All components have access to auth context
```

---

## 🔒 Security Features

### Implemented
- ✅ JWT token authentication
- ✅ Password hashing (backend)
- ✅ Protected routes
- ✅ Token expiration handling
- ✅ Automatic logout on 401
- ✅ CORS configured
- ✅ Input validation (frontend & backend)

### Token Management
- **Storage**: localStorage
- **Header**: `Authorization: Bearer {token}`
- **Expiration**: 24 hours (access token)
- **Refresh**: 30 days (refresh token)
- **Cleanup**: On logout or 401 error

---

## 📊 Data Flow Diagram

```
User Action (Frontend)
    ↓
React Component
    ↓
API Service (axios)
    ↓
Add JWT Token (interceptor)
    ↓
HTTP Request → Flask Backend
    ↓
Verify JWT Token
    ↓
Process Request
    ↓
Database (SQLite)
    ↓
JSON Response ← Flask Backend
    ↓
Update State (React)
    ↓
Re-render UI
```

---

## 🐛 Troubleshooting

### Issue: "Failed to fetch medicines"
**Solution**: Make sure backend is running at `http://127.0.0.1:5000`

### Issue: "Network Error"
**Solution**: Check CORS settings in backend and frontend API URL

### Issue: "Token has expired"
**Solution**: Login again to get new token

### Issue: "Unauthorized"
**Solution**: Check if token is in localStorage: `localStorage.getItem('token')`

### Issue: Medicines not showing
**Solution**: 
1. Check backend is running
2. Check database has data: `http://127.0.0.1:5000/api/medicines`
3. Check browser console for errors

### Issue: Login not working
**Solution**:
1. Check credentials (admin@medireach.com / admin123)
2. Check backend logs for errors
3. Check network tab in browser DevTools

---

## 📝 Environment Variables

### Frontend (`.env`)
```env
VITE_API_URL=http://127.0.0.1:5000/api
VITE_APP_NAME=Medi-Reach
VITE_APP_VERSION=1.0.0
```

### Backend (`.env`)
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
DATABASE_URI=sqlite:///medi_reach.db
FRONTEND_URL=http://localhost:3000
```

---

## ✅ Integration Checklist

- [x] Backend API running
- [x] Frontend connecting to backend
- [x] Authentication working (login/signup)
- [x] JWT tokens stored and sent
- [x] Protected routes functional
- [x] Medicines fetched from database
- [x] Categories loaded from backend
- [x] Medicine details from API
- [x] Order placement integrated
- [x] Order tracking functional
- [x] Error handling implemented
- [x] Loading states added
- [x] Logout working
- [x] User info displayed in navbar
- [x] Field name mapping complete
- [x] CORS configured
- [x] Environment variables set

---

## 🎉 Success!

The Medi-Reach application is now fully integrated with:
- ✅ React frontend communicating with Flask backend
- ✅ JWT authentication flow complete
- ✅ Real-time data from database
- ✅ Protected routes working
- ✅ Error handling and validation
- ✅ Professional user experience

**The application is ready for use and testing!**

---

## 📚 Next Steps (Optional Enhancements)

1. **Add Order History Page**
   - Show user's past orders
   - Use `orderAPI.getMyOrders()`

2. **Add Admin Dashboard**
   - Manage medicines
   - View all orders
   - Update order statuses

3. **Add Profile Page**
   - View/edit user info
   - Change password

4. **Add Real-time Notifications**
   - Order status updates
   - Low stock alerts

5. **Add Payment Integration**
   - Stripe/PayPal
   - Mobile money

6. **Add Image Upload**
   - Medicine images
   - Prescription uploads

7. **Add Search Autocomplete**
   - Suggest medicines as you type

8. **Add Reviews & Ratings**
   - User feedback on medicines
   - Pharmacy ratings

---

**Integration completed successfully! Both frontend and backend are working together seamlessly.** 🚀
