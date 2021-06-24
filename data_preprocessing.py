from data_preparation import *
from requirements import np
X = data.Open.values
Y = data.Close.values
X = np.log(X)
Y = np.log(Y)
lstm_X = X.reshape(-1, 1, 1)
lstm_Y = Y.reshape(-1, 1, 1)
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)
x_train = X[:200000]
y_train = Y[:200000]
x_test = X[200000:]
y_test = Y[200000:]
lstm_x_train = lstm_X[:200000]
lstm_y_train = lstm_Y[:200000]
lstm_x_test = lstm_X[200000:]
lstm_y_test = lstm_Y[200000:]

