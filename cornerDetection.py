import cv2
import numpy as np

# Load the image
img = cv2.imread('pcd.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners using the Harris method
dst = cv2.cornerHarris(gray, 3, 5, 0.1)

# Create a boolean bitmap of corner positions
corners = dst > 0.05 * dst.max()

# Find the coordinates from the boolean bitmap
coord = np.argwhere(corners)

# Draw circles on the coordinates to mark the corners
for y, x in coord:
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

# Display the image with corners
cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()