# Medi-Reach API

A simple Flask-based backend for managing medicines, with a frontend for adding and viewing medicines.

## Project Structure

```
├── app.py
├── api.py
├── auth.py
├── db.py
├── instance/
│   └── medi_reach.db
├── requirements.txt
├── static/
│   └── css/
│       └── styles.css
└── templates/
    ├── base.html
    ├── add_medicine.html
    ├── medicines.html
    └── ...
```

---

## Setup

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

The app runs at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## API Endpoints

### 1. Get all medicines

```
GET /api/medicines
```

**Response:**

```json
{
  "count": 4,
  "medicines": [
    { "id": 1, "name": "Paracetamol", "price": 5.0 },
    { "id": 2, "name": "Amoxicillin", "price": 8.5 }
  ]
}
```

---

### 2. Add a new medicine

```
POST /api/medicines/create
Content-Type: application/json
```

**Body:**

```json
{
  "name": "Aspirin",
  "price": 7.5
}
```

**Response:**

```json
{
  "message": "Medicine added successfully",
  "id": 5,
  "name": "Aspirin",
  "price": 7.5
}
```

> Note: `id` is auto-generated, so you do not provide it.

---
Done by Ivan

### Notes

* Database is located at `instance/medi_reach.db` (ignored by git).
* Make sure the database and `instance/` folder exist before running the app.
* Only POST valid JSON to `/api/medicines/create` — `name` must be non-empty and `price` > 0.
