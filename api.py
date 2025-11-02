from flask import Blueprint, jsonify, request
from db import get_db_connection

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/medicines")
def get_medicines():
    """Return all medicines as JSON."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM medicines")
    rows = cursor.fetchall()
    conn.close()

    medicines = [dict(row) for row in rows]
    return jsonify({"count": len(medicines), "medicines": medicines})


@api_bp.route("/api/medicines/create", methods=["POST"])
def add_medicine():
    """Add a new medicine to the database with validation."""
    data = request.get_json()

    # Validate input
    name = data.get("name")
    price = data.get("price")

    if not name or not isinstance(name, str) or name.strip() == "":
        return jsonify({"error": "Medicine name must be a non-empty string"}), 400

    if price is None:
        return jsonify({"error": "Price is required"}), 400

    try:
        price = float(price)
        if price <= 0:
            return jsonify({"error": "Price must be greater than 0"}), 400
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400

    # Insert into database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO medicines (name, price) VALUES (?, ?)", (name.strip(), price)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return (
        jsonify(
            {
                "message": "Medicine added successfully",
                "id": new_id,
                "name": name.strip(),
                "price": price,
            }
        ),
        201,
    )
