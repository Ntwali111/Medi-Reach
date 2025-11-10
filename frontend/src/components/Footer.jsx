import { Link } from 'react-router-dom';
import { Package, Mail, Phone, MapPin } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-secondary text-white mt-auto mb-16 md:mb-0">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <div className="w-10 h-10 bg-primary rounded-full flex items-center justify-center">
                <Package className="text-white" size={24} />
              </div>
              <span className="text-2xl font-bold">Medi-Reach</span>
            </div>
            <p className="text-gray-300 text-sm">
              Making medicine accessible and delivery efficient for everyone.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="text-gray-300 hover:text-primary transition-colors">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/medicines" className="text-gray-300 hover:text-primary transition-colors">
                  Medicines
                </Link>
              </li>
              <li>
                <Link to="/track" className="text-gray-300 hover:text-primary transition-colors">
                  Track Order
                </Link>
              </li>
              <li>
                <Link to="/about" className="text-gray-300 hover:text-primary transition-colors">
                  About Us
                </Link>
              </li>
            </ul>
          </div>

          {/* Support */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Support</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/faq" className="text-gray-300 hover:text-primary transition-colors">
                  FAQ
                </Link>
              </li>
              <li>
                <Link to="/contact" className="text-gray-300 hover:text-primary transition-colors">
                  Contact Us
                </Link>
              </li>
              <li>
                <Link to="/privacy" className="text-gray-300 hover:text-primary transition-colors">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link to="/terms" className="text-gray-300 hover:text-primary transition-colors">
                  Terms of Service
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact</h3>
            <ul className="space-y-3">
              <li className="flex items-start space-x-2">
                <MapPin size={20} className="text-primary mt-1 flex-shrink-0" />
                <span className="text-gray-300 text-sm">
                  123 Medical Street, Healthcare City
                </span>
              </li>
              <li className="flex items-center space-x-2">
                <Phone size={20} className="text-primary flex-shrink-0" />
                <span className="text-gray-300 text-sm">+250794903699</span>
              </li>
              <li className="flex items-center space-x-2">
                <Mail size={20} className="text-primary flex-shrink-0" />
                <span className="text-gray-300 text-sm">support@medireach.com</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400 text-sm">
          <p>&copy; {new Date().getFullYear()} Medi-Reach. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
