from flask import Flask, url_for, render_template
from api import api_bp
from db import init_medicine_table, seed_medicines
from auth import auth_bp

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)

# Initialize DB and seed medicines
init_medicine_table()
seed_medicines()

def nav():
    return (
        f'<nav style="display:flex;gap:12px;padding:12px 0;">'
        f'<a href="{url_for("home")}">Home</a>'
        f'<a href="{url_for("medicines")}">Medicines</a>'
        f'<a href="{url_for("order")}">Order</a>'
        f'</nav><hr/>'
    )

@app.route("/", endpoint="home")
def home():
    return (
        nav()
        + "<h1>Medi-Reach</h1>"
        + "<p>Welcome. Use the navigation to browse medicines or place an order.</p>"
    )

@app.route("/medicines")
def medicines():
    return render_template("medicines.html")


@app.route("/contact")
def contact():
    return nav() + "<h1>Place an Order</h1><p>Ordering UI will be implemented by teammates.</p>"

@app.route("/order")
def order():
    return nav() + "<h1>Place an Order</h1><p>Ordering UI will be implemented by teammates.</p>"

if __name__ == "__main__":
    app.run(debug=True)
