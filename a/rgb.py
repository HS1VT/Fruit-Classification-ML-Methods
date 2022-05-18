import cv2
import numpy as np  
import os

file1 = open("fruits_avg.csv","a")
directory = 'Watermelon'

r=0
g=0
b=0
count=0
red=[]
green=[]
blue=[]

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        cap=cv2.imread(f)
        for x in range (0,100,1):
            for y in range(0,100,1):
                color = cap[y,x]
                r=r+color[0]
                g=g+color[1]
                b=b+color[2]
                count=count+1
    r=r/count
    b=b/count
    g=g/count
    red.append(r)
    green.append(g)
    blue.append(b)
    r=0
    b=0
    g=0
    count=0
r_f=0
b_f=0
g_f=0
for i in range(0,len(red)):
    r_f=r_f+red[i]
    b_f-b_f+blue[i]
    g_f=g_f+green[i]

file1.write('Watermelon,')
file1.write(str(r_f)+','+str(g_f)+','+str(b_f)+'\n')

        
