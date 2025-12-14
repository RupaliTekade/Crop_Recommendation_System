🌱 Crop Recommendation System

A Machine Learning–based Crop Recommendation System that suggests the most suitable crop to grow based on soil nutrients and environmental conditions. The project is built using Python, Scikit-learn, Flask, and deployed for real-world usage.

🚀 Live Demo : https://crop-recommendation-system-z2wz.onrender.com

📌 Problem Statement

Farmers often struggle to decide which crop to cultivate due to varying soil nutrients and climatic conditions. This system predicts the best crop using machine learning by analyzing:

Soil nutrients (N, P, K)

Temperature

Humidity

pH value

Rainfall

🧠 Machine Learning Approach

Algorithm: Random Forest Classifier

Preprocessing:

Label Encoding (target variable)

MinMax Scaling (feature normalization)

Evaluation Metrics:

Accuracy Score

Classification Report

Confusion Matrix

The model is trained on an agricultural dataset and saved using pickle for deployment.

📊 Model Performance

Achieved high accuracy on test data

Random Forest chosen for:

Better handling of non-linear data

Robustness against overfitting

⚙️ Input Features
Feature	Description
N	Nitrogen content in soil
P	Phosphorus content in soil
K	Potassium content in soil
Temperature	Temperature in °C (can be negative)
Humidity	Relative humidity (%)
pH	Soil pH value (0–14)
Rainfall	Rainfall in mm


✅ Input Validation

To ensure realistic predictions, the system validates inputs:

Temperature allowed between -5°C to 50°C

Humidity between 0–100%

pH between 0–14

Rainfall within realistic agricultural limits

N, P, K must be non-negative


🖥️ Tech Stack

Programming Language: Python

Machine Learning: Scikit-learn

Web Framework: Flask

Frontend: HTML, CSS

Deployment: Render (Free tier)






🎯 Use Cases

Helps farmers choose the right crop

Educational ML project for students

Demonstrates end-to-end ML deployment

📌 Future Improvements

Add fertilizer recommendation

Display prediction confidence score

Crop-wise climate explanation

Mobile-friendly UI



⭐ If you like this project

Give it a star ⭐ and feel free to fork or contribute!
