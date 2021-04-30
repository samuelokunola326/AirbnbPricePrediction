# AirbnbPricePrediction

## Overview 
This project is a python-based machine learning web application that was hosted using flask as the back end then deployed to Heroku for general access. The application is powered by 3 different machine learning models that are used to analyze an Airbnb dataset. The predictions from the model are then pooled together to create an estimated price range based on the input of the user.s

<!-- You can access the application through the link: Need Link -->

 ###### Data Sources

* https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data?select=AB_NYC_2019.csv
* https://www.kaggle.com/kritikseth/us-airbnb-open-data#__sid=js0
* http://insideairbnb.com/get-the-data.html

 <!-- ###### Hosting Application
The app uses html flask templates on the back end to render data via web browser and enable functionality and then deploy to Heroku for public access. -->

 ###### Preprocessing/Data Cleaning
The team used Jupyter Notebook to complete all preprocessing and data cleaning that was needed before spliting, training and testing each model.

* Remove outliers in the upper bound of dataset.
* Clean data by removing N/A's and adding 0 to blank numerical fileds where needed. 
* Translate categorical data to representative numerical fields in prep for creating test and training data.
* Check feature importance for hyperparameter tuning.

<!-- describe dataset  -->

###### Model Testing/Selection
Our group will train and test 3 different model types to predict the price of Airbnb listings in the New York area. We will compare the accuracy of the model against each other and use the model that produces the highest accuracy score as our final/primary model.

###### Data Visualization
Our team will also use Tableau to visualize our findings during the exploration of the model testing/selection process.
