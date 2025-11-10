"""
Order management routes for Medi-Reach
Handles order placement, tracking, and status updates
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Order, Medicine, User
from app.utils import admin_required, generate_order_number
from datetime import datetime, timedelta

order_bp = Blueprint('orders', __name__)


@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    """
    Place a new order
    
    Request Body:
        - medicine_id (int): Medicine ID
        - quantity (int): Order quantity
        - delivery_address (str): Delivery address
        - city (str): City
        - phone (str): Contact phone number
        - pharmacy_name (str, optional): Selected pharmacy
        - payment_method (str, optional): Payment method
        - notes (str, optional): Additional notes
        - prescription_url (str, optional): Prescription file URL (if required)
    
    Returns:
        JSON response with created order data
    """
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['medicine_id', 'quantity', 'delivery_address', 'city', 'phone']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Get medicine
        medicine = Medicine.query.get(data['medicine_id'])
        if not medicine:
            return jsonify({'error': 'Medicine not found'}), 404
        
        # Validate quantity
        try:
            quantity = int(data['quantity'])
        except ValueError:
            return jsonify({'error': 'Invalid quantity'}), 400
        
        if quantity <= 0:
            return jsonify({'error': 'Quantity must be greater than 0'}), 400
        
        # Check stock availability
        if medicine.stock < quantity:
            return jsonify({'error': f'Insufficient stock. Only {medicine.stock} units available'}), 400
        
        # Check prescription requirement
        if medicine.requires_prescription and not data.get('prescription_url'):
            return jsonify({'error': 'Prescription is required for this medicine'}), 400
        
        # Calculate total price
        total_price = medicine.price * quantity
        
        # Create order
        order = Order(
            order_number=generate_order_number(),
            user_id=current_user_id,
            medicine_id=medicine.id,
            quantity=quantity,
            total_price=total_price,
            delivery_address=data['delivery_address'].strip(),
            city=data['city'].strip(),
            phone=data['phone'].strip(),
            pharmacy_name=data.get('pharmacy_name'),
            payment_method=data.get('payment_method', 'Cash on Delivery'),
            notes=data.get('notes'),
            prescription_url=data.get('prescription_url'),
            status='Pending',
            estimated_delivery=datetime.utcnow() + timedelta(days=3)
        )
        
        # Update medicine stock
        medicine.stock -= quantity
        
        db.session.add(order)
        db.session.commit()
        
        return jsonify({
            'message': 'Order placed successfully',
            'order': order.to_dict(include_medicine=True)
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create order: {str(e)}'}), 500


@order_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_user_orders():
    """
    Get all orders for the authenticated user
    
    Query Parameters:
        - status (str): Filter by order status
        - page (int): Page number (default: 1)
        - per_page (int): Items per page (default: 20)
    
    Returns:
        JSON response with list of orders
    """
    try:
        current_user_id = get_jwt_identity()
        
        # Get query parameters
        status = request.args.get('status', type=str)
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # Build query
        query = Order.query.filter_by(user_id=current_user_id)
        
        # Apply status filter
        if status:
            query = query.filter_by(status=status)
        
        # Order by creation date (newest first)
        query = query.order_by(Order.created_at.desc())
        
        # Paginate
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        orders = pagination.items
        
        return jsonify({
            'orders': [order.to_dict(include_medicine=True) for order in orders],
            'total': pagination.total,
            'page': page,
            'per_page': per_page,
            'pages': pagination.pages
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch orders: {str(e)}'}), 500


@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    """
    Get a single order by ID
    
    Args:
        order_id (int): Order ID
    
    Returns:
        JSON response with order data
    """
    try:
        current_user_id = get_jwt_identity()
        order = Order.query.get(order_id)
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        # Check if user owns this order or is admin
        user = User.query.get(current_user_id)
        if order.user_id != current_user_id and not user.is_admin:
            return jsonify({'error': 'Unauthorized access to this order'}), 403
        
        return jsonify({
            'order': order.to_dict(include_user=True, include_medicine=True)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch order: {str(e)}'}), 500


@order_bp.route('/orders/track/<order_number>', methods=['GET'])
def track_order(order_number):
    """
    Track an order by order number (public endpoint)
    
    Args:
        order_number (str): Order number
    
    Returns:
        JSON response with order tracking information
    """
    try:
        order = Order.query.filter_by(order_number=order_number.upper()).first()
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        return jsonify({
            'order': order.to_dict(include_medicine=True)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to track order: {str(e)}'}), 500


@order_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
@jwt_required()
@admin_required
def update_order_status(order_id):
    """
    Update order status (Admin only)
    
    Args:
        order_id (int): Order ID
    
    Request Body:
        - status (str): New order status
    
    Returns:
        JSON response with updated order data
    """
    try:
        order = Order.query.get(order_id)
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        data = request.get_json()
        
        if not data or 'status' not in data:
            return jsonify({'error': 'Status is required'}), 400
        
        new_status = data['status']
        
        # Validate status
        valid_statuses = ['Pending', 'Processing', 'Confirmed', 'In Transit', 'Delivered', 'Cancelled']
        if new_status not in valid_statuses:
            return jsonify({'error': f'Invalid status. Must be one of: {", ".join(valid_statuses)}'}), 400
        
        # Update status
        order.status = new_status
        
        # Set delivery date if status is Delivered
        if new_status == 'Delivered' and not order.delivered_at:
            order.delivered_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': 'Order status updated successfully',
            'order': order.to_dict(include_medicine=True)
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update order status: {str(e)}'}), 500


@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@jwt_required()
def cancel_order(order_id):
    """
    Cancel an order (user can only cancel their own pending orders)
    
    Args:
        order_id (int): Order ID
    
    Returns:
        JSON response confirming cancellation
    """
    try:
        current_user_id = get_jwt_identity()
        order = Order.query.get(order_id)
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        # Check ownership
        if order.user_id != current_user_id:
            return jsonify({'error': 'Unauthorized to cancel this order'}), 403
        
        # Only pending orders can be cancelled
        if order.status != 'Pending':
            return jsonify({'error': 'Only pending orders can be cancelled'}), 400
        
        # Restore medicine stock
        medicine = Medicine.query.get(order.medicine_id)
        if medicine:
            medicine.stock += order.quantity
        
        # Update order status
        order.status = 'Cancelled'
        
        db.session.commit()
        
        return jsonify({
            'message': 'Order cancelled successfully',
            'order': order.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to cancel order: {str(e)}'}), 500


@order_bp.route('/orders/all', methods=['GET'])
@jwt_required()
@admin_required
def get_all_orders():
    """
    Get all orders in the system (Admin only)
    
    Query Parameters:
        - status (str): Filter by status
        - page (int): Page number
        - per_page (int): Items per page
    
    Returns:
        JSON response with all orders
    """
    try:
        # Get query parameters
        status = request.args.get('status', type=str)
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # Build query
        query = Order.query
        
        if status:
            query = query.filter_by(status=status)
        
        # Order by creation date
        query = query.order_by(Order.created_at.desc())
        
        # Paginate
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        orders = pagination.items
        
        return jsonify({
            'orders': [order.to_dict(include_user=True, include_medicine=True) for order in orders],
            'total': pagination.total,
            'page': page,
            'per_page': per_page,
            'pages': pagination.pages
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch orders: {str(e)}'}), 500


@order_bp.route('/orders/stats', methods=['GET'])
@jwt_required()
@admin_required
def get_order_stats():
    """
    Get order statistics (Admin only)
    
    Returns:
        JSON response with order statistics
    """
    try:
        total_orders = Order.query.count()
        pending_orders = Order.query.filter_by(status='Pending').count()
        processing_orders = Order.query.filter_by(status='Processing').count()
        delivered_orders = Order.query.filter_by(status='Delivered').count()
        cancelled_orders = Order.query.filter_by(status='Cancelled').count()
        
        # Calculate total revenue (delivered orders only)
        delivered = Order.query.filter_by(status='Delivered').all()
        total_revenue = sum(order.total_price for order in delivered)
        
        return jsonify({
            'total_orders': total_orders,
            'pending': pending_orders,
            'processing': processing_orders,
            'delivered': delivered_orders,
            'cancelled': cancelled_orders,
            'total_revenue': total_revenue
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch statistics: {str(e)}'}), 500
