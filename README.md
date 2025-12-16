# Linear Regression Predictor

A small toy project demonstrating a complete pipeline for a simple linear regression model:
- generate synthetic data,
- train a scikit-learn LinearRegression model,
- save the trained model with pickle,
- serve a minimal Flask web app to make predictions from user input.

The model in this project is trained on synthetic data generated as y = 5 * X + 3 + noise, so predictions follow that underlying relationship.

---

## Features
- Synthetic data generation and model training with scikit-learn.
- Model persistence using pickle (`model/model.pkl`).
- Simple Flask app with an HTML form to submit a single numeric input (CGPA in the UI) and receive a predicted package value.
- Minimal, easy-to-understand code intended for learning and quick prototyping.

---

## Repository structure (expected)
- `train.py` (or similar): training script that creates `model/model.pkl`
- `model/` : directory containing saved model (`model.pkl`)
- `app.py` : Flask application that loads `model/model.pkl` and exposes `/` and `/predict`
- `templates/index.html` : Flask template (the provided HTML) for the UI
- `README.md` : this file

If your filenames are different, substitute accordingly.

---

## Requirements

Recommended Python version: 3.8+

Create a virtual environment and install dependencies:

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Example `requirements.txt` for this project:
```
numpy
scikit-learn
flask
```

(If you don't have a `requirements.txt`, you can install packages directly: `pip install numpy scikit-learn flask`)

---

## Training the model

The training script (example name: `train.py`) performs these steps:
- generates synthetic X and y data (100 samples),
- fits a `LinearRegression()` model,
- saves the fitted model to `model/model.pkl` using `pickle`.

Run the training script:

```bash
# Make sure a model/ directory exists
mkdir -p model

# Run the training script (adjust filename if needed)
python train.py
```

After running you should see:
```
✅ Model trained and saved at model/model.pkl
```

---

## Running the Flask app

Start the Flask web app (example filename: `app.py`):

```bash
# Make sure the virtualenv is activated and dependencies installed
python app.py
```

Default behavior in the provided code:
- Host: `127.0.0.1`
- Port: `5000`
- Debug mode: enabled

Open your browser and navigate to:
http://127.0.0.1:5000/

You will see a form that asks for a numeric input (labelled "Enter CGPA value:"). Enter a value and click "Predict" — the app will display the predicted package computed by the saved linear regression model.

---

## Example usage

If the underlying model is approximately y = 5 * X + 3:
- If you input X = 6.0, expected prediction ≈ 5*6 + 3 = 33 (plus/minus noise).

---

## Important notes & troubleshooting

- Ensure `model/model.pkl` exists and is accessible by the Flask app. If you retrain and overwrite the model, restart the Flask server to reload it (the current code loads the model at import/startup).
- If you encounter `ModuleNotFoundError`, install the missing package into your active venv.
- If the app returns "Invalid input", ensure the form sends a numeric value and that the form input name matches the expected key (`x_value` in the provided code).
- If running on a remote server and you want external access, change `host="127.0.0.1"` to `host="0.0.0.0"` in `app.run(...)` (be cautious about exposing debug mode).

---

## Extending this project

Ideas for improvement:
- Add validation and clearer error messages on the UI.
- Provide a REST JSON endpoint (e.g., `/api/predict`) to allow programmatic prediction requests.
- Replace synthetic data with a real dataset (CSV) and add a data loading/EDA step.
- Add unit tests for training and prediction functions.
- Containerize the app with Docker for easy deployment.

---

## License

This project is provided for educational purposes. You can apply an open-source license such as MIT if desired.

---

## Author

vinodbavage31

Acknowledgements: this is a compact educational example demonstrating scikit-learn model training and a minimal Flask-based prediction UI.
