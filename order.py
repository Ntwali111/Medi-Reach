from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db import get_db_connection

order_bp = Blueprint("order", __name__)


@order_bp.route("/order")
def order():
    """Display order form with available medicines."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM medicines ORDER BY name")
    medicines = [dict(row) for row in cursor.fetchall()]
    conn.close()

    user_id = session.get("user_id")
    user_name = session.get("user_name", "")

    return render_template("order.html", medicines=medicines, user_name=user_name)


@order_bp.route("/order/submit", methods=["POST"])
def submit_order():
    """Handle order submission and store in database."""
    try:
        medicine_id = request.form.get("medicine_id")
        quantity = request.form.get("quantity", "1")
        delivery_address = request.form.get("address", "").strip()
        customer_name = request.form.get("customer_name", "").strip()

        if not medicine_id:
            flash("Please select a medicine!", "error")
            return redirect(url_for("order.order"))

        if not delivery_address:
            flash("Delivery address is required!", "error")
            return redirect(url_for("order.order"))

        if not customer_name:
            flash("Your name is required!", "error")
            return redirect(url_for("order.order"))

        try:
            medicine_id = int(medicine_id)
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
        except ValueError:
            flash("Invalid quantity!", "error")
            return redirect(url_for("order.order"))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, price FROM medicines WHERE id = ?", (medicine_id,))
        medicine = cursor.fetchone()

        if not medicine:
            conn.close()
            flash("Medicine not found!", "error")
            return redirect(url_for("order.order"))

        total_price = float(medicine["price"]) * quantity
        user_id = session.get("user_id")

        cursor.execute(
            """
            INSERT INTO orders (user_id, medicine_id, medicine_name, quantity, total_price, delivery_address, customer_name, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
        """,
            (
                user_id,
                medicine_id,
                medicine["name"],
                quantity,
                total_price,
                delivery_address,
                customer_name,
            ),
        )

        order_id = cursor.lastrowid
        conn.commit()
        conn.close()

        flash("Order placed successfully!", "success")
        return redirect(url_for("order.confirm_order", order_id=order_id))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("order.order"))


@order_bp.route("/order/confirm/<int:order_id>")
def confirm_order(order_id):
    """Display order confirmation."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, medicine_name, quantity, total_price, delivery_address, customer_name, status, created_at
        FROM orders WHERE id = ?
    """,
        (order_id,),
    )
    order = cursor.fetchone()
    conn.close()

    if not order:
        flash("Order not found!", "error")
        return redirect(url_for("order.order"))

    return render_template("order_confirm.html", order=dict(order))

