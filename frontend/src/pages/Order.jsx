import { useState, useEffect } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import { ArrowLeft, MapPin, Upload, CreditCard, CheckCircle } from 'lucide-react';
import { mockMedicines, mockPharmacies } from '../data/mockData';
import Loader from '../components/Loader';

const Order = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const [medicine, setMedicine] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [quantity, setQuantity] = useState(location.state?.quantity || 1);
  const [selectedPharmacy, setSelectedPharmacy] = useState(mockPharmacies[0]?.id || null);
  const [prescriptionFile, setPrescriptionFile] = useState(null);
  const [formData, setFormData] = useState({
    deliveryAddress: '',
    city: '',
    phone: '',
    paymentMethod: 'cash',
    notes: '',
  });
  const [errors, setErrors] = useState({});
  const [addresses, setAddresses] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem('mr_addresses') || '[]');
    } catch {
      return [];
    }
  });
  const [selectedAddressId, setSelectedAddressId] = useState(null);
  const [addressEditor, setAddressEditor] = useState({ id: null, name: '', street: '', city: '', contact: '' });
  const [isEditingAddress, setIsEditingAddress] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      const found = mockMedicines.find(m => m.id === parseInt(id));
      setMedicine(found);
      setIsLoading(false);
    }, 500);
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const saveAddresses = (list) => {
    setAddresses(list);
    localStorage.setItem('mr_addresses', JSON.stringify(list));
  };

  const handleSelectAddress = (id) => {
    setSelectedAddressId(id);
    const addr = addresses.find(a => a.id === id);
    if (addr) {
      setFormData(prev => ({
        ...prev,
        deliveryAddress: addr.street,
        city: addr.city,
        phone: addr.contact
      }));
    }
  };

  const startAddAddress = () => {
    setAddressEditor({ id: null, name: '', street: '', city: '', contact: '' });
    setIsEditingAddress(true);
  };

  const startEditAddress = () => {
    const addr = addresses.find(a => a.id === selectedAddressId);
    if (!addr) return;
    setAddressEditor({ ...addr });
    setIsEditingAddress(true);
  };

  const handleDeleteAddress = () => {
    if (!selectedAddressId) return;
    const next = addresses.filter(a => a.id !== selectedAddressId);
    saveAddresses(next);
    setSelectedAddressId(null);
  };

  const handleAddressEditorChange = (e) => {
    const { name, value } = e.target;
    setAddressEditor(prev => ({ ...prev, [name]: value }));
  };

  const commitAddressEditor = () => {
    const { id, name, street, city, contact } = addressEditor;
    if (!name || !street || !city || !contact) return;
    if (id) {
      const next = addresses.map(a => (a.id === id ? { id, name, street, city, contact } : a));
      saveAddresses(next);
      setSelectedAddressId(id);
    } else {
      const newId = 'addr_' + Math.random().toString(36).slice(2, 9);
      const next = [...addresses, { id: newId, name, street, city, contact }];
      saveAddresses(next);
      setSelectedAddressId(newId);
    }
    setIsEditingAddress(false);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setPrescriptionFile(file);
      setErrors(prev => ({ ...prev, prescription: '' }));
    }
  };

  const validate = () => {
    const newErrors = {};
    
    if (!formData.deliveryAddress) newErrors.deliveryAddress = 'Delivery address is required';
    if (!formData.city) newErrors.city = 'City is required';
    if (!formData.phone) newErrors.phone = 'Phone number is required';
    if (!selectedPharmacy) newErrors.pharmacy = 'Please select a pharmacy';
    if (medicine?.requiresPrescription && !prescriptionFile) {
      newErrors.prescription = 'Prescription is required for this medicine';
    }
    
    return newErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const newErrors = validate();
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setIsSubmitting(true);
    
    // Simulate API call
    setTimeout(() => {
      const orderId = 'ORD-' + Math.random().toString(36).substr(2, 9).toUpperCase();

      // Persist selected address for this order
      try {
        const map = JSON.parse(localStorage.getItem('mr_order_address_map') || '{}');
        const selected = addresses.find(a => a.id === selectedAddressId) || null;
        if (selected) {
          map[orderId] = selected;
          localStorage.setItem('mr_order_address_map', JSON.stringify(map));
        }
      } catch {}

      setIsSubmitting(false);
      navigate('/track', { 
        state: { 
          orderId,
          success: true,
          message: 'Order placed successfully!',
          selectedAddress: addresses.find(a => a.id === selectedAddressId) || null
        } 
      });
    }, 1500);
  };

  if (isLoading) {
    return <Loader fullScreen />;
  }

  if (!medicine) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-700 mb-2">Medicine Not Found</h2>
          <button onClick={() => navigate('/medicines')} className="btn-primary mt-4">
            Browse Medicines
          </button>
        </div>
      </div>
    );
  }

  const totalPrice = medicine.price * quantity;

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Back Button */}
        <button
          onClick={() => navigate(-1)}
          className="inline-flex items-center space-x-2 text-primary hover:text-primary-dark mb-6 transition-colors"
        >
          <ArrowLeft size={20} />
          <span>Back</span>
        </button>

        <h1 className="text-3xl md:text-4xl font-bold text-secondary mb-8">Place Order</h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Order Form */}
          <div className="lg:col-span-2 space-y-6">
            {/* Medicine Summary */}
            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-xl font-bold text-secondary mb-4">Order Summary</h2>
              <div className="flex items-center space-x-4">
                <div className="w-20 h-20 bg-gray-100 rounded-lg flex items-center justify-center">
                  <span className="text-2xl">💊</span>
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold text-lg">{medicine.name}</h3>
                  <p className="text-gray-600">{medicine.category}</p>
                  <p className="text-primary font-semibold">{medicine.price} XAF × {quantity}</p>
                </div>
              </div>
            </div>

            {/* Delivery Information */}
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="bg-white rounded-xl shadow-md p-6">
                <h2 className="text-xl font-bold text-secondary mb-4 flex items-center space-x-2">
                  <MapPin size={24} />
                  <span>Delivery Information</span>
                </h2>
                
                <div className="space-y-4">
                  <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
                    <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                      <div className="flex-1">
                        <label className="block text-sm font-medium text-gray-700 mb-1">Saved Addresses</label>
                        <div className="flex gap-2">
                          <select
                            value={selectedAddressId || ''}
                            onChange={(e) => handleSelectAddress(e.target.value || null)}
                            className="input-field"
                          >
                            <option value="">Select an address</option>
                            {addresses.map(a => (
                              <option key={a.id} value={a.id}>{a.name} — {a.street}, {a.city}</option>
                            ))}
                          </select>
                        </div>
                      </div>
                      <div className="flex gap-2">
                        <button type="button" onClick={startAddAddress} className="btn-primary whitespace-nowrap">Add</button>
                        <button type="button" onClick={startEditAddress} disabled={!selectedAddressId} className={`px-4 py-2 rounded-lg border ${selectedAddressId ? 'border-primary text-primary hover:bg-primary/5' : 'border-gray-200 text-gray-400 cursor-not-allowed'}`}>Edit</button>
                        <button type="button" onClick={handleDeleteAddress} disabled={!selectedAddressId} className={`px-4 py-2 rounded-lg border ${selectedAddressId ? 'border-red-300 text-red-600 hover:bg-red-50' : 'border-gray-200 text-gray-400 cursor-not-allowed'}`}>Delete</button>
                      </div>
                    </div>

                    {isEditingAddress && (
                      <div className="mt-4 grid grid-cols-1 md:grid-cols-4 gap-3">
                        <input name="name" value={addressEditor.name} onChange={handleAddressEditorChange} placeholder="Name (Home, Office)" className="input-field" />
                        <input name="street" value={addressEditor.street} onChange={handleAddressEditorChange} placeholder="Street / Address" className="input-field" />
                        <input name="city" value={addressEditor.city} onChange={handleAddressEditorChange} placeholder="City" className="input-field" />
                        <input name="contact" value={addressEditor.contact} onChange={handleAddressEditorChange} placeholder="Contact Number" className="input-field" />
                        <div className="md:col-span-4 flex justify-end gap-2">
                          <button type="button" onClick={() => setIsEditingAddress(false)} className="px-4 py-2 rounded-lg border border-gray-300">Cancel</button>
                          <button type="button" onClick={commitAddressEditor} className="btn-primary">Save</button>
                        </div>
                      </div>
                    )}
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Delivery Address *
                    </label>
                    <input
                      type="text"
                      name="deliveryAddress"
                      value={formData.deliveryAddress}
                      onChange={handleChange}
                      placeholder="Enter your full address"
                      className={`input-field ${errors.deliveryAddress ? 'border-red-500' : ''}`}
                    />
                    {errors.deliveryAddress && (
                      <p className="mt-1 text-sm text-red-500">{errors.deliveryAddress}</p>
                    )}
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        City *
                      </label>
                      <input
                        type="text"
                        name="city"
                        value={formData.city}
                        onChange={handleChange}
                        placeholder="Enter city"
                        className={`input-field ${errors.city ? 'border-red-500' : ''}`}
                      />
                      {errors.city && (
                        <p className="mt-1 text-sm text-red-500">{errors.city}</p>
                      )}
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Phone Number *
                      </label>
                      <input
                        type="tel"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        placeholder="Enter phone number"
                        className={`input-field ${errors.phone ? 'border-red-500' : ''}`}
                      />
                      {errors.phone && (
                        <p className="mt-1 text-sm text-red-500">{errors.phone}</p>
                      )}
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Additional Notes
                    </label>
                    <textarea
                      name="notes"
                      value={formData.notes}
                      onChange={handleChange}
                      placeholder="Any special instructions for delivery"
                      rows={3}
                      className="input-field"
                    />
                  </div>
                </div>
              </div>

              {/* Pharmacy Selection */}
              <div className="bg-white rounded-xl shadow-md p-6">
                <h2 className="text-xl font-bold text-secondary mb-4">Select Pharmacy</h2>
                <div className="space-y-3">
                  {mockPharmacies.map(pharmacy => (
                    <label
                      key={pharmacy.id}
                      className={`block p-4 border-2 rounded-lg cursor-pointer transition-colors ${
                        selectedPharmacy === pharmacy.id
                          ? 'border-primary bg-primary/5'
                          : 'border-gray-200 hover:border-primary/50'
                      }`}
                    >
                      <input
                        type="radio"
                        name="pharmacy"
                        value={pharmacy.id}
                        checked={selectedPharmacy === pharmacy.id}
                        onChange={() => {
                          setSelectedPharmacy(pharmacy.id);
                          setErrors(prev => ({ ...prev, pharmacy: '' }));
                        }}
                        className="sr-only"
                      />
                      <div className="flex justify-between items-start">
                        <div>
                          <h3 className="font-semibold text-gray-900">{pharmacy.name}</h3>
                          <p className="text-sm text-gray-600">{pharmacy.address}</p>
                          <p className="text-sm text-gray-600">{pharmacy.phone}</p>
                        </div>
                        <div className="text-right">
                          <p className="text-sm font-medium text-primary">{pharmacy.distance}</p>
                          <p className="text-sm text-gray-600">⭐ {pharmacy.rating}</p>
                        </div>
                      </div>
                    </label>
                  ))}
                </div>
                {errors.pharmacy && (
                  <p className="mt-2 text-sm text-red-500">{errors.pharmacy}</p>
                )}
              </div>

              {/* Prescription Upload */}
              {medicine.requiresPrescription && (
                <div className="bg-white rounded-xl shadow-md p-6">
                  <h2 className="text-xl font-bold text-secondary mb-4 flex items-center space-x-2">
                    <Upload size={24} />
                    <span>Upload Prescription *</span>
                  </h2>
                  <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
                    <Upload className="mx-auto text-gray-400 mb-2" size={48} />
                    <label className="cursor-pointer">
                      <span className="text-primary hover:text-primary-dark font-medium">
                        Click to upload
                      </span>
                      <input
                        type="file"
                        accept="image/*,.pdf"
                        onChange={handleFileChange}
                        className="hidden"
                      />
                    </label>
                    <p className="text-sm text-gray-500 mt-1">
                      PNG, JPG or PDF (max. 5MB)
                    </p>
                    {prescriptionFile && (
                      <p className="mt-2 text-sm text-green-600 flex items-center justify-center space-x-1">
                        <CheckCircle size={16} />
                        <span>{prescriptionFile.name}</span>
                      </p>
                    )}
                  </div>
                  {errors.prescription && (
                    <p className="mt-2 text-sm text-red-500">{errors.prescription}</p>
                  )}
                </div>
              )}

              {/* Payment Method */}
              <div className="bg-white rounded-xl shadow-md p-6">
                <h2 className="text-xl font-bold text-secondary mb-4 flex items-center space-x-2">
                  <CreditCard size={24} />
                  <span>Payment Method</span>
                </h2>
                <div className="space-y-3">
                  <label className="flex items-center space-x-3 p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-primary/50 transition-colors">
                    <input
                      type="radio"
                      name="paymentMethod"
                      value="cash"
                      checked={formData.paymentMethod === 'cash'}
                      onChange={handleChange}
                      className="w-4 h-4 text-primary"
                    />
                    <span className="font-medium">Cash on Delivery</span>
                  </label>
                  <label className="flex items-center space-x-3 p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-primary/50 transition-colors">
                    <input
                      type="radio"
                      name="paymentMethod"
                      value="card"
                      checked={formData.paymentMethod === 'card'}
                      onChange={handleChange}
                      className="w-4 h-4 text-primary"
                    />
                    <span className="font-medium">Mobile Money</span>
                  </label>
                </div>
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="btn-primary w-full"
              >
                {isSubmitting ? 'Processing...' : `Place Order - ${totalPrice} XAF`}
              </button>
            </form>
          </div>

          {/* Order Summary Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-xl shadow-md p-6 sticky top-24">
              <h2 className="text-xl font-bold text-secondary mb-4">Price Details</h2>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-600">Price ({quantity} item{quantity > 1 ? 's' : ''})</span>
                  <span className="font-semibold">{totalPrice} XAF</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Delivery Fee</span>
                  <span className="font-semibold text-green-600">FREE</span>
                </div>
                <div className="border-t pt-3 flex justify-between">
                  <span className="font-bold text-lg">Total Amount</span>
                  <span className="font-bold text-lg text-primary">{totalPrice} XAF</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Order;
