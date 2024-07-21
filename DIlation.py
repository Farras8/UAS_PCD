import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image 
img = cv2.imread(r"pcd.jpeg", 0) 

# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] 

# define the kernel 
kernel = np.ones((3, 3), np.uint8) 

# invert the image 
invert = cv2.bitwise_not(binr) 

# dilate the image 
dilation = cv2.dilate(invert, kernel, iterations=1) 

# print the output 
plt.imshow(dilation, cmap='gray')
plt.axis('off')  # Optionally hide the axis
plt.show()  # Display the image
