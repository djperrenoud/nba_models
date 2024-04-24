# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

def random_forest_regressor():
    # Load the dataset
    data = pd.read_csv('21_22_data.csv', encoding='latin1')  # Specify the encoding as 'latin1'
    
    # Remove unnecessary columns
    data = data.drop(columns=['Player', 'Age', 'Rk', 'Tm', 'Pos'])
    
    # Splitting the data into predictor and target variables
    X = data.drop(columns=['PTS'])
    y = data['PTS']
    
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Implementing the Random Forest algorithm
    model = RandomForestRegressor(random_state=0)
    model.fit(X_train, y_train)
    
    # Making predictions
    y_pred = model.predict(X_test)
    
    # Model evaluation
    r_squared = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='blue')
    plt.title('Actual vs Predicted')
    plt.xlabel('Actual PTS')
    plt.ylabel('Predicted PTS')
    plt.show()
    
    return {"r_squared": r_squared, "mse": mse}

