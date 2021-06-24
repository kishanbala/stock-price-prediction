from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('randomforest.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results in GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.log(int_features)
    final_features = final_features.reshape(-1,1)
    prediction = model.predict(final_features)
    output = round(float(np.exp(prediction)),2)

    return render_template('index.html',
                           prediction_text="The predicted closing price of your desired stock is {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
