import { useState, useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';
import { Search, Package, Truck, CheckCircle, Clock, MapPin, Phone } from 'lucide-react';
import { mockOrders, orderStatuses } from '../data/mockData';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const Track = () => {
  const location = useLocation();
  const [orderId, setOrderId] = useState('');
  const [order, setOrder] = useState(null);
  const [isSearching, setIsSearching] = useState(false);
  const [error, setError] = useState('');
  const [showSuccess, setShowSuccess] = useState(false);
  const mapRef = useRef(null);
  const driverMarkerRef = useRef(null);
  const routeLineRef = useRef(null);
  const [mapReady, setMapReady] = useState(false);

  useEffect(() => {
    if (location.state?.orderId) {
      setOrderId(location.state.orderId);
      if (location.state?.success) {
        setShowSuccess(true);
        setTimeout(() => setShowSuccess(false), 5000);
      }
    }
  }, [location.state]);

  const handleSearch = (e) => {
    e.preventDefault();
    setError('');
    setOrder(null);

    if (!orderId.trim()) {
      setError('Please enter an order ID');
      return;
    }

    setIsSearching(true);

    // Simulate API call
    setTimeout(() => {
      const found = mockOrders.find(o => o.id === orderId.toUpperCase());
      if (found) {
        setOrder(found);
      } else {
        setError('Order not found. Please check your order ID and try again.');
      }
      setIsSearching(false);
    }, 800);
  };

  const getStatusSteps = (currentStatus) => {
    const steps = [
      { key: 'pending', label: 'Order Placed', icon: Package },
      { key: 'processing', label: 'Processing', icon: Clock },
      { key: 'confirmed', label: 'Confirmed', icon: CheckCircle },
      { key: 'in_transit', label: 'In Transit', icon: Truck },
      { key: 'delivered', label: 'Delivered', icon: CheckCircle },
    ];

    const statusOrder = ['pending', 'processing', 'confirmed', 'in_transit', 'delivered'];
    const currentIndex = statusOrder.indexOf(currentStatus);

    return steps.map((step, index) => ({
      ...step,
      completed: index <= currentIndex,
      active: index === currentIndex,
    }));
  };

  useEffect(() => {
    if (!order) return;

    const getSavedOrderAddress = (id) => {
      try {
        const map = JSON.parse(localStorage.getItem('mr_order_address_map') || '{}');
        return map[id] || null;
      } catch {
        return null;
      }
    };

    const pickCityFromText = (text) => {
      const t = (text || '').toLowerCase();
      if (t.includes('yaounde')) return 'Yaounde';
      if (t.includes('douala')) return 'Douala';
      if (t.includes('bamenda')) return 'Bamenda';
      return '';
    };

    const cityToLatLng = (city) => {
      switch ((city || '').toLowerCase()) {
        case 'yaounde':
          return [3.848, 11.502];
        case 'douala':
          return [4.051, 9.768];
        case 'bamenda':
          return [5.959, 10.145];
        default:
          return [3.848, 11.502];
      }
    };

    const sel = getSavedOrderAddress(order.id);
    const addressText = sel?.street || order.deliveryAddress || '';
    const cityText = sel?.city || pickCityFromText(order.deliveryAddress) || '';
    const userPos = cityToLatLng(cityText);

    let map = mapRef.current;
    if (!map) {
      map = L.map('orderMap').setView(userPos, 13);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap'
      }).addTo(map);
      mapRef.current = map;
      setMapReady(true);
    } else {
      map.setView(userPos, 13);
      if (driverMarkerRef.current) {
        map.removeLayer(driverMarkerRef.current);
        driverMarkerRef.current = null;
      }
      if (routeLineRef.current) {
        map.removeLayer(routeLineRef.current);
        routeLineRef.current = null;
      }
    }

    const userMarker = L.circleMarker(userPos, { radius: 8, color: '#22c55e', fillColor: '#22c55e', fillOpacity: 0.8 }).addTo(map);
    userMarker.bindPopup(`${addressText || 'Delivery Address'}${cityText ? ', ' + cityText : ''}`);

    let driverPos = [userPos[0] + 0.02, userPos[1] - 0.02];
    driverMarkerRef.current = L.circleMarker(driverPos, { radius: 8, color: '#3b82f6', fillColor: '#3b82f6', fillOpacity: 0.8 }).addTo(map);
    driverMarkerRef.current.bindPopup('Driver');

    routeLineRef.current = L.polyline([driverPos, userPos], { color: '#9333ea', weight: 4, opacity: 0.8 }).addTo(map);

    const moveInterval = setInterval(() => {
      const step = 0.2;
      const latDiff = userPos[0] - driverPos[0];
      const lngDiff = userPos[1] - driverPos[1];
      const dist = Math.sqrt(latDiff * latDiff + lngDiff * lngDiff);
      if (dist < 0.0005) return;
      const unitLat = latDiff / dist;
      const unitLng = lngDiff / dist;
      driverPos = [driverPos[0] + unitLat * 0.001 * step, driverPos[1] + unitLng * 0.001 * step];
      if (driverMarkerRef.current) driverMarkerRef.current.setLatLng(driverPos);
      if (routeLineRef.current) routeLineRef.current.setLatLngs([driverPos, userPos]);
    }, 3000);

    return () => {
      clearInterval(moveInterval);
      if (mapRef.current) {
        if (driverMarkerRef.current) {
          mapRef.current.removeLayer(driverMarkerRef.current);
          driverMarkerRef.current = null;
        }
        if (routeLineRef.current) {
          mapRef.current.removeLayer(routeLineRef.current);
          routeLineRef.current = null;
        }
      }
    };
  }, [order]);

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Success Message */}
        {showSuccess && (
          <div className="mb-6 bg-green-50 border border-green-200 rounded-lg p-4 flex items-start space-x-3">
            <CheckCircle className="text-green-600 flex-shrink-0 mt-0.5" size={24} />
            <div>
              <h3 className="font-semibold text-green-800">Order Placed Successfully!</h3>
              <p className="text-sm text-green-700 mt-1">
                Your order has been placed. Use the order ID below to track your delivery.
              </p>
            </div>
          </div>
        )}

        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-secondary mb-4">
            Track Your Order
          </h1>
          <p className="text-gray-600">
            Enter your order ID to check the delivery status
          </p>
        </div>

        {/* Search Form */}
        <div className="bg-white rounded-xl shadow-md p-6 mb-8">
          <form onSubmit={handleSearch}>
            <div className="flex flex-col sm:flex-row gap-4">
              <div className="flex-1">
                <input
                  type="text"
                  placeholder="Enter Order ID (e.g., ORD-001)"
                  value={orderId}
                  onChange={(e) => {
                    setOrderId(e.target.value);
                    setError('');
                  }}
                  className="input-field"
                />
              </div>
              <button
                type="submit"
                disabled={isSearching}
                className="btn-primary flex items-center justify-center space-x-2 sm:w-auto"
              >
                <Search size={20} />
                <span>{isSearching ? 'Searching...' : 'Track Order'}</span>
              </button>
            </div>
          </form>

          {error && (
            <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-sm text-red-700">{error}</p>
            </div>
          )}
        </div>

        {/* Order Details */}
        {order && (
          <div className="space-y-6">
            {/* Order Info Card */}
            <div className="bg-white rounded-xl shadow-md p-6">
              <div className="flex justify-between items-start mb-6">
                <div>
                  <h2 className="text-2xl font-bold text-secondary mb-1">Order #{order.id}</h2>
                  <p className="text-gray-600">Placed on {new Date(order.orderDate).toLocaleDateString()}</p>
                </div>
                <span className={`px-4 py-2 rounded-full text-white font-medium ${orderStatuses[order.status].color}`}>
                  {orderStatuses[order.status].label}
                </span>
              </div>

              {/* Medicine Details */}
              <div className="border-t border-b py-4 mb-4">
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gray-100 rounded-lg flex items-center justify-center">
                    <span className="text-2xl">💊</span>
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-lg">{order.medicineName}</h3>
                    <p className="text-gray-600">Quantity: {order.quantity}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-2xl font-bold text-primary">{order.totalPrice} XAF</p>
                  </div>
                </div>
              </div>

              {/* Delivery Info */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="flex items-start space-x-3">
                  <MapPin className="text-primary flex-shrink-0 mt-1" size={20} />
                  <div>
                    <p className="font-semibold text-gray-700">Delivery Address</p>
                    <p className="text-gray-600 text-sm">{order.deliveryAddress}</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <Package className="text-primary flex-shrink-0 mt-1" size={20} />
                  <div>
                    <p className="font-semibold text-gray-700">Pharmacy</p>
                    <p className="text-gray-600 text-sm">{order.pharmacy}</p>
                  </div>
                </div>
              </div>

              {order.estimatedDelivery && (
                <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                  <p className="text-sm text-blue-800">
                    <span className="font-semibold">Estimated Delivery:</span>{' '}
                    {new Date(order.estimatedDelivery).toLocaleDateString()}
                  </p>
                </div>
              )}

              {order.deliveryDate && (
                <div className="mt-4 p-4 bg-green-50 rounded-lg">
                  <p className="text-sm text-green-800">
                    <span className="font-semibold">Delivered on:</span>{' '}
                    {new Date(order.deliveryDate).toLocaleDateString()}
                  </p>
                </div>
              )}
            </div>

            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-xl font-bold text-secondary mb-4">Delivery Map</h2>
              <div id="orderMap" className="w-full h-64 md:h-80 rounded-lg"></div>
            </div>

            {/* Tracking Timeline */}
            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-xl font-bold text-secondary mb-6">Delivery Status</h2>
              
              <div className="relative">
                {getStatusSteps(order.status).map((step, index, array) => {
                  const StepIcon = step.icon;
                  return (
                    <div key={step.key} className="relative flex items-start mb-8 last:mb-0">
                      {/* Connector Line */}
                      {index < array.length - 1 && (
                        <div
                          className={`absolute left-6 top-12 w-0.5 h-full -ml-px ${
                            step.completed ? 'bg-primary' : 'bg-gray-300'
                          }`}
                        />
                      )}

                      {/* Icon */}
                      <div
                        className={`relative z-10 flex items-center justify-center w-12 h-12 rounded-full border-4 ${
                          step.completed
                            ? 'bg-primary border-primary text-white'
                            : 'bg-white border-gray-300 text-gray-400'
                        }`}
                      >
                        <StepIcon size={24} />
                      </div>

                      {/* Content */}
                      <div className="ml-4 flex-1">
                        <h3
                          className={`font-semibold ${
                            step.active ? 'text-primary' : step.completed ? 'text-gray-900' : 'text-gray-500'
                          }`}
                        >
                          {step.label}
                        </h3>
                        {step.active && (
                          <p className="text-sm text-gray-600 mt-1">
                            Your order is currently being {step.label.toLowerCase()}
                          </p>
                        )}
                        {step.completed && !step.active && (
                          <p className="text-sm text-gray-500 mt-1">Completed</p>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Contact Support */}
            <div className="bg-primary/5 border border-primary/20 rounded-xl p-6">
              <h3 className="font-semibold text-secondary mb-2">Need Help?</h3>
              <p className="text-gray-600 text-sm mb-4">
                If you have any questions about your order, please contact our support team.
              </p>
              <div className="flex flex-col sm:flex-row gap-3">
                <a
                  href="tel:+237222123456"
                  className="flex items-center justify-center space-x-2 px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors"
                >
                  <Phone size={20} />
                  <span>Call Support</span>
                </a>
                <a
                  href="mailto:support@medireach.com"
                  className="flex items-center justify-center space-x-2 px-4 py-2 border border-primary text-primary rounded-lg hover:bg-primary/5 transition-colors"
                >
                  <span>Email Support</span>
                </a>
              </div>
            </div>
          </div>
        )}

        {/* Recent Orders */}
        {!order && !error && (
          <div className="bg-white rounded-xl shadow-md p-6">
            <h2 className="text-xl font-bold text-secondary mb-4">Recent Orders</h2>
            <div className="space-y-3">
              {mockOrders.map((mockOrder) => (
                <button
                  key={mockOrder.id}
                  onClick={() => {
                    setOrderId(mockOrder.id);
                    setOrder(mockOrder);
                  }}
                  className="w-full text-left p-4 border border-gray-200 rounded-lg hover:border-primary hover:bg-primary/5 transition-colors"
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-semibold text-gray-900">{mockOrder.id}</p>
                      <p className="text-sm text-gray-600">{mockOrder.medicineName}</p>
                    </div>
                    <span className={`px-3 py-1 rounded-full text-white text-xs font-medium ${orderStatuses[mockOrder.status].color}`}>
                      {orderStatuses[mockOrder.status].label}
                    </span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Track;
