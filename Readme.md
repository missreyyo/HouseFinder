# Real Estate Price Prediction Project

## Overview
This project aims to predict real estate prices using various machine learning models, focusing on achieving a Mean Absolute Percentage Error (MAPE) below 10%. The dataset includes real estate listings with various features, both numerical and categorical. The project encompasses data loading, cleaning, preprocessing, feature selection, model training, and evaluation.

## Table of Contents

- [Data Loading](#data-loading)
- [Data Cleaning](#data-cleaning)

- [Removal of Outliers](#removal-of-outliers)
- [Categorical Encoding](#categorical-encoding)

- [Feature Selection](#feature-selection)
- [Machine Learning Algorithm and Parameterization](#machine-learning-algorithm-and-parameterization)

- [Model Training](#model-training)
- [Evaluation and Conclusion](#evaluation-and-conclusion)

- [Recommendations](#recommendations)
- [Visualization and Interpretation of Results](#visualization-and-interpretation-of-results)

### Data Loading
Data is loaded into a pandas DataFrame for analysis and preprocessing using `pd.read_csv()`.

### Data Cleaning
#### Missing Values
Check for missing values using `df.isnull().sum()`.

#### Price Column
Remove dots and convert the column to numeric format:
```python
df['Price'] = df['Price'].str.replace('.', '').astype(float)
```
## Removal of Outliers
- **Price:** Remove unlikely price values.
- **Observations:** Remove districts with fewer than 5 observations and neighborhoods with fewer than 2 observations.
- **Square Meters:** Remove unlikely values in square meters.
- **Number of Rooms and Floor of Home:** Detect and remove abnormal values.

## Categorical Encoding
- **Floor Category:** Convert floor category and other categorical data into numerical format.
- **Label Encoding:** Use Scikit-learn's LabelEncoder to convert categorical variables into numerical format:
  ```python
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  df['City'] = le.fit_transform(df['City'])
  ```
  ## One-Hot Encoding
Apply one-hot encoding for non-ordinal categorical variables:
```python
df = pd.get_dummies(df, columns=['Floor Category', 'City', 'Town', 'Neighborhood', 'Credit Acceptance', 'Kombi Doğalgaz Heating'])
```
## Feature Selection
Selected features include Total Square Meter, Number of Rooms, Number of Floors, Floor of Home, and all one-hot encoded categorical variables.

## Machine Learning Algorithm and Parameterization
### Train-Test Split
Split the dataset into training (80%) and testing (20%) sets:
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
```
## Feature Scaling
Apply standard scaling to standardize the features:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
## Model Training
Train a Random Forest Regressor with 210 estimators and a random state of 50:
```python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=210, random_state=50)
model.fit(X_train, y_train)
```
## Evaluation and Conclusion
### First Project
- **Linear Regression:** Simple and fast but low performance on complex datasets.
- **XGBoost:** Higher accuracy and performance with hyperparameter optimization.

### Latest Project
- **Random Forest:** Best performance with MAPE: 7.05%, MAE: 337,268, R-squared: 0.857.

## Recommendations
- **First Project:** Good initial attempt. Starting with simple models is a valid approach.
- **Latest Project:** The Random Forest model showed the best performance and can be confidently used in business or research projects.

## Visualization and Interpretation of Results
- **Histogram:** The Percentage Error Histogram shows that most errors are low, indicating accurate predictions.
- **Scatter Plot:** The Price vs. Percentage Error Scatter Plot shows that the error rate increases for higher-priced houses.

## Conclusion
The goal of reducing the error rate below 10% was successfully achieved. The project required significant time and effort, involving trial and error for optimization. The results are promising, and the model demonstrates strong potential for practical application, indicating that it can support business or research projects and even the establishment of a startup company. Continuous improvement and further validation are necessary due to intense competition in the field.
