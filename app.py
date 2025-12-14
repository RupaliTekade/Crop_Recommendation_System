from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load pickled objects
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))  # MUST exist

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    # DataFrame for scaler
    input_df = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    )

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict
    pred_num = model.predict(scaled_input)

    # Decode label
    crop = encoder.inverse_transform(pred_num)[0]
    crop_image = crop.replace(" ", "_")

    return render_template(
        "index.html",
        crop=crop,
        crop_image=crop_image
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

