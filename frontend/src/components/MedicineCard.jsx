import { Link } from 'react-router-dom';
import { ShoppingCart, AlertCircle, Package } from 'lucide-react';

const MedicineCard = ({ medicine }) => {
  const { id, name, price, stock, requires_prescription, category, image_url } = medicine;
  const image = image_url;

  return (
    <div className="card group">
      {/* Medicine Image */}
      <div className="relative mb-4 overflow-hidden rounded-lg bg-gray-100 h-48 flex items-center justify-center">
        {image ? (
          <img
            src={image}
            alt={name}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-200"
          />
        ) : (
          <div className="text-gray-400 text-center">
            <Package size={48} />
            <p className="text-sm mt-2">No Image</p>
          </div>
        )}
        
        {/* Prescription Badge */}
        {requires_prescription && (
          <div className="absolute top-2 right-2 bg-accent-red text-white text-xs px-2 py-1 rounded-full font-medium flex items-center space-x-1">
            <AlertCircle size={12} />
            <span>Rx Required</span>
          </div>
        )}
      </div>

      {/* Medicine Info */}
      <div className="space-y-2">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <h3 className="font-semibold text-lg text-secondary group-hover:text-primary transition-colors">
              {name}
            </h3>
            <p className="text-sm text-gray-500 capitalize">{category}</p>
          </div>
        </div>

        <div className="flex items-center justify-between pt-2">
          <div>
            <p className="text-2xl font-bold text-primary">{price} XAF</p>
            <p className="text-sm text-gray-500">
              {stock > 0 ? `${stock} in stock` : 'Out of stock'}
            </p>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex space-x-2 pt-3">
          <Link
            to={`/medicine/${id}`}
            className="flex-1 text-center px-4 py-2 border border-primary text-primary rounded-lg hover:bg-primary hover:text-white transition-colors"
          >
            View Details
          </Link>
          <Link
            to={`/order/${id}`}
            className={`flex items-center justify-center px-4 py-2 rounded-lg transition-colors ${
              stock > 0
                ? 'bg-primary text-white hover:bg-primary-dark'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            onClick={(e) => stock === 0 && e.preventDefault()}
          >
            <ShoppingCart size={20} />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default MedicineCard;
