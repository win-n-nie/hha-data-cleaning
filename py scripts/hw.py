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

