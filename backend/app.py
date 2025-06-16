from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)


model = joblib.load('pcos_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_data = pd.DataFrame([[data['age'], data['bmi'], data['menstrual_irregularity'], data['testosterone'], data['follicle_count']]],
                                  columns=["Age", "BMI", "Menstrual_Irregularity", "Testosterone_Level(ng/dL)", "Antral_Follicle_Count"])
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]

        result = "The person has PCOS" if prediction == 1 else "The person does not have PCOS"
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
 