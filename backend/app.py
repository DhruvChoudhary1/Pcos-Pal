from flask import Flask, request, jsonify, send_from_directory
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import mysql.connector
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="dhruv",
    password="dc131204",
    database="pcos_app"
)
cursor = db.cursor(dictionary=True)

# Load ML model and scaler
model = joblib.load('pcos_model.pkl')
scaler = joblib.load('scaler.pkl')


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_FOLDER = os.path.join(BASE_DIR, '..', 'frontend')
# ========== ROUTES ==========

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, 'login-signup.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(FRONTEND_FOLDER, path)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        return jsonify({"error": "Email already exists"}), 409

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (name, email, hashed_pw))
    db.commit()

    return jsonify({"message": "Signup successful"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Received data:", data)  # DEBUG PRINT

    email = data['email']
    password = data['password']

    cursor.execute("SELECT * FROM users WHERE email = %s OR name = %s", (email, email))

    user = cursor.fetchone()
    print("User from DB:", user)  # DEBUG PRINT

    if user and bcrypt.check_password_hash(user['password'], password):
        return jsonify({"message": "Login successful", "user_id": user['id'], "name": user['name']}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        user_id = data['user_id']  # Passed from frontend

        input_data = pd.DataFrame([[data['age'], data['bmi'], data['menstrual_irregularity'],
                                     data['testosterone'], data['follicle_count']]],
                                  columns=["Age", "BMI", "Menstrual_Irregularity",
                                           "Testosterone_Level(ng/dL)", "Antral_Follicle_Count"])
        
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]
        result = "The person has PCOS" if prediction == 1 else "The person does not have PCOS"

        # Save to predictions table
        cursor.execute("""
            INSERT INTO predictions (user_id, age, bmi, menstrual_irregularity, testosterone, follicle_count, result)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (user_id, data['age'], data['bmi'], data['menstrual_irregularity'],
              data['testosterone'], data['follicle_count'], result))
        db.commit()

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 200


if __name__ == '__main__':
    app.run(debug=True)
