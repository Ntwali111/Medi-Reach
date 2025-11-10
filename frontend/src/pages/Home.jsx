import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Search, Package, Truck, Shield, Clock } from 'lucide-react';
import { mockMedicines } from '../data/mockData';
import MedicineCard from '../components/MedicineCard';

const Home = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/medicines?search=${encodeURIComponent(searchQuery)}`);
    }
  };

  const featuredMedicines = mockMedicines.slice(0, 4);

  const features = [
    {
      icon: Search,
      title: 'Easy Search',
      description: 'Find medicines quickly with our smart search',
    },
    {
      icon: Package,
      title: 'Wide Selection',
      description: 'Access to thousands of medicines and health products',
    },
    {
      icon: Truck,
      title: 'Fast Delivery',
      description: 'Get your medicines delivered to your doorstep',
    },
    {
      icon: Shield,
      title: 'Verified Pharmacies',
      description: 'All pharmacies are licensed and verified',
    },
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary to-primary-dark text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Welcome to Medi-Reach
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-white/90">
              Your trusted partner for medicine delivery. Search, order, and track with ease.
            </p>

            {/* Search Bar */}
            <form onSubmit={handleSearch} className="max-w-2xl mx-auto">
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search for medicines, etc..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full px-6 py-4 rounded-full text-gray-800 text-lg focus:outline-none focus:ring-4 focus:ring-white/30 pr-14"
                />
                <button
                  type="submit"
                  className="absolute right-2 top-1/2 -translate-y-1/2 bg-secondary text-white p-3 rounded-full hover:bg-secondary-light transition-colors"
                >
                  <Search size={24} />
                </button>
              </div>
            </form>

            {/* Quick Actions */}
            <div className="flex flex-wrap justify-center gap-4 mt-8">
              <Link
                to="/medicines"
                className="bg-white text-primary px-6 py-3 rounded-full font-medium hover:bg-gray-100 transition-colors"
              >
                Browse Medicines
              </Link>
              <Link
                to="/track"
                className="bg-secondary text-white px-6 py-3 rounded-full font-medium hover:bg-secondary-light transition-colors"
              >
                Track Order
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl md:text-4xl font-bold text-center text-secondary mb-12">
            Why Choose Medi-Reach?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="text-center p-6 rounded-xl hover:bg-gray-50 transition-colors"
              >
                <div className="inline-flex items-center justify-center w-16 h-16 bg-primary/10 rounded-full mb-4">
                  <feature.icon className="text-primary" size={32} />
                </div>
                <h3 className="text-xl font-semibold text-secondary mb-2">
                  {feature.title}
                </h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Recommended Products */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-8">
            <h2 className="text-3xl md:text-4xl font-bold text-secondary">
              Recommended Products
            </h2>
            <Link
              to="/medicines"
              className="text-primary hover:text-primary-dark font-medium flex items-center space-x-1"
            >
              <span>View All</span>
              <span>→</span>
            </Link>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {featuredMedicines.map((medicine) => (
              <MedicineCard key={medicine.id} medicine={medicine} />
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-secondary text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Clock className="mx-auto mb-6 text-primary" size={64} />
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Need Medicine Urgently?
          </h2>
          <p className="text-xl mb-8 text-white/90">
            Order now and get fast delivery from verified pharmacies near you
          </p>
          <Link
            to="/medicines"
            className="inline-block bg-primary text-white px-8 py-4 rounded-full text-lg font-medium hover:bg-primary-dark transition-colors"
          >
            Order Now
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Home;
