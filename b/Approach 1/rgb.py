import cv2
import numpy as np  
import os

file1 = open("fruits.txt","a")
directory = 'Watermelon'

r=0
g=0
b=0
count=0

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
    file1.write('Watermelon,')
    file1.write(str(r)+','+str(g)+','+str(b)+'\n')
    r=0
    b=0
    g=0
    count=0

        
