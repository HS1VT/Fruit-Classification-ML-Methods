import pandas as pd
import math
data_frame = pd.read_csv('fruits.csv')

x = data_frame.iloc[:,[1,2,3]].values
y = data_frame.iloc[:,0].values
fruit=[]
final=[]
r=[]
g=[]
b=[]
init=y[0]
red=0
green=0
blue=0
count=0
for j in range(0,len(y)):
    if y[j]==init:
        red=red+x[j][0]
        green=green+x[j][1]
        blue=blue+x[j][2]
    else:
        final.append([red,blue,green])
        init=y[j]
        red=0
        green=0
        blue=0

print(len(final))

