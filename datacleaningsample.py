import pandas as pd
import numpy as np

with open('TestLog.txt') as file:
        i=0
        data=[]
        for line in file:
            s=line.split()
            data.append(s)
data_df = pd.DataFrame(data)
data_df.columns= ['Distance','Vertical','Horizontal']
data_df
