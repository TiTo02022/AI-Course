import pandas as pd
import numpy as np


adult=pd.read_csv('adult.csv')
pd.options.display.max_columns=50
pd.options.display.max_rows=100
#print(adult.head(10)) #1
#print(adult.tail(10)) #2
#print(adult.shape) #3
#print(adult.info) #4
print(adult.sample(frac=0.5, random_state=42))


