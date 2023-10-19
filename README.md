# Data-Science-Projects Repository

Welcome to my Data Science Projects Repository, where you can find two distinct data science projects: a drug classification machine learning model and a food truck weekend planner. 
This repository contains detailed information and code for each of these projects.

## Project 1: Drug Classification Model

### Overview
This project focuses on building a drug classification model using XGBoost.
The model takes several features, including age, sex, blood pressure, cholesterol, and sodium to potassium ratio in the blood, and predicts one of six drugs. 
The Folder contains a Python script file that creates an API to take POST requests for data and predicts a Durg type using the classification model. There is also a Dockerfile that can deploy the model into production. Through two simple terminal operations, the Dockerfile can create a Docker container. 

## Project 2: Food Truck Weekend Planner

### Overview
The Food Truck Weekend Planner project is designed for food enthusiasts who want to explore various food trucks in Indiana over a weekend. 
It scrapes data from the Yelp API, cleans it, and then utilizes the Google Maps API to create a detailed two-day weekend plan, including departure times, travel times, and transportation type.
The routes for both days are visualized on an interactive map with the Folium package.
