import sqlite3
import os

DB_PATH = os.path.join("instance", "medi_reach.db")

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_users_table():
    """Create users table if not exists."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def init_medicines_table():
    """Create medicines table if not exists."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def init_orders_table():
    """Create orders table if not exists."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            medicine_id INTEGER NOT NULL,
            medicine_name TEXT NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            total_price REAL NOT NULL,
            delivery_address TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (medicine_id) REFERENCES medicines(id)
        )
        """
    )
    conn.commit()
    conn.close()

def seed_medicines():
    """Insert sample medicines for development."""
    sample_data = [
        ("Paracetamol", 5.00),
        ("Amoxicillin", 8.50),
        ("Ibuprofen", 6.75),
        ("Vitamin C", 4.25),
    ]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM medicines")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany(
            "INSERT INTO medicines (name, price) VALUES (?, ?)", sample_data
        )
        conn.commit()
        print("Sample medicines added!")
    else:
        print("ℹ Medicines already exist — skipping seeding.")

    conn.close()

def insert_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
    )
    conn.commit()
    conn.close()


def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def insert_order(user_id, medicine_id, medicine_name, quantity, total_price, delivery_address, customer_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO orders
        (user_id, medicine_id, medicine_name, quantity, total_price, delivery_address, customer_name)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (user_id, medicine_id, medicine_name, quantity, total_price, delivery_address, customer_name)
    )
    conn.commit()
    conn.close()


def get_all_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders


def get_all_medicines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()
    conn.close()
    return medicines
