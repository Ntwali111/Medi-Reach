# Medi-Reach

A modern web application designed to make medicine search, ordering, and delivery tracking easy and efficient. Medi-Reach bridges the gap between medicine accessibility and delivery efficiency by connecting users with local pharmacies.

![Medi-Reach](https://img.shields.io/badge/Status-Frontend_Complete-success)
![React](https://img.shields.io/badge/React-18.2.0-blue)
![Tailwind](https://img.shields.io/badge/TailwindCSS-3.3.6-38bdf8)

## 🎯 Project Overview

Medi-Reach is a comprehensive medicine delivery platform that allows users to:
- 🔍 Search for medicines from an extensive catalog
- 📦 Place orders with local verified pharmacies
- 🚚 Track deliveries in real-time
- 💊 Upload prescriptions for prescription-required medicines
- 📱 Access the platform from any device (fully responsive)

## 📁 Project Structure

```
Medi-Reach/
│
├── frontend/                    # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── assets/             # Images, icons, etc.
│   │   ├── components/         # Reusable React components
│   │   │   ├── Navbar.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── MedicineCard.jsx
│   │   │   └── Loader.jsx
│   │   ├── pages/              # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── Medicines.jsx
│   │   │   ├── MedicineDetails.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Signup.jsx
│   │   │   ├── Order.jsx
│   │   │   └── Track.jsx
│   │   ├── services/           # API integration
│   │   │   └── api.js
│   │   ├── data/               # Mock data for development
│   │   │   └── mockData.js
│   │   ├── App.jsx             # Main app component
│   │   ├── main.jsx            # Entry point
│   │   └── index.css           # Global styles
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/                     # Backend API (placeholder)
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Git

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   The app will automatically open at `http://localhost:3000`

### Build for Production

```bash
cd frontend
npm run build
```

The production-ready files will be in the `frontend/dist` directory.

## 🎨 Design & Features

### Color Scheme
- **Primary**: Teal/Turquoise (#5DBAAA) - Main brand color
- **Secondary**: Dark Navy (#1E3A5F) - Text and accents
- **Accent Red**: (#EF4444) - Prescription badges and alerts

### Pages & Features

#### 1. **Home Page** (`/`)
- Hero section with search functionality
- Feature highlights
- Recommended medicines
- Call-to-action sections

#### 2. **Medicines Page** (`/medicines`)
- Browse all available medicines
- Advanced search and filtering
- Category filters
- Prescription-only filter
- Responsive grid layout

#### 3. **Medicine Details Page** (`/medicine/:id`)
- Detailed medicine information
- Dosage and side effects
- Stock availability
- Quantity selector
- Direct order placement

#### 4. **Login Page** (`/login`)
- Email and password authentication
- Form validation
- Responsive design matching Figma mockup

#### 5. **Signup Page** (`/signup`)
- Comprehensive registration form
- Field validation
- Date picker for DOB
- Password confirmation

#### 6. **Order Page** (`/order/:id`)
- Order summary
- Delivery address form
- Pharmacy selection
- Prescription upload (for Rx medicines)
- Payment method selection
- Price breakdown

#### 7. **Track Order Page** (`/track`)
- Order ID search
- Real-time status tracking
- Visual timeline
- Order details
- Contact support options

### Responsive Design
- **Mobile-first approach**
- Bottom navigation bar on mobile
- Collapsible filters on mobile
- Adaptive layouts for all screen sizes
- Touch-friendly interface

## 🛠️ Technology Stack

### Frontend
- **Framework**: React 18.2.0
- **Build Tool**: Vite 5.0.8
- **Routing**: React Router DOM 6.20.0
- **Styling**: Tailwind CSS 3.3.6
- **Icons**: Lucide React 0.294.0
- **HTTP Client**: Axios 1.6.2

### Development Tools
- **PostCSS**: For Tailwind processing
- **Autoprefixer**: CSS vendor prefixing

## 📦 Mock Data

The application currently uses mock data for development and testing. Mock data includes:
- 8 sample medicines with various categories
- 3 sample orders with different statuses
- 3 sample pharmacies
- Order status definitions

Mock data is located in `frontend/src/data/mockData.js`

## 🔌 API Integration

The API service is pre-configured in `frontend/src/services/api.js` with:
- Axios instance with interceptors
- Authentication token handling
- Error handling
- Organized endpoint functions for:
  - Authentication
  - Medicines
  - Orders
  - Pharmacies

To connect to a real backend, update the `VITE_API_URL` environment variable.

## 🎯 Key Components

### Navbar
- Responsive navigation
- Mobile menu
- Bottom navigation on mobile
- Authentication state handling

### MedicineCard
- Reusable medicine display
- Prescription badges
- Stock indicators
- Quick actions (view/order)

### Loader
- Configurable sizes
- Full-screen option
- Consistent loading states

### Footer
- Site links
- Contact information
- Responsive layout

## 📱 Mobile Optimization

- Touch-friendly buttons and inputs
- Bottom navigation bar for easy thumb access
- Collapsible filters and menus
- Optimized images and assets
- Fast loading times

## 🔒 Security Features (Planned)

- JWT token authentication
- Secure password handling
- HTTPS enforcement
- Input validation and sanitization
- CORS configuration

## 🚧 Future Enhancements

- [ ] Backend API implementation
- [ ] Real-time order tracking with WebSockets
- [ ] Push notifications
- [ ] Payment gateway integration
- [ ] User profile management
- [ ] Order history
- [ ] Medicine reviews and ratings
- [ ] Pharmacy ratings
- [ ] Advanced search with filters
- [ ] Wishlist functionality
- [ ] Multi-language support

## 📄 License

This project is part of an academic assignment.

## 👥 Contributors

- **Developer**: Medi-Reach Team
- **Design Reference**: Moaye's Figma Design

## 📞 Support

For questions or issues, please contact:
- Email: support@medireach.com
- Phone: +237 222 123 456

---

**Note**: This is the frontend implementation. The backend API is a placeholder and will be implemented in a future phase.
