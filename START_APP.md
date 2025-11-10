# 🚀 Quick Start Guide - Medi-Reach

## Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed
- Git Bash or PowerShell

---

## 🎯 Quick Start (3 Steps)

### Step 1: Start Backend (Terminal 1)
```bash
cd backend
pip install -r requirements.txt
python run.py
```
✅ Backend running at: **http://127.0.0.1:5000**

### Step 2: Setup & Start Frontend (Terminal 2)
```bash
cd frontend

# Copy environment file
cp .env.example .env

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```
✅ Frontend running at: **http://localhost:3000**

### Step 3: Open Browser
Navigate to: **http://localhost:3000**

---

## 🔐 Test Credentials

### Admin Account
- **Email**: `admin@medireach.com`
- **Password**: `admin123`

### Or Create New Account
- Click "Sign Up" and register

---

## ✅ Verify Integration

1. **Login** with admin credentials
2. **Browse Medicines** - Should see 8 medicines
3. **Search** for "para" - Should filter results
4. **View Details** - Click any medicine
5. **Place Order** - Click order button (requires login)
6. **Track Order** - Use order number from confirmation

---

## 🛠️ Troubleshooting

### Backend not starting?
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

### Frontend not starting?
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Can't see medicines?
- Check backend is running at http://127.0.0.1:5000
- Check frontend .env file has correct API_URL
- Check browser console for errors

---

## 📁 Project Structure

```
Medi-Reach/
├── backend/          # Flask API (Port 5000)
│   ├── app/          # Application code
│   ├── instance/     # Database (auto-created)
│   └── run.py        # Start here
│
├── frontend/         # React App (Port 3000)
│   ├── src/          # Source code
│   ├── .env          # Environment config
│   └── package.json  # Dependencies
│
└── Documentation
    ├── README.md
    ├── INTEGRATION_GUIDE.md
    └── START_APP.md (this file)
```

---

## 🎉 You're All Set!

The application should now be running with:
- ✅ Backend API at http://127.0.0.1:5000
- ✅ Frontend UI at http://localhost:3000
- ✅ Database with sample data
- ✅ Admin account ready to use

**Enjoy using Medi-Reach!** 💊
