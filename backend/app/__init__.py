"""
Medi-Reach Backend Application Factory
Initializes Flask app with all extensions and blueprints
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import get_config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_name='default'):
    """
    Application factory pattern
    Creates and configures the Flask application
    
    Args:
        config_name (str): Configuration environment name
        
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    config_class = get_config()
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={
        r"/api/*": {
            "origins": app.config['CORS_ORIGINS'],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Create instance folder if it doesn't exist
    import os
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register blueprints
    from app.auth import auth_bp
    from app.medicine_routes import medicine_bp
    from app.order_routes import order_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(medicine_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')
    
    # Root route
    @app.route('/')
    def index():
        """API root endpoint"""
        return jsonify({
            'message': 'Welcome to Medi-Reach API',
            'version': '1.0.0',
            'status': 'running',
            'endpoints': {
                'auth': '/api/signup, /api/login',
                'medicines': '/api/medicines',
                'orders': '/api/orders'
            }
        }), 200
    
    # Health check endpoint
    @app.route('/health')
    def health():
        """Health check endpoint"""
        return jsonify({'status': 'healthy'}), 200
    
    # Global error handlers
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        db.session.rollback()
        return jsonify({'error': 'Internal server error'}), 500
    
    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """Handle expired JWT tokens"""
        return jsonify({'error': 'Token has expired'}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        """Handle invalid JWT tokens"""
        return jsonify({'error': 'Invalid token'}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        """Handle missing JWT tokens"""
        return jsonify({'error': 'Authorization token is missing'}), 401
    
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Seed initial data if database is empty
        from app.utils import seed_database
        seed_database()
    
    return app
