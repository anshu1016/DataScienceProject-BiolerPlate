# from flask import Flask, jsonify, render_template, request
# import os
# import numpy as np 
# import pandas as pd 
# from src.DataScienceProject.pipeline.prediction_pipeline import PredictionPipeline


# app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def homepage():
#     return render_template('index.html')

# # route to train the pipeline 
# @app.route('/train', methods=['GET'])
# def training():
#     os.system('python main.py')
#     return render_template('index.html', train_status="✅ Model trained successfully!")


# @app.route('/predict', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             fixed_acidity = float(request.form['fixed_acidity'])
#             volatile_acidity = float(request.form['volatile_acidity'])
#             citric_acid = float(request.form['citric_acid'])
#             residual_sugar = float(request.form['residual_sugar'])
#             chlorides = float(request.form['chlorides'])
#             free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
#             total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
#             density = float(request.form['density'])
#             pH = float(request.form['pH'])
#             sulphates = float(request.form['sulphates'])
#             alcohol = float(request.form['alcohol'])
            
#             data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
#                     free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            
#             data = np.array(data).reshape(1, 11)
            
#             obj = PredictionPipeline()
#             predict = obj.predict(data)

#             # Render the same index.html and pass prediction
#             return render_template('index.html', prediction=round(float(predict[0]), 2))

#         except Exception as e:
#             print('The Exception message is: ', e)
#             return 'Something went wrong'
#     else:
#         return render_template('index.html')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from src.DataScienceProject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    prediction = None
    train_status = request.args.get('train_status')  # Capture from redirect
    form_data = {}

    if request.method == 'POST':
        try:
            fields = [
                'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide',
                'density', 'pH', 'sulphates', 'alcohol'
            ]
            form_data = {field: request.form.get(field, '') for field in fields}
            data = np.array([float(form_data[field]) for field in fields]).reshape(1, -1)

            obj = PredictionPipeline()
            prediction = round(float(obj.predict(data)[0]), 2)

        except Exception as e:
            print("Prediction Error:", e)
            prediction = "⚠️ Error occurred during prediction."

    return render_template("index.html", prediction=prediction, train_status=train_status, form_data=form_data)

@app.route("/train", methods=['GET'])
def training():
    os.system('python main.py')
    return redirect(url_for('homepage', train_status="✅ Model trained successfully!"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
