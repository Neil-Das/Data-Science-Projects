import pandas as pd
from flask import Flask, request, jsonify
import joblib
import sklearn
import xgboost

app = Flask(__name__)

model = joblib.load("xgb_model_jl")

@app.route("/predict", methods = ["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    predictions = model.predict(query_df)
    predictions = [str(i) for i in predictions]
    return jsonify({"Predictions": list(predictions)})

@app.route("/", methods = ["GET"])
def welcome():
    return f'This is the Drug Classification Model. Please send a POST request to receive a prediction on the Drug Type.'

if __name__ == "__main__":
    app.run()