from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory database for demonstration purposes
users_db = {}

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users_db:
        return jsonify({"message": "User already exists!"}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = hashed_password

    return jsonify({"message": "User registered successfully!"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    hashed_password = users_db.get(username)

    if not hashed_password or not check_password_hash(hashed_password, password):
        return jsonify({"message": "Invalid username or password!"}), 401

    return jsonify({"message": f"Welcome, {username}!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
