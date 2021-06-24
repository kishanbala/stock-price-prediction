from requirements import *
from data_preprocessing import x_train, y_train, lstm_x_train, lstm_y_train, x_test, y_test, lstm_x_test, \
    lstm_y_test

## Ensemble model

model1 = LinearRegression(fit_intercept=True)
model2 = AdaBoostRegressor(random_state=123)
model3 = xg.XGBRegressor(random_state=123)
model = VotingRegressor(estimators=[('lr', model1), ('abr', model2), ('xgr', model3)], verbose=True)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
RMSE = mean_squared_error(y_test, y_pred, squared=False)
print("R2 score for ensemble model is {:.2f}".format(model.score(x_train, y_train.ravel())))
print("Root Mean squared error for ensemble model is {}".format(RMSE))

## RandomForest model
forest = RandomForestRegressor(random_state=133, bootstrap=False)
forest.fit(x_train, y_train.ravel())
y_pred = forest.predict(x_test)
RMSE = mean_squared_error(y_test, y_pred, squared=False)
print("R2 score for training data is {:.2f}".format(forest.score(x_train, y_train.ravel())))
print("Root Mean squared error for RandomForest model is  {}".format(RMSE))

## LSTM
lstm = Sequential()

lstm.add(LSTM(units=100, return_sequences=True, input_shape=(lstm_x_train.shape[1], 1)))
lstm.add(Dropout(0.3))

lstm.add(LSTM(units=100, return_sequences=True))
lstm.add(Dropout(0.3))

lstm.add(LSTM(units=100, return_sequences=True))
lstm.add(Dropout(0.3))

lstm.add(LSTM(units=100))
lstm.add(Dropout(0.2))

lstm.add(Dense(units=1))

lstm.compile(optimizer='SGD', loss='mean_squared_error')

lst_model = lstm.fit(lstm_x_train, lstm_y_train, epochs=500, batch_size=1000, validation_split=0.3)

RMSE = RootMeanSquaredError(lstm_x_test, lstm_y_test)
print("Root Mean squared error for LSTM is {}".format(RMSE))
