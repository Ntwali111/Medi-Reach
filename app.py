from flask import Flask, url_for, render_template, request

app = Flask(__name__)

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
    return nav() + "<h1>Medicines</h1><p>List will be displayed by frontend/data endpoints.</p>"

@app.route("/order")
def order():
    return nav() + "<h1>Place an Order</h1><p>Ordering UI will be implemented by teammates.</p>"

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
