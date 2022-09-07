import pandas as pd
import datetime as dt 
import uuid ### creates unique identifier 
import numpy as np ### deals with special values

df = pd.read_csv('/Users/wendyarias/Downloads/School_Learning_Modalities.csv')
df
df.shape

df.columns
df.columns = df.columns.str.lower()

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex , seperate type of programming language for dealing with strings, first part is what we were looking for second part is what we replace with
list(df)

df.dtypes


numbers = df.select_dtypes(include=['int64', 'float64']).columns
numbers
df.isnull().sum()

df2 = df.rename(columns= {'learning_modality' : 'modality_inperson'})
list(df2)

df2['modality_inperson'] = df2['modality_inperson'].map({'In Person' :True , 'Hybrid' :False , 'Remote' :False})
df2['modality_inperson']

