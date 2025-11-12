
from flask import Flask, url_for, render_template, request
from api import api_bp
from db import init_medicine_table, init_orders_table, seed_medicines
from auth import auth_bp
from order import order_bp

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(order_bp)

# Initialize DB and seed medicines
init_medicine_table()
init_orders_table()
seed_medicines()

@app.route("/", endpoint="home")
def home():
    return render_template("index.html")

@app.route("/medicines")
def medicines():
    return render_template("medicines.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/track", methods=["GET"])
def track():
    order_id = request.args.get("order_id", "")
    status = None
    if order_id:
        # Mock status logic
        status = "Out for delivery" if order_id == "123" else "Order not found. Try 123."
    return render_template("track.html", order_id=order_id, status=status)

if __name__ == "__main__":
    app.run(debug=True)
