from flask import Flask,request,render_template
import numpy
import pandas
import sklearn
import pickle

# importing model
model = pickle.load(open('model.pkl','rb'))

# creating flask app
app = Flask(__name__)


@app.route('/')