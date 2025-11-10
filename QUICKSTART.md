# Medi-Reach Quick Start Guide

## 🚀 Running the Frontend

### Step 1: Install Dependencies
```bash
cd frontend
npm install
```

### Step 2: Start Development Server
```bash
npm run dev
```

The application will open automatically at `http://localhost:3000`

## 📱 Testing the Application

### Available Routes

1. **Home Page**: `http://localhost:3000/`
   - Search for medicines
   - View featured products
   - Navigate to other sections

2. **Medicines Page**: `http://localhost:3000/medicines`
   - Browse all medicines
   - Use search and filters
   - Click on any medicine card to view details

3. **Medicine Details**: `http://localhost:3000/medicine/1`
   - View detailed information
   - Adjust quantity
   - Click "Place Order"

4. **Login**: `http://localhost:3000/login`
   - Enter any email and password (mock authentication)
   - Click "Sign In"

5. **Signup**: `http://localhost:3000/signup`
   - Fill out the registration form
   - Click "Submit Registration"

6. **Order Page**: `http://localhost:3000/order/1`
   - Fill delivery information
   - Select pharmacy
   - Upload prescription (for Rx medicines)
   - Place order

7. **Track Order**: `http://localhost:3000/track`
   - Enter order ID: `ORD-001`, `ORD-002`, or `ORD-003`
   - View order status and timeline

## 🎨 Design Features to Notice

### Color Scheme (from Figma)
- **Primary Teal**: #5DBAAA (buttons, accents)
- **Dark Navy**: #1E3A5F (text, headers)
- **Red Badges**: For prescription-required medicines

### Responsive Features
- **Desktop**: Full navigation bar at top
- **Mobile**: Bottom navigation bar (try resizing browser)
- **Tablet**: Adaptive layouts

### Interactive Elements
- Hover effects on cards and buttons
- Smooth transitions
- Loading states
- Form validation with error messages

## 📦 Mock Data

The app uses mock data located in `frontend/src/data/mockData.js`:

- **8 medicines** with different categories and prices
- **3 sample orders** with various statuses
- **3 pharmacies** with ratings and distances

## 🔧 Common Commands

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## ✅ Verification Checklist

- [ ] All 7 pages load correctly
- [ ] Navigation works (desktop and mobile)
- [ ] Search functionality works on Home and Medicines pages
- [ ] Filters work on Medicines page
- [ ] Medicine cards display properly
- [ ] Login/Signup forms validate input
- [ ] Order form validates required fields
- [ ] Track order shows timeline correctly
- [ ] Mobile bottom navigation appears on small screens
- [ ] All buttons and links are clickable

## 🐛 Troubleshooting

### Port Already in Use
If port 3000 is already in use:
```bash
# The dev server will automatically try port 3001, 3002, etc.
# Or specify a different port:
npm run dev -- --port 3001
```

### Dependencies Not Installing
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Styles Not Loading
Make sure Tailwind CSS is properly configured. The CSS warnings about `@tailwind` directives are normal - they're processed by PostCSS during build.

## 📝 Notes

- **Authentication**: Currently uses mock authentication (any credentials work)
- **Data Persistence**: No data is saved (refresh resets everything)
- **Backend**: Not implemented yet - all data is mock/local
- **Images**: Medicine images are placeholders (null in mock data)

## 🎯 Next Steps

After verifying the frontend works:
1. Test all routes and features
2. Check responsive design on different screen sizes
3. Verify form validations
4. Test the complete user flow (browse → order → track)

## 💡 Tips

- Use browser DevTools to test mobile responsiveness
- Check the console for any errors
- Try different order IDs in the track page
- Test with medicines that require prescriptions vs. those that don't

---

**Ready to start?** Run `cd frontend && npm install && npm run dev` and enjoy! 🎉
