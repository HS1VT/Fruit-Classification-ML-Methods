First I stored the images in x_train and labels corresponding to those images in y_train lists. We used the test_train_split to split the test and train images to make the x_test and y_test lists.
I converted the image from x*y*z*3 to greyscale and converted them into size 32x32 so to make it as x*32*32*1.
After feeding in keras model and after running 13 epoch, I got an accuracy of 62.5%.
After evaluating, the final accuracy was 59.29%
Collaborator: Shaleen Malik (12041360)