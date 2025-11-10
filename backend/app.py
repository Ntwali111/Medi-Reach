# Medi-Reach Backend API
# This is a placeholder file for the backend implementation
# Backend will be implemented in a future phase

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Medi-Reach API - Coming Soon'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
