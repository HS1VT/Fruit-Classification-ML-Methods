If we run the model on all the 68,000+ images again and again then it is going to take a long time. So, I have extracted the features and stored them in a CSV and then  run the code on it, in this way the entire operation is completed in a few seconds. 

We extract the features from a file called rgb.py 
rgb.py extaracts the RGB value of all the image of a given class (we'll have to enter the classes independently) and stores it in a file called fruits.txt. We then convert the .txt file to .csv and rename to Fruit_360.csv.
rgb.py calculates the value of each pixel and averages it out to get final values for a given image.

KNN_1.ipynb uses sklearn library and computes the accuracy of all the fruits at the end with a total accuracy of around 90%. I have also done the KNN without using any library which is in the Approach 2 folder.
The code is properly commented at all places required.