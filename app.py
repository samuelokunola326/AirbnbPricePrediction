from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo
import xgboost as xgb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
import joblib
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder


linear_model = joblib.load("models/LR.h5")
xgb_model = joblib.load("models/xgbmodel.h5")
rf_model = joblib.load("models/rf.h5")


app = Flask(__name__)
app.static_folder = "templates/static"



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        testdf = []
        boroughtype = int(request.form["boroughradio"])
        roomtype = int(request.form["roomtyperadio"])
        review_input = request.form["reviewmonth"]
        avail_input = request.form["availability"]
        testdf.append(float(review_input))
        testdf.append(int(avail_input))
        borough = ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
        room = ["Entire Home/Apt", "Private Room", "Shared Room"]
        boroughpicked = borough[boroughtype]
        roompicked = room[roomtype]
        for x in range(5):
            if boroughtype == 0:
                testdf.append(1)
            else:
                testdf.append(0)
            boroughtype = boroughtype - 1
        for x in range(3):
            if roomtype == 0:
                testdf.append(1)
            else:
                testdf.append(0)
            roomtype = roomtype - 1
        
        df = pd.DataFrame([testdf], columns=[
            "reviews_per_month",
            "availability_365",
            "neighbourhood_group_Bronx",
            "neighbourhood_group_Brooklyn",
            "neighbourhood_group_Manhattan",
            "neighbourhood_group_Queens",
            "neighbourhood_group_Staten Island",
            "room_type_Entire home/apt",
            "room_type_Private room",
            "room_type_Shared room"])
        xgbtest = xgb.DMatrix(df)
        linear_predict = linear_model.predict(df)
        xgb_predict = xgb_model.predict(xgbtest)
        rf_predict = rf_model.predict(df)
        price = [linear_predict[0][0], xgb_predict[0], rf_predict[0]]
        #price = [linear_predict[0][0], xgb_predict[0]]

        print(price)
        
        minprice = round(min(price), 2)
        maxprice = round(max(price), 2)
        avgprice = round((sum(price) / 3), 2)
        
        return render_template("predict.html", MinPrice=minprice, MaxPrice=maxprice, Average=avgprice, Borough=boroughpicked, RoomType=roompicked, ReviewPerMonth=review_input, Availability=avail_input)
    else:
        return render_template("predict.html")


@app.route("/infographic")
def infographic():
    return render_template("infographic.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)