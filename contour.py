import matplotlib.pyplot as plt
import numpy as np
import cv2

# Membaca gambar dan mengubah ukurannya
sample_image = cv2.imread('pcd.jpeg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))
plt.axis('off')
plt.imshow(img)
plt.title('Gambar Asli')
plt.show()

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.axis('off')
plt.imshow(gray, cmap='gray')
plt.title('Gambar Grayscale')
plt.show()

# Thresholding untuk segmentasi biner
_, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
plt.axis('off')
plt.imshow(thresh, cmap='gray')
plt.title('Gambar Thresholding')
plt.show()

# Deteksi tepi dan dilasi untuk memperbaiki kontur
edges = cv2.dilate(cv2.Canny(thresh, 0, 255), None)
plt.axis('off')
plt.imshow(edges, cmap='gray')
plt.title('Deteksi  Dilasi')
plt.show()

# Mencari kontur dan memilih kontur terbesar
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    cnt = max(contours, key=cv2.contourArea)
else:
    raise ValueError("Tidak ada kontur yang ditemukan")

# Membuat masker dan menggambar kontur pada masker
mask = np.zeros((256, 256), np.uint8)
masked = cv2.drawContours(mask, [cnt], -1, 255, -1)
plt.axis('off')
plt.imshow(mask, cmap='gray')
plt.title('Contour Detection')
plt.show()

# Mengaplikasikan masker pada gambar asli
dst = cv2.bitwise_and(img, img, mask=mask)
segmented = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(segmented)
plt.title('Gambar Tersegmentasi')
plt.show()
