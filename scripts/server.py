import numpy as np
import pickle
from paths import model_path
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pickle.load(open(model_path, 'rb'))

@app.route('/api/<val>')
def predict(val):
    prediction = model.predict(np.array([[float(val)]]))
    return jsonify(prediction.item())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
