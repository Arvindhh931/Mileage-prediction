# Fuel Efficiency prediction

### with Root mean sqauared error of 2.5 miles per gallon

### **Deployment link** - [Make Prediction using various car features](https://arvindhh931-mileage-prediction-autompg-57du1p.streamlit.app/)
### **Integrating web application with database to collect data for prediction using cloud database service 'Deta'**
## Source:

This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University. The dataset was used in the 1983 American Statistical Association Exposition.

link - [Auto mpg (UCI machine learning repository)](https://archive.ics.uci.edu/ml/datasets/auto+mpg)

## Data Set Information:

This dataset is a slightly modified version of the dataset provided in the StatLib library. In line with the use by Ross Quinlan (1993) in predicting the attribute "mpg", 8 of the original instances were removed because they had unknown values for the "mpg" attribute. The original dataset is available in the file "auto-mpg.data-original".

### Attribute Information:

1. mpg : fuel efficiency in miles per gallon (continuous)
2. cylinders : Number of cylinders in a car (multi-valued discrete)
3. displacement : in cubic inches (continuous)
4. horsepower : (continuous)
5. weight : weight of car in pounds (continuous)
6. acceleration : (continuous)
7. model year : (multi-valued discrete)
8. origin : 1,2,3 (multi-valued discrete)
9. car name : string (unique for each instance)

Total 3 multivalued discrete and 5 continuous attributes

## Objective:
Prediction of city-cycle fuel consumption in miles per gallon given technical aspects & vehicle information 

![Alt Text](https://i.imgur.com/JSiYFsw.gif)

## Assumptions:
origin is taken as 1: USA 2:Europe 3: Asia for convenience

## Final Predictive Model 

### Multiple linear Regression
Kaggle - https://www.kaggle.com/code/hharvind/fuel-efficiency-prediction-in-mpg

## Skills Aquired- 
1) Exploratory Data Analysis
2) Data pre-processing
2) KNN-Imputer
3) Linear Regression
4) L1 & L2 Regularization
5) Polynomial Linear Regression
6) KNearestNeighbour Regression
7) Automatic Report generation (Functional Programming)

## Hurdles
1) Automobile Domain 
2) Treating outliers when Less amount of Data available
3) High Multi-collinearity
4) Deployment and integration with Database

## Liabraries used
1) Numpy
2) Pandas
3) Scikit-learn
4) Streamlit (Deployment)
5) Deta
