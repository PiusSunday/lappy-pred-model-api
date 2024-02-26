# Lappy-Pred-App

In this project, I implemented a machine learning model for predicting laptop prices based on their specifications. 
The model is built using Python and various machine learning packages, and it's exposed as a RESTful API using Flask.
Users can make POST requests to the API with laptop specifications, and the model will return an estimated price. 
In this repository, I detailed the process, and it contains the code for training the model, and deploying it as an API.

## Laptop Prices Predictor

* Designed a Flask API that predicts the price a laptop given the configurations.
* Sourced the laptops data from ouedkniss.com, facebook marketplace and instagram laptop stores in Algeria.
* Developed Different LINEAR_MODELS, NEURAL_NETWORKS, DECISION_TREES, NEAREST_NEIGHBORS, and SUPPORT VECTOR MACHINES Regressors to get the best model.
* Deployed the Machine Learning model to Heroku Server using Flask

## Links and Resources Used

* **OuedKniss MarketPlace**: [https://www.ouedkniss.com/](https://ouedkniss.com/)

* **Heroku**: [https://www.heroku.com/](https://www.www.heroku.com/)

* **Model Deployment Video**: [https://youtu.be/ax3WyB-_LJY](https://youtu.be/ax3WyB-_LJY)

* **Packages**: pandas, numpy, sklearn, flask, pickle

## Web Scraping

I sourced my laptop data from OuedKniss website which is a major marketplace for different laptops in the Algerian Market. This page contains the specifications of different laptops. I tried to extract the different features of the laptops such as:

* BRAND
* CPU (BRAND, CORE, GENERATION, FAMILY)
* RAM
* DDR TYPE
* GPU BRAND
* SCREEN SIZES
* PRICE
* etc...# Lappy-Pred-App

In this project, I implemented a machine learning model for predicting laptop prices based on their specifications.
The model is built using Python and various machine learning packages, and it's exposed as a RESTful API using Flask.
Users can make POST requests to the API with laptop specifications, and the model will return an estimated price.
In this repository, I detailed the process, and it contains the code for training the model, and deploying it as an API.

## Laptop Prices Predictor

* Designed a Flask API that predicts the price a laptop given the configurations.
* Sourced the laptops data from ouedkniss.com, facebook marketplace and instagram laptop stores in Algeria.
* Developed Different LINEAR_MODELS, NEURAL_NETWORKS, DECISION_TREES, NEAREST_NEIGHBORS, and SUPPORT VECTOR MACHINES Regressors to get the best model.
* Deployed the Machine Learning model to Heroku Server using Flask

## Links and Resources Used

* **OuedKniss MarketPlace**: [https://www.ouedkniss.com/](https://ouedkniss.com/)

* **Heroku**: [https://www.heroku.com/](https://www.www.heroku.com/)

* **Model Deployment Video**: [https://youtu.be/ax3WyB-_LJY](https://youtu.be/ax3WyB-_LJY)

* **Packages**: pandas, numpy, sklearn, flask, pickle

## Web Scraping

I sourced my laptop data from OuedKniss website which is a major marketplace for different laptops in the Algerian Market. This page contains the specifications of different laptops. I tried to extract the different features of the laptops such as:

* BRAND
* CPU (BRAND, CORE, GENERATION, FAMILY)
* RAM
* DDR TYPE
* GPU BRAND
* SCREEN SIZES
* PRICE
* etc...

After extracting the laptop data from different sources, My dataset now consists of the information more than 200 different laptops.
Link to complete dataset will be seen in the files.

## Feature Engineering

From the data I sourced from the different sources, I made the following changes and created new variables:

* RAM - Made columns for RAM SIZE in GB, the RAM(DDR) version
* PROCESSOR - Made columns for CPU BRAND, CPU CORE, CPU GENERATION and CPU FAMILY
* STORAGE - Made new columns for the DISK TYPE and the SSD and HDD SIZES
* DISPLAY - Made new columns for the SCREEN SIZE(in inches) and SCREEN RESOLUTION
* GRAPHICS CARD - Made new columns for the GPU BRAND and GPU TYPE

## Data Preprocessing

Since we can only feed numerical data to our models, The few columns which are categorical (String Columns), they need to converted to numerical columns.

This I did use sklearn OneHotEncoder library.

These converted columns are: BRAND, CPU BRAND, CPU CORE, CPU FAMILY, DISK TYPE, GPU BRAND, GPU TYPE, SCREEN RESOLUTION, and STATE.

## Exploratory Data Analysis

A file would be included for the Exploratory Data Analysis done in Jupyter NoteBook.

## Model Building

Used scikit-learn library for the Machine Learning tasks. Applied OneHotEncoding and converted the categorical variables into numerical ones. Then I split the data into training and test sets with a train size of 80% and test size of 20%.

I tried 5 different Regression Models ( LINEAR MODELS, NEURAL NETWORKS, DECISION TREES, NEAREST NEIGHBORS, and SUPPORT VECTOR MACHINES) and evaluated them using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (R-MSE) and Root Square Score(R²).

## Model Deployment

I deployed the model as a flask API in JSON format to Heroku which is a Platform As A Service(PAAS)

[Heroku API](https://lappy-pred-app.herokuapp.com)


After extracting the laptop data from different sources, My dataset now consists of the information more than 200 different laptops.
Link to complete dataset will be seen in the files.

## Feature Engineering

From the data I sourced from the different sources, I made the following changes and created new variables:

* RAM - Made columns for RAM SIZE in GB, the RAM(DDR) version
* PROCESSOR - Made columns for CPU BRAND, CPU CORE, CPU GENERATION and CPU FAMILY
* STORAGE - Made new columns for the DISK TYPE and the SSD and HDD SIZES
* DISPLAY - Made new columns for the SCREEN SIZE(in inches) and SCREEN RESOLUTION
* GRAPHICS CARD - Made new columns for the GPU BRAND and GPU TYPE

## Data Preprocessing

Since we can only feed numerical data to our models, The few columns which are categorical (String Columns), they need to converted to numerical columns.
  
This I did use sklearn OneHotEncoder library.

These converted columns are: BRAND, CPU BRAND, CPU CORE, CPU FAMILY, DISK TYPE, GPU BRAND, GPU TYPE, SCREEN RESOLUTION, and STATE.

## Exploratory Data Analysis

A file would be included for the Exploratory Data Analysis done in Jupyter NoteBook.

## Model Building

Used scikit-learn library for the Machine Learning tasks. Applied OneHotEncoding and converted the categorical variables into numerical ones. Then I split the data into training and test sets with a train size of 80% and test size of 20%.

I tried 5 different Regression Models ( LINEAR MODELS, NEURAL NETWORKS, DECISION TREES, NEAREST NEIGHBORS, and SUPPORT VECTOR MACHINES) and evaluated them using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (R-MSE) and Root Square Score(R²).

## Model Deployment

I deployed the model as a flask API in JSON format to Heroku which is a Platform As A Service(PAAS)

[Heroku API](https://lappy-pred-app.herokuapp.com)
