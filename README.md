# stock-price-prediction
The aim of this project is to predict the closing price of a stock listed in the NSE based on the Open price for a given day. The project is purely regression based and I have handled ensemble technique to demonstrate the effectiveness of ensemble models. Totally 3 models are used:

Ensemble method(Linear + AdaBoost +XGBoost Regressor)
RandomForeset Regressor
A simple LSTM.
The results showed that ensemble did not support our use case whereas randomforeset and LSTM were most effective. I have tried to use matplotlib library to visualize the performance of each model.
This project includes script required to be deployed as a simple web app.

PS: 
1. Predicting the price of a stock does not only depend on the historical prices but a variety of factors including economy, environment conditions, internal and external security of a country, civil situation, etc. This is a simple project to demonstrate the usage of regression techniques and the importance of clean data.
2. I have not uploaded the model file owing to large size(~500MB).

![Capture](https://user-images.githubusercontent.com/44191470/123221135-3f0b2f00-d4ec-11eb-8593-240df9f718bd.PNG)
