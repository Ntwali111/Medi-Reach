import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Medicines from './pages/Medicines';
import MedicineDetails from './pages/MedicineDetails';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Order from './pages/Order';
import Track from './pages/Track';

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/medicines" element={<Medicines />} />
            <Route path="/medicine/:id" element={<MedicineDetails />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/order/:id" element={<Order />} />
            <Route path="/track" element={<Track />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
