from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join("model", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        x_value = float(request.form["x_value"])
        prediction = model.predict(np.array([[x_value]]))[0][0]
        return render_template("index.html", prediction=round(prediction, 2))
    except:
        return render_template("index.html", prediction="Invalid input")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
