# Medi-Reach Component Map

## 🗺️ Component Hierarchy

```
App.jsx (Root)
│
├── Navbar (Global)
│   ├── Desktop Navigation
│   ├── Mobile Menu
│   └── Bottom Navigation (Mobile)
│
├── Routes
│   │
│   ├── Home (/)
│   │   ├── Hero Section
│   │   ├── Search Bar
│   │   ├── Features Grid
│   │   └── MedicineCard × 4 (Featured)
│   │
│   ├── Medicines (/medicines)
│   │   ├── Search & Filters
│   │   └── MedicineCard × N (Grid)
│   │
│   ├── MedicineDetails (/medicine/:id)
│   │   ├── Medicine Image
│   │   ├── Info Section
│   │   └── Quantity Selector
│   │
│   ├── Login (/login)
│   │   ├── Logo
│   │   └── Login Form
│   │
│   ├── Signup (/signup)
│   │   └── Registration Form
│   │
│   ├── Order (/order/:id)
│   │   ├── Order Summary
│   │   ├── Delivery Form
│   │   ├── Pharmacy Selection
│   │   ├── Prescription Upload
│   │   └── Price Sidebar
│   │
│   └── Track (/track)
│       ├── Search Form
│       ├── Order Details
│       └── Status Timeline
│
└── Footer (Global)
    ├── Brand Section
    ├── Quick Links
    ├── Support Links
    └── Contact Info
```

## 📦 Component Details

### Reusable Components

#### Navbar
**Location**: `src/components/Navbar.jsx`  
**Props**: None (uses React Router hooks)  
**Features**:
- Desktop horizontal navigation
- Mobile hamburger menu
- Bottom navigation bar (mobile only)
- Authentication state detection
- Active route highlighting

#### Footer
**Location**: `src/components/Footer.jsx`  
**Props**: None  
**Features**:
- Four-column layout (desktop)
- Responsive grid
- Links to all major pages
- Contact information
- Social proof

#### MedicineCard
**Location**: `src/components/MedicineCard.jsx`  
**Props**: 
- `medicine` (object): Medicine data
  - `id`, `name`, `price`, `stock`, `requiresPrescription`, `category`, `image`

**Features**:
- Image display with fallback
- Prescription badge
- Stock indicator
- Price display
- Action buttons (View/Order)

#### Loader
**Location**: `src/components/Loader.jsx`  
**Props**:
- `size` (string): 'small' | 'medium' | 'large'
- `fullScreen` (boolean): Full-screen overlay

**Features**:
- Configurable sizes
- Optional full-screen mode
- Animated spinner
- Centered layout

---

## 📄 Page Components

### Home
**Route**: `/`  
**File**: `src/pages/Home.jsx`  
**State**:
- `searchQuery` (string)

**Sections**:
1. Hero with gradient background
2. Search bar with submit
3. Features grid (4 items)
4. Recommended products (uses MedicineCard)
5. CTA section

### Medicines
**Route**: `/medicines`  
**File**: `src/pages/Medicines.jsx`  
**State**:
- `medicines` (array)
- `filteredMedicines` (array)
- `searchQuery` (string)
- `selectedCategory` (string)
- `showPrescriptionOnly` (boolean)
- `isLoading` (boolean)

**Features**:
- Search with URL params
- Category dropdown
- Prescription filter
- Clear filters
- Empty state
- Responsive grid

### MedicineDetails
**Route**: `/medicine/:id`  
**File**: `src/pages/MedicineDetails.jsx`  
**State**:
- `medicine` (object)
- `quantity` (number)
- `isLoading` (boolean)

**Features**:
- Large image display
- Detailed information
- Quantity selector
- Order button
- Back navigation
- Not found state

### Login
**Route**: `/login`  
**File**: `src/pages/Login.jsx`  
**State**:
- `formData` (object): email, password
- `errors` (object)
- `showPassword` (boolean)
- `isLoading` (boolean)

**Features**:
- Email/password fields
- Show/hide password
- Form validation
- Error messages
- Forgot password link
- Sign up link

### Signup
**Route**: `/signup`  
**File**: `src/pages/Signup.jsx`  
**State**:
- `formData` (object): fullName, email, phone, dateOfBirth, country, password, confirmPassword
- `errors` (object)
- `showPassword` (boolean)
- `showConfirmPassword` (boolean)
- `isLoading` (boolean)

**Features**:
- 7-field registration form
- Password confirmation
- Date picker
- Field validation
- Icon-enhanced inputs

