# Import required libraries
import cv2

# Read the image on which we are going to apply watermark
img = cv2.imread("pcd.jpeg")

# Read the watermark image
wm = cv2.imread("watermark.jpg")

# Get height and width of the watermark image
h_wm, w_wm = wm.shape[:2]

# Get height and width of the image
h_img, w_img = img.shape[:2]

# Calculate coordinates of the center of the image
center_x = int(w_img / 2)
center_y = int(h_img / 2)

# Calculate the region of interest (ROI) from top, bottom, right, and left
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

# Ensure ROI is within image bounds
top_y = max(top_y, 0)
left_x = max(left_x, 0)
bottom_y = min(bottom_y, h_img)
right_x = min(right_x, w_img)

# Resize watermark if it's larger than the image
if h_wm > (bottom_y - top_y) or w_wm > (right_x - left_x):
    wm = cv2.resize(wm, (right_x - left_x, bottom_y - top_y))

# Add watermark to the image
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result

# Display the watermarked image
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
