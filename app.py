import os
import flask
import numpy as np
import pickle
import joblib
from flask import Flask, redirect, url_for, request, render_template

#create instance of the class
app = Flask(__name__, template_folder = 'templates')

#tell the falsk which url should trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

## prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,4)
    loaded_pipe = joblib.load("./model/pipe.joblib") # Load the pipeline
    result = loaded_pipe.predict(to_predict) # predict the values using loaded pipeline
    return result[0]

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.values()
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
    if float(result) == 0:
        prediction = 'This Customer belongs to group 1: Frequent card user with higher balance.' 
        img_filename = '/static/cluster_image/group1.png'
    elif float (result) == 1:
        prediction = 'This Customer belongs to group 2: Non-frequent card user with high card limit.'
        img_filename = '/static/cluster_image/group2.png'
    else:
        prediction = 'This Customer belongs to group 3: Non-frequent user with lower card limit and more contacts.'
        img_filename = '/static/cluster_image/group3.png'
    return render_template("result.html",prediction = prediction,user_image = img_filename)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)