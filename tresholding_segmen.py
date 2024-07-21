import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import cv2

# Membaca gambar dan mengubah format
sample_image = cv2.imread('pcd.jpeg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img)
plt.title('Gambar Asli')
plt.show()

# Mengubah gambar ke grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Menerapkan threshold Otsu
thresh = threshold_otsu(img_gray)
img_otsu = img_gray < thresh
plt.axis('off')
plt.imshow(img_otsu, cmap='gray')
plt.title('Hasil Threshold Otsu')
plt.show()

# Fungsi untuk menerapkan masker pada gambar
def filter_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask
    return np.dstack([r, g, b])

# Menerapkan masker pada gambar
filtered = filter_image(img, img_otsu)
plt.axis('off')
plt.imshow(filtered)
plt.title('Gambar Terfilter')
plt.show()
