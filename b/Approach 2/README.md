First I extracted all the features in the same way as in approach 1 using rgb.py. Then I made a vector of all the images which contained the r,g and b values like <r,g,b>. Now we made a vector of the test image (watermelon in the case of test) in the same way like <r,g,b>. We also use the HOG features (as shown in code).
Now we find the euclidean distance between the vector of test image from all the other images and store them in a list. We then find the 11 distances (K=11) that are least and then store it in a list with their label. Now we compare the labels of the list from the label of the test image and then find the accuracy of the predicted image.

NOTE: while loading the .ipynb in colab, upload the fruits.csv and wat_test.jpg in the resources.