import { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, ShoppingCart, AlertCircle, Package, Info } from 'lucide-react';
import { mockMedicines } from '../data/mockData';
import Loader from '../components/Loader';

const MedicineDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [medicine, setMedicine] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    // Simulate API call
    setTimeout(() => {
      const found = mockMedicines.find(m => m.id === parseInt(id));
      setMedicine(found);
      setIsLoading(false);
    }, 500);
  }, [id]);

  const handleQuantityChange = (delta) => {
    const newQuantity = quantity + delta;
    if (newQuantity >= 1 && newQuantity <= (medicine?.stock || 1)) {
      setQuantity(newQuantity);
    }
  };

  const handleOrder = () => {
    navigate(`/order/${id}`, { state: { quantity } });
  };

  if (isLoading) {
    return <Loader fullScreen />;
  }

  if (!medicine) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <Package size={64} className="mx-auto text-gray-400 mb-4" />
          <h2 className="text-2xl font-bold text-gray-700 mb-2">Medicine Not Found</h2>
          <p className="text-gray-500 mb-6">The medicine you're looking for doesn't exist.</p>
          <Link to="/medicines" className="btn-primary">
            Browse Medicines
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Back Button */}
        <Link
          to="/medicines"
          className="inline-flex items-center space-x-2 text-primary hover:text-primary-dark mb-6 transition-colors"
        >
          <ArrowLeft size={20} />
          <span>Back to Medicines</span>
        </Link>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Medicine Image */}
          <div className="bg-white rounded-xl shadow-md p-8">
            <div className="relative">
              {medicine.requiresPrescription && (
                <div className="absolute top-4 right-4 bg-accent-red text-white px-4 py-2 rounded-full font-medium flex items-center space-x-2 z-10">
                  <AlertCircle size={20} />
                  <span>Rx Required</span>
                </div>
              )}
              <div className="bg-gray-100 rounded-lg h-96 flex items-center justify-center">
                {medicine.image ? (
                  <img
                    src={medicine.image}
                    alt={medicine.name}
                    className="w-full h-full object-cover rounded-lg"
                  />
                ) : (
                  <div className="text-center text-gray-400">
                    <Package size={96} />
                    <p className="mt-4 text-lg">No Image Available</p>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Medicine Info */}
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-md p-8">
              <div className="mb-6">
                <span className="inline-block px-3 py-1 bg-primary/10 text-primary rounded-full text-sm font-medium mb-3">
                  {medicine.category}
                </span>
                <h1 className="text-3xl md:text-4xl font-bold text-secondary mb-2">
                  {medicine.name}
                </h1>
                <p className="text-gray-600">by {medicine.manufacturer}</p>
              </div>

              <div className="border-t border-b py-6 mb-6">
                <div className="flex items-baseline space-x-2 mb-2">
                  <span className="text-4xl font-bold text-primary">{medicine.price}</span>
                  <span className="text-xl text-gray-600">XAF</span>
                </div>
                <p className={`text-sm ${medicine.stock > 0 ? 'text-green-600' : 'text-red-600'}`}>
                  {medicine.stock > 0 ? `${medicine.stock} units in stock` : 'Out of stock'}
                </p>
              </div>

              {/* Quantity Selector */}
              {medicine.stock > 0 && (
                <div className="mb-6">
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Quantity
                  </label>
                  <div className="flex items-center space-x-4">
                    <button
                      onClick={() => handleQuantityChange(-1)}
                      disabled={quantity <= 1}
                      className="w-10 h-10 rounded-lg border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                      -
                    </button>
                    <span className="text-xl font-semibold w-12 text-center">{quantity}</span>
                    <button
                      onClick={() => handleQuantityChange(1)}
                      disabled={quantity >= medicine.stock}
                      className="w-10 h-10 rounded-lg border border-gray-300 flex items-center justify-center hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                      +
                    </button>
                  </div>
                </div>
              )}

              {/* Order Button */}
              <button
                onClick={handleOrder}
                disabled={medicine.stock === 0}
                className="btn-primary w-full flex items-center justify-center space-x-2"
              >
                <ShoppingCart size={20} />
                <span>{medicine.stock > 0 ? 'Place Order' : 'Out of Stock'}</span>
              </button>
            </div>

            {/* Additional Info */}
            <div className="bg-white rounded-xl shadow-md p-8">
              <h2 className="text-xl font-bold text-secondary mb-4 flex items-center space-x-2">
                <Info size={24} />
                <span>Product Information</span>
              </h2>
              
              <div className="space-y-4">
                <div>
                  <h3 className="font-semibold text-gray-700 mb-1">Description</h3>
                  <p className="text-gray-600">{medicine.description}</p>
                </div>

                <div>
                  <h3 className="font-semibold text-gray-700 mb-1">Dosage</h3>
                  <p className="text-gray-600">{medicine.dosage}</p>
                </div>

                <div>
                  <h3 className="font-semibold text-gray-700 mb-1">Side Effects</h3>
                  <p className="text-gray-600">{medicine.sideEffects}</p>
                </div>

                {medicine.requiresPrescription && (
                  <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                    <div className="flex items-start space-x-2">
                      <AlertCircle className="text-red-600 flex-shrink-0 mt-0.5" size={20} />
                      <div>
                        <h4 className="font-semibold text-red-800 mb-1">
                          Prescription Required
                        </h4>
                        <p className="text-sm text-red-700">
                          This medicine requires a valid prescription from a licensed healthcare provider.
                          You will need to upload your prescription during the order process.
                        </p>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MedicineDetails;
