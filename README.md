# Customer Clustering Project 

# Objective
* Find possible groups of clients and define their characteristics. 
* Evaluate the churn rate in all groups of clients.
* Build an application that allows your customer to find the right group (cluster) for the client.

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
- Create a virtual enviroment in Python(version>3.9) and activate it
- pip install -r requirements.txt
- Install [Docker](https://docs.docker.com/get-docker/)\
`docker build -t flask-heroku:latest .`\
`docker run -d -p 5000:5000 flask-heroku`

* Create [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) account and a new app name\
`heroku container:login`\
`heroku container:push web --app your_app_name`\
`heroku container:release web --app your_app_name`


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

- Kmeans with only numerical data  (silhouette score: 49.6)
- Kmeans with both numerical and categorical features. For categorical features, apply one hot encoding (silhouette score: 49.1)

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
- Flask \
Create app.py to get and post information from API
- Docker \
Create docker container to run the app
- Heroku \
App pushed on heroku so that everyone can have the access to use the app