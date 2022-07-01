from distutils.log import debug
from flask import Flask, jsonify, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)


LABEL = ['Not Diabetes', 'Pre-Diabetes', 'Diabetes']
columns=['BMI', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
       'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
       'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
       'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Income']
       
with open("full_pipeline_with_predictor_ada.pkl", "rb") as g:
    predictor_ada = pickle.load(g)

with open("full_pipeline_with_predictor_rf.pkl", "rb") as f:
    predictor_rf = pickle.load(f)

@app.route("/")
def homepage():
    return "<h1>Backend Pemodelan Diabetes </h1>"

@app.route("/predict_ada", methods=["GET", "POST"])
def diabetes_inference_ada():
    if request.method == 'POST':
        data = request.json
        print(data)
        new_data = [data['BMI'],
                        data['HighBP'],
                        data['HighChol'],
                        data['CholCheck'],
                        data['Smoker'],
                        data['Stroke'],
                        data['HeartDiseaseorAttack'],
                        data['PhysActivity'],
                        data['Fruits'],
                        data['Veggies'],
                        data['HvyAlcoholConsump'],
                        data['AnyHealthcare'],
                        data['NoDocbcCost'],
                        data['GenHlth'],
                        data['MentHlth'],
                        data['PhysHlth'],
                        data['DiffWalk'],
                        data['Sex'],
                        data['Age'],
                        data['Income']]

        new_data = pd.DataFrame([new_data],columns=columns)

        res = predictor_ada.predict(new_data)
        print("res :", res )
        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': LABEL[int(res[0])]}}


        return jsonify(response)
            

    return "Silahkan gunakan method post untuk mengakses model"

@app.route("/predict_rf", methods=["GET", "POST"])
def diabetes_inference_rf():
    if request.method == 'POST':
        data = request.json
        new_data = [data['BMI'],
                        data['HighBP'],
                        data['HighChol'],
                        data['CholCheck'],
                        data['Smoker'],
                        data['Stroke'],
                        data['HeartDiseaseorAttack'],
                        data['PhysActivity'],
                        data['Fruits'],
                        data['Veggies'],
                        data['HvyAlcoholConsump'],
                        data['AnyHealthcare'],
                        data['NoDocbcCost'],
                        data['GenHlth'],
                        data['MentHlth'],
                        data['PhysHlth'],
                        data['DiffWalk'],
                        data['Sex'],
                        data['Age'],
                        data['Income']]

        new_data = pd.DataFrame([new_data],columns=columns)

        res = predictor_ada.predict(new_data)
        print("res :", res )
        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': LABEL[int(res[0])]}}


        return jsonify(response)