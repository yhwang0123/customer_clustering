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
        prediction = "Group 1 - Frequent card user with higher balance"
        churn = "This customer is most likely to continue with our card service."
        group_image = '/static/cluster_image/g1.png'
        img_filename = '/static/cluster_image/group1.png'
    elif float (result) == 1:
        prediction = "Group 2 - Non-frequent card user with high card limit"
        churn =  "This customer is more likely to continue with our card service."
        group_image = '/static/cluster_image/g2.png'
        img_filename = '/static/cluster_image/group2.png'
    else:
        prediction = "Group 3 - Non-frequent user with lower card limit and more contacts with customer service"
        churn = "This customer is more likely to churn."
        group_image = '/static/cluster_image/g3.png'
        img_filename = '/static/cluster_image/group3.png'
    return render_template("result.html",prediction = prediction,churn=churn, group_image = group_image, user_image = img_filename)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)