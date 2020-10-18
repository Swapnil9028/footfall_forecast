# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv(r'C:\Users\Ishan Ambasta\Desktop\Artefact\Abhinav\Arimax_v3_wo_covid_v2.csv')
x=dataset[['Imp Festivals', 'Less Imp Festivals', 'No Holiday', 'weekend','noofEvents', 'campaignPriority', 'marketingSpend']]
y=dataset[['Visitors']]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(x, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,0,29,13,1,1,20000]]))

