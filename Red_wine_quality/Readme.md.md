# Red Wine Quality Prediction Machine Learning Model

by: Sanket Sharma, Email: ur.sanketsharma@gmail.com, Linkedin: https://www.linkedin.com/in/ursanketsharma/


## Introduction
Dataset used for this project is Red wine Quality data set from UCI machine learning library which is also available on Kaggle (https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009). Each wine in this dataset is given a “quality” score between 0 and 10. For the purpose of this project, I converted the output to “good quality” (a score of 7 or higher), "avarage quality"(a score greater than 5 and leass than 7) and "poor quality" (score below 5).

The quality of a wine is determined by 11 Features:
1. Fixed acidity
2. Volatile acidity
3. Citric acid
4. Residual sugar
5. Chlorides
6. Free sulfur dioxide
7. Total sulfur dioxide
8. Density
9. pH
10. Sulfates
11. Alcohol

## Objective
To experiment with different classification methods to see which yields the highest accuracy and choose the one with highest accuracy to build a prediction app in python.

## Setup
I have used below python libraries for EDA and Model building
- numpy
- pandas
- matplotlib.pyplot
- seaborn
- sklearn
- pickle

For frontend i have used:
- streamlit

## Model Evaluation:
Models have been evaluated against accuracy score. Different accuracy scores achieved by diffrent model are as follows in descending order:

| Model        | Accuracy Score |
|--------------|----------------|
| ExtraTrees   | 0.884375       |
| RandomForest | 0.865625       |
| GBC          | 0.850000       |
| GNB          | 0.815625       |
| DecisionTree | 0.784375       |
| AdaBoost     | 0.728125       |

Finally selected "Extratrees" with highest accuracy score for predictions.
