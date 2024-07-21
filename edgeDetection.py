import cv2
import numpy as np

# Load the image
img = cv2.imread('pcd.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny method
edges = cv2.Canny(gray, 150, 300)

# Create a copy of the original image to display edges
img_with_edges = img.copy()
img_with_edges[edges == 255] = (255, 0, 0)

# Stack the original image and the edge-detected image horizontally
combined_image = np.hstack((img, img_with_edges))

# Display the combined image
cv2.imshow('Original and Canny Edges', combined_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
