# House-Price-Prediction

# Project Overview
This project aims to build a robust predictive model to estimate residential property prices based on various features such as location, square footage, number of rooms, and amenities. By applying Supervised Machine Learning (Regression), this tool helps real estate investors and homeowners make data-driven decisions regarding property valuation.

# Key Features

Outlier Detection: Used statistical methods to identify and remove anomalies in pricing that could skew model performance.
 Model: Evaluated performance across Linear Regression
Performance Metrics: Assessed model accuracy using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

# Tech Stack

Language: Python 
Libraries: Pandas, NumPy (Data Manipulation), Scikit-Learn (ML Modeling), Matplotlib/Seaborn (Visualizations) 
Environment: Jupyter Notebook / VS Code

# Project Pipeline
Data Acquisition: Loaded housing datasets (e.g., Kaggle House Prices or local market data).
Exploratory Data Analysis (EDA): Visualized correlations between features like "Total SqFt" and "Sale Price" using scatter plots.
Data Cleaning: Handled missing values and performed feature scaling to ensure model stability.
Modeling: Trained regression models to find the line of best fit for price prediction.
Validation: Used Cross-Validation to ensure the model generalizes well to unseen data.
