"""
Medi-Reach: Main Flask application with routing and basic database wiring.

This file defines the application entrypoint, core routes, and a minimal
SQLAlchemy model to demonstrate data access from views.

Architecture
- Routing and app setup live here (controller layer)
- HTML templates live in templates/ (view layer)
- Data model (example: Medicine) defined here for now; can be moved to a
  dedicated models.py in a later iteration (model layer)
"""

from __future__ import annotations

from typing import List

from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy


# App factory not strictly required here; use a single-module app for MVP clarity.
app = Flask(__name__, instance_relative_config=True)

# Basic configuration; move to instance config for secrets in later iterations.
app.config["SECRET_KEY"] = "dev-secret-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///medi_reach.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Medicine(db.Model):
    """Minimal example model to demonstrate DB integration.

    Fields can be extended by the database-focused team member later.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self) -> str:  # pragma: no cover - simple representation
        return f"<Medicine id={self.id} name={self.name!r} price={self.price}>"


def _ensure_db_initialized() -> None:
    """Create tables if they do not exist yet.

    This is safe to call during development; in production, prefer migrations.
    """
    with app.app_context():
        db.create_all()


@app.route("/")
def index():
    """Homepage introducing Medi-Reach and linking to other sections."""
    return render_template("index.html")


@app.route("/medicines")
def medicines():
    """List available medicines (placeholder list until seeding/CRUD is added)."""
    _ensure_db_initialized()
    items: List[Medicine] = Medicine.query.order_by(Medicine.name.asc()).all()
    return render_template("medicines.html", medicines=items)


@app.route("/order", methods=["GET", "POST"])
def order():
    """Mock order form. POST will validate minimal fields and show a flash."""
    if request.method == "POST":
        customer_name = request.form.get("customer_name", "").strip()
        medicine_name = request.form.get("medicine_name", "").strip()
        address = request.form.get("address", "").strip()

        if not customer_name or not medicine_name or not address:
            flash("Please fill out all fields before submitting.", "error")
        else:
            # In a future iteration, persist order and trigger fulfillment workflow.
            flash("Order submitted successfully (mock).", "success")
            return redirect(url_for("order"))

    return render_template("order.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Simple contact page with a feedback form (not persisted yet)."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("All fields are required.", "error")
        else:
            # Future: save message or send email via a background job.
            flash("Thanks for reaching out! We will get back to you soon.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/health")
def health():
    """Health check endpoint useful for quick validation and CI smoke tests."""
    return jsonify({"status": "ok"})


@app.route("/debug/seed")
def debug_seed():
    """Development helper to seed a few medicines if none exist.

    This avoids circular-import issues by keeping related logic co-located.
    Remove or lock down in production environments.
    """
    _ensure_db_initialized()
    if Medicine.query.count() == 0:
        db.session.add_all(
            [
                Medicine(name="Paracetamol 500mg", price=1.50),
                Medicine(name="Ibuprofen 200mg", price=2.00),
                Medicine(name="Amoxicillin 500mg", price=5.25),
            ]
        )
        db.session.commit()
        seeded = True
    else:
        seeded = False

    return jsonify({"seeded": seeded, "count": Medicine.query.count()})


if __name__ == "__main__":
    # Create tables on first run for convenience during development.
    _ensure_db_initialized()
    app.run(debug=True)


