import pandas as pd
import pickle
from paths import csv_path, model_path
from sklearn.linear_model import LinearRegression

data = pd.read_csv(csv_path)
x, y = data[['YearsExperience']], data[['Salary']]

model = LinearRegression()
model.fit(x, y)
pickle.dump(model, open(model_path, 'wb'))