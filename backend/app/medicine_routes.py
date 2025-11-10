"""
Medicine management routes for Medi-Reach
Handles CRUD operations for medicines
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Medicine, User
from app.utils import admin_required

medicine_bp = Blueprint('medicines', __name__)


@medicine_bp.route('/medicines', methods=['GET'])
def get_medicines():
    """
    Get all medicines with optional filtering and pagination
    
    Query Parameters:
        - page (int): Page number (default: 1)
        - per_page (int): Items per page (default: 20)
        - category (str): Filter by category
        - search (str): Search in name and description
        - requires_prescription (bool): Filter by prescription requirement
    
    Returns:
        JSON response with list of medicines
    """
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        category = request.args.get('category', type=str)
        search = request.args.get('search', type=str)
        requires_prescription = request.args.get('requires_prescription', type=str)
        
        # Build query
        query = Medicine.query
        
        # Apply filters
        if category:
            query = query.filter(Medicine.category.ilike(f'%{category}%'))
        
        if search:
            search_filter = f'%{search}%'
            query = query.filter(
                db.or_(
                    Medicine.name.ilike(search_filter),
                    Medicine.description.ilike(search_filter)
                )
            )
        
        if requires_prescription is not None:
            req_prescription = requires_prescription.lower() == 'true'
            query = query.filter(Medicine.requires_prescription == req_prescription)
        
        # Paginate results
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        medicines = pagination.items
        
        return jsonify({
            'medicines': [medicine.to_dict() for medicine in medicines],
            'total': pagination.total,
            'page': page,
            'per_page': per_page,
            'pages': pagination.pages
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch medicines: {str(e)}'}), 500


@medicine_bp.route('/medicines/<int:medicine_id>', methods=['GET'])
def get_medicine(medicine_id):
    """
    Get a single medicine by ID
    
    Args:
        medicine_id (int): Medicine ID
    
    Returns:
        JSON response with medicine data
    """
    try:
        medicine = Medicine.query.get(medicine_id)
        
        if not medicine:
            return jsonify({'error': 'Medicine not found'}), 404
        
        return jsonify({
            'medicine': medicine.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch medicine: {str(e)}'}), 500


@medicine_bp.route('/medicines', methods=['POST'])
@jwt_required()
@admin_required
def create_medicine():
    """
    Create a new medicine (Admin only)
    
    Request Body:
        - name (str): Medicine name
        - category (str): Medicine category
        - description (str): Medicine description
        - price (float): Medicine price
        - stock (int): Available stock
        - dosage (str, optional): Dosage information
        - side_effects (str, optional): Side effects
        - manufacturer (str, optional): Manufacturer name
        - requires_prescription (bool, optional): Prescription requirement
        - image_url (str, optional): Image URL
    
    Returns:
        JSON response with created medicine data
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'category', 'description', 'price', 'stock']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Validate data types
        try:
            price = float(data['price'])
            stock = int(data['stock'])
        except ValueError:
            return jsonify({'error': 'Invalid price or stock value'}), 400
        
        if price <= 0:
            return jsonify({'error': 'Price must be greater than 0'}), 400
        
        if stock < 0:
            return jsonify({'error': 'Stock cannot be negative'}), 400
        
        # Create medicine
        medicine = Medicine(
            name=data['name'].strip(),
            category=data['category'].strip(),
            description=data['description'].strip(),
            price=price,
            stock=stock,
            dosage=data.get('dosage'),
            side_effects=data.get('side_effects'),
            manufacturer=data.get('manufacturer'),
            requires_prescription=data.get('requires_prescription', False),
            image_url=data.get('image_url')
        )
        
        db.session.add(medicine)
        db.session.commit()
        
        return jsonify({
            'message': 'Medicine created successfully',
            'medicine': medicine.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create medicine: {str(e)}'}), 500


@medicine_bp.route('/medicines/<int:medicine_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_medicine(medicine_id):
    """
    Update an existing medicine (Admin only)
    
    Args:
        medicine_id (int): Medicine ID
    
    Request Body:
        Any medicine fields to update
    
    Returns:
        JSON response with updated medicine data
    """
    try:
        medicine = Medicine.query.get(medicine_id)
        
        if not medicine:
            return jsonify({'error': 'Medicine not found'}), 404
        
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update fields
        if 'name' in data:
            medicine.name = data['name'].strip()
        if 'category' in data:
            medicine.category = data['category'].strip()
        if 'description' in data:
            medicine.description = data['description'].strip()
        if 'price' in data:
            try:
                price = float(data['price'])
                if price <= 0:
                    return jsonify({'error': 'Price must be greater than 0'}), 400
                medicine.price = price
            except ValueError:
                return jsonify({'error': 'Invalid price value'}), 400
        if 'stock' in data:
            try:
                stock = int(data['stock'])
                if stock < 0:
                    return jsonify({'error': 'Stock cannot be negative'}), 400
                medicine.stock = stock
            except ValueError:
                return jsonify({'error': 'Invalid stock value'}), 400
        if 'dosage' in data:
            medicine.dosage = data['dosage']
        if 'side_effects' in data:
            medicine.side_effects = data['side_effects']
        if 'manufacturer' in data:
            medicine.manufacturer = data['manufacturer']
        if 'requires_prescription' in data:
            medicine.requires_prescription = data['requires_prescription']
        if 'image_url' in data:
            medicine.image_url = data['image_url']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Medicine updated successfully',
            'medicine': medicine.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update medicine: {str(e)}'}), 500


@medicine_bp.route('/medicines/<int:medicine_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_medicine(medicine_id):
    """
    Delete a medicine (Admin only)
    
    Args:
        medicine_id (int): Medicine ID
    
    Returns:
        JSON response confirming deletion
    """
    try:
        medicine = Medicine.query.get(medicine_id)
        
        if not medicine:
            return jsonify({'error': 'Medicine not found'}), 404
        
        db.session.delete(medicine)
        db.session.commit()
        
        return jsonify({
            'message': 'Medicine deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete medicine: {str(e)}'}), 500


@medicine_bp.route('/medicines/categories', methods=['GET'])
def get_categories():
    """
    Get all unique medicine categories
    
    Returns:
        JSON response with list of categories
    """
    try:
        categories = db.session.query(Medicine.category).distinct().all()
        category_list = [cat[0] for cat in categories if cat[0]]
        
        return jsonify({
            'categories': sorted(category_list)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch categories: {str(e)}'}), 500
