from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model_avg .joblib')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sequence = request.form['sequence']

    # Use the loaded model for prediction
    new_data = {'Sequence': [sequence]}
    new_df = pd.DataFrame(new_data)
    prediction = model.predict(new_df)

    return render_template('predict.html', sequence=sequence, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)