# Customer Clustering Project 

# Mission
* Find possible groups of clients and define their characteristics. 
* Evaluate the churn rate in all groups of clients.
* Build an application that allows your customer to find the right group (cluster) for a given client.

# Objective
* Build machine learning model for clustering.
* Select the right performance metrics for model.
* Tuning parameters of the model for better performance.
* Describe the results from unsupervised learning.
* Be able to deploy a machine learning model.
* Be able to create a Flask API that can handle a machine learning model.
* Create a basic Graphical User Interface to call the API.
* Deploy the API and the interface on Heroku.

# Solution
An app for searching the customer group hhas been developed and deployed on heroku with the link:\
http://credit-card-customer.herokuapp.com/

### index page:
![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/App%20Outline.png)

### result page:
![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/result.png)

# Data Sources
The dataset of the credit card customers can be downloaded on the following link:\
[Credit Card Customers](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)

# Usage
* Create a virtual enviroment in Python(version>3.9) and activate it
* pip install -r requirements.txt
* Install [Docker](https://docs.docker.com/get-docker/)
* Create [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) account and a new app name

# Process Flow
![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/work%20flow.png)

### Data Processing
1. Data cleaning and wrangling
2. Exploratory data analysis
   * for categorical features, plot the distribution chart between existing and churn customers\
   some examples:\
   ![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/gender_distribution.png)
   ![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/income_distribution.png)

   * for numerical features, get the mean values of each feature and compare the data between existing and churn customers

3. Features Selection based on heatmap and exploratory data analysis


### Model building

1. Kmeans with only numerical data  (silhouette score: 49.6)
2. Kmeans with numerical and categorical features, using one hot encoding (silhouette score: 49.1)
3. K-propotype to combine numerical and categorical features(silhouette score not available for this mode)

Kmeans with only numerical features was the final model for deployment, as it gives the better silhouette score.

### Clusters Prediction

* Group 1: Frequent card user with higher balance.\
Churn Rate: 8.1%
* Group 2: Non-frequent card user with high card limit.\
Churn Rate: 10.7%
* Group 3: Non-frequent user with lower card limit and more customer contacts.\
Churn Rate: 30.3% \
![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/assets/Churn%20Rate%20in%20client%20group.png)

### Cluster Anlaysis
Analysis and define groups characteristics.
#### Example:
![alt text](https://github.com/yhwang0123/customer_clustering/blob/main/static/cluster_image/group1.png)

### Deployment
1. Flask \
Create app.py to get and post information from API
2. Docker \
Create docker container to run the app
3. Heroku \
App pushed on heroku so that everyone can have the access to use the app