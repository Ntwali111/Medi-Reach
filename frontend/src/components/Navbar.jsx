import { Link, useLocation } from 'react-router-dom';
import { Home, Package, ShoppingCart, User, Menu, X } from 'lucide-react';
import { useState } from 'react';

const Navbar = () => {
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const isAuthenticated = localStorage.getItem('token');

  const navLinks = [
    { path: '/', label: 'Home', icon: Home },
    { path: '/medicines', label: 'Medicines', icon: Package },
    { path: '/track', label: 'Track Order', icon: ShoppingCart },
  ];

  return (
    <>
      {/* Desktop Navbar */}
      <nav className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center space-x-2">
              <div className="w-10 h-10 bg-primary rounded-full flex items-center justify-center">
                <Package className="text-white" size={24} />
              </div>
              <span className="text-2xl font-bold text-secondary">Medi-Reach</span>
            </Link>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  className={`flex items-center space-x-1 px-3 py-2 rounded-lg transition-colors ${
                    location.pathname === link.path
                      ? 'text-primary font-semibold'
                      : 'text-gray-600 hover:text-primary'
                  }`}
                >
                  <link.icon size={20} />
                  <span>{link.label}</span>
                </Link>
              ))}
            </div>

            {/* Auth Buttons */}
            <div className="hidden md:flex items-center space-x-4">
              {isAuthenticated ? (
                <Link
                  to="/profile"
                  className="flex items-center space-x-2 px-4 py-2 rounded-lg bg-primary text-white hover:bg-primary-dark transition-colors"
                >
                  <User size={20} />
                  <span>Profile</span>
                </Link>
              ) : (
                <>
                  <Link
                    to="/login"
                    className="px-4 py-2 text-secondary hover:text-primary transition-colors"
                  >
                    Login
                  </Link>
                  <Link
                    to="/signup"
                    className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors"
                  >
                    Sign Up
                  </Link>
                </>
              )}
            </div>

            {/* Mobile Menu Button */}
            <button
              className="md:hidden p-2"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden bg-white border-t">
            <div className="px-4 py-4 space-y-3">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  onClick={() => setIsMenuOpen(false)}
                  className={`flex items-center space-x-2 px-3 py-2 rounded-lg ${
                    location.pathname === link.path
                      ? 'bg-primary text-white'
                      : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  <link.icon size={20} />
                  <span>{link.label}</span>
                </Link>
              ))}
              <div className="pt-3 border-t space-y-2">
                {isAuthenticated ? (
                  <Link
                    to="/profile"
                    onClick={() => setIsMenuOpen(false)}
                    className="flex items-center space-x-2 px-3 py-2 rounded-lg bg-primary text-white"
                  >
                    <User size={20} />
                    <span>Profile</span>
                  </Link>
                ) : (
                  <>
                    <Link
                      to="/login"
                      onClick={() => setIsMenuOpen(false)}
                      className="block px-3 py-2 text-center rounded-lg border border-primary text-primary"
                    >
                      Login
                    </Link>
                    <Link
                      to="/signup"
                      onClick={() => setIsMenuOpen(false)}
                      className="block px-3 py-2 text-center rounded-lg bg-primary text-white"
                    >
                      Sign Up
                    </Link>
                  </>
                )}
              </div>
            </div>
          </div>
        )}
      </nav>

      {/* Mobile Bottom Navigation */}
      <div className="md:hidden fixed bottom-0 left-0 right-0 bg-primary shadow-lg z-50">
        <div className="flex justify-around items-center h-16">
          {navLinks.map((link) => (
            <Link
              key={link.path}
              to={link.path}
              className={`flex flex-col items-center justify-center flex-1 h-full ${
                location.pathname === link.path
                  ? 'text-white'
                  : 'text-white/70'
              }`}
            >
              <link.icon size={24} />
              <span className="text-xs mt-1">{link.label}</span>
            </Link>
          ))}
          <Link
            to={isAuthenticated ? '/profile' : '/login'}
            className={`flex flex-col items-center justify-center flex-1 h-full ${
              location.pathname === '/profile' || location.pathname === '/login'
                ? 'text-white'
                : 'text-white/70'
            }`}
          >
            <User size={24} />
            <span className="text-xs mt-1">Account</span>
          </Link>
        </div>
      </div>
    </>
  );
};

export default Navbar;