### Order
**Route**: `/order/:id`  
**File**: `src/pages/Order.jsx`  
**State**:
- `medicine` (object)
- `quantity` (number)
- `selectedPharmacy` (number)
- `prescriptionFile` (file)
- `formData` (object): deliveryAddress, city, phone, paymentMethod, notes
- `errors` (object)
- `isSubmitting` (boolean)

**Features**:
- Order summary
- Delivery form
- Pharmacy selection (radio)
- File upload (Rx)
- Payment method
- Price sidebar
- Form validation

### Track
**Route**: `/track`  
**File**: `src/pages/Track.jsx`  
**State**:
- `orderId` (string)
- `order` (object)
- `isSearching` (boolean)
- `error` (string)
- `showSuccess` (boolean)

**Features**:
- Order ID search
- Status timeline
- Order details
- Recent orders
- Success notification
- Contact support

---

## 🔄 Data Flow

### Mock Data Flow
```
mockData.js
    ↓
Pages (useState)
    ↓
Components (props)
    ↓
User Interface
```

### Future API Flow (Ready)
```
User Action
    ↓
Page Component
    ↓
api.js (Axios)
    ↓
Backend API
    ↓
Response
    ↓
State Update
    ↓
UI Re-render
```

---

## 🎨 Styling System

### Tailwind Classes
**Custom Components** (in `index.css`):
- `.btn-primary` - Primary button style
- `.btn-secondary` - Secondary button style
- `.input-field` - Form input style
- `.card` - Card container style

### Color Utilities
- `bg-primary` - Teal background
- `text-primary` - Teal text
- `bg-secondary` - Navy background
- `text-secondary` - Navy text
- `bg-accent-red` - Red background

### Responsive Breakpoints
- `sm:` - 640px and up
- `md:` - 768px and up
- `lg:` - 1024px and up
- `xl:` - 1280px and up

---

## 🔌 Services

### API Service
**Location**: `src/services/api.js`  
**Exports**:
- `api` (default) - Axios instance
- `authAPI` - Authentication endpoints
- `medicineAPI` - Medicine endpoints
- `orderAPI` - Order endpoints
- `pharmacyAPI` - Pharmacy endpoints

**Features**:
- Request interceptor (adds auth token)
- Response interceptor (handles 401)
- Base URL configuration
- Timeout handling

---

## 📊 State Management

### Current: Local State (useState)
Each page manages its own state independently.

### Future Considerations:
- Context API for global state
- Redux for complex state
- React Query for server state

---

## 🧪 Component Testing Guide

### Manual Testing Checklist

**Navbar**:
- [ ] Desktop nav links work
- [ ] Mobile menu toggles
- [ ] Bottom nav appears on mobile
- [ ] Active route highlighted

**MedicineCard**:
- [ ] Displays all medicine info
- [ ] Prescription badge shows when needed
- [ ] Stock indicator correct
- [ ] Buttons navigate correctly

**Forms (Login/Signup/Order)**:
- [ ] Validation triggers on submit
- [ ] Error messages display
- [ ] Success redirects work
- [ ] Loading states show

**Pages**:
- [ ] All routes load
- [ ] Search works
- [ ] Filters work
- [ ] Navigation flows correctly

---

## 💡 Usage Examples

### Using MedicineCard
```jsx
import MedicineCard from '../components/MedicineCard';

<MedicineCard medicine={{
  id: 1,
  name: "Paracetamol",
  price: 2500,
  stock: 50,
  requiresPrescription: false,
  category: "Analgesic"
}} />
```

### Using Loader
```jsx
import Loader from '../components/Loader';

// Small inline loader
<Loader size="small" />

// Full screen loader
<Loader fullScreen />
```

### Accessing Mock Data
```jsx
import { mockMedicines, mockOrders } from '../data/mockData';

const [medicines, setMedicines] = useState(mockMedicines);
```

---

## 🔍 Finding Components

### By Feature
- **Authentication**: Login.jsx, Signup.jsx
- **Medicine Browsing**: Medicines.jsx, MedicineDetails.jsx
- **Ordering**: Order.jsx
- **Tracking**: Track.jsx
- **Navigation**: Navbar.jsx, Footer.jsx
- **UI Elements**: MedicineCard.jsx, Loader.jsx

### By Type
- **Pages**: `src/pages/*.jsx`
- **Components**: `src/components/*.jsx`
- **Services**: `src/services/*.js`
- **Data**: `src/data/*.js`

---

This component map serves as a quick reference for understanding the application structure and finding specific components.
