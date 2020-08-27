# Project 2 - Ames Housing Data and Kaggle Challenge

![]('logo1.jpg')    ![]('logo2.png')




## Problem Statement
You've been recently hired at [Furman Realty](https://furmanrealty.com/central-iowa-mls-listings/) and your first work assignment is to build a model that will make the best possible prediction of home values in Ames, Iowa (Furman's product team would like to eventually turn this into a feature on their website, that homeowners can use to get an estimate of their house). You will be making a presentation to your inhouse product team about the process that led you to your final model and predictions.


## Executive Summary

Potential homebuyers, developers and potential investors would want to have more information on what are key features that actually contribute towards maximising the return on their investment or ensuring they don't shortchange themselves when making a sale. This is not an appraisal/definitive sale price but rather a starting point for negotations.

The more obvious inferences like having a better overall quality or a bigger size having a direct impact to the sale price. However, some interesting features were discovered to add more value to the overall value. For example, having the presence of a paved driveway, using poured concrete for your foundation or having a hipped roof, which is a type of roof where all sides slope downwards to the walls.

Features like having an unfinished garage interior, having a knob & tube wiring fusebox or having a carport(basically an unenclosed garage with 2 open sides) will hurt the sale value of a home.

If customers were interested in flipping houses (buying reasonably priced homes and refurnishing them), the neighbourhoods of Northridge Heights and Stone Brook would be of interest to potential 'investors'.


## The Data Science Process

### 1. Get the Data
The train and test sets have been provided in csv formats and at a first glance, there are several null values that would need to be imputed.


### 2. Explore the Data
* Explored the missing values and determine if the values are missing at random or is there is any discernable pattern
* Split the dataset into categorical and numerical sets for comparative analysis with respect to the target variable
* Based on the visualisations, determine the most suitable set of features to be cleaned for modelling
* Clean up any missing values by imputing with mean or null where neccesary 
* Created new interaction columns
* Label and One-Hot Encoded Categorical features


### 3. Modelling
* Create a baseline model to compare R2 score
* Create a function to return model metics and visualise the coefficients
* Train/test split and standardise the dataset
* Test against Linear Regression to optimise the CV, number of folds
* Run Lasso, Ridge and Elasticnet to evaluate the features


### 4. Evaluate the model
* Features that had zero or very close to zero coeffients from the Lasso model were progressively removed and evaluated
* After 3 rounds of feature elimination, 15 features were finally selected and their polynomial interaction terms were created to improve the fit of the model.
* Ridge was determined as the best model after fitting on the kaggle test data.


### 5. Answer the DS problem
* Built an estimator for SalePrice, which at the moment has a standard deviation of approximately  **$26k** (tested against blind data) 
* From the EDA visualisations, made recommendations on features that would add/detract value from a home


## Recommendations
There are several features that can be added to the dataset to improve the model's performance. For example:
* Home characteristics from current homeowners (including square footage, location or the number of bathrooms)
* Unique features like hardwood floors, granite countertops or a landscaped backyard (also from homeowners)
* On-market data such as listing price, description, comparable homes in the area and days on the market 
* Off-market data — tax assessments, prior sales and other publicly available records

In terms of the technical improvements, we could utilise Recursive Feature Elimation or run Feature Selector under Random Forest, to better evaluate the most effective features to utilise.