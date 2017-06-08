import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import *

#converting to data frames
dw=pd.DataFrame()
d=[]
for i in xrange(1,20):
    with open('%i.txt' %i) as file:
        data=[]
        for line in file:
            s=line.split()
            data.append(s)
            
            d.append(pd.DataFrame(data))
#concating all the 20 data frames
dw=pd.concat(d)    
dw.columns= ['Distance','Vertical','Horizontal']
dw.index = range(4780506)
    

with open('3.txt') as file:
        data=[]
        for line in file:
            s=line.split()
            data.append(s)
ddfg=pd.DataFrame(data)
    #dw.shape[0]
ddfg.columns= ['Distance','Vertical','Horizontal']

ddfg    
a=[]    
for i in xrange(ddfg.shape[0]):
    if(float(ddfg.iloc[i,1])<0.0):
        a.append(-1)
    else:
        a.append(int(floor(float(ddfg.iloc[i,1])+0.5)))
    if(float(ddfg.iloc[i,2])<0.0):
        a.append(-1)
    else:
        a.append(int(floor(float(ddfg.iloc[i,2])+0.5)))
    #a.append(int(floor(float(ddfg.iloc[i,2])+0.5)))


    

distance_train=dw.iloc[:,0].to_frame()
labels_train=dw.iloc[:,1].to_frame()
labels_train2=dw.iloc[:,2].to_frame()

with open('7.txt') as file:
        data=[]
        for line in file:
            s=line.split()
            data.append(s)
ddfg=pd.DataFrame(data)
distance_test=ddfg.iloc[:,0].to_frame()
labels_test=ddfg.iloc[:,1].to_frame()
labels_test2=ddfg.iloc[:,2].to_frame()





from sklearn.linear_model import LinearRegression



reg_model = LinearRegression()
reg_model.fit(distance_train,labels_train)
reg_model2= LinearRegression()
reg_model2.fit(distance_train,labels_train)

plt.scatter(distance_train,labels_train, color = 'red')

plt.show()

plt.scatter(distance_train,labels_train2, color = 'red')
plt.plot(distance_train, reg_model2.predict(distance_train), color='blue')
plt.show()


labels_pred=reg_model.predict(distance_test)
labels_pred2=reg_model2.predict(distance_test)
b=[]

for i in xrange(609):
     if(float(labels_pred[i][0])<0.0):
        b.append(-1)
     else:
        b.append(int(floor(labels_pred[i][0]+0.5)))
     if(float(labels_pred2[i][0])<0.0):
        b.append(-1)
     else:
        b.append(int(floor(labels_pred2[i][0]+0.5)))
   

with open('final.txt','w') as file:
    for x in b:
        file.write(str(x) + '\n')
 
