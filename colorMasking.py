import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca gambar
sample_image = cv2.imread('pcd.jpeg')

# Mengubah dari BGR ke RGB
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

# Menampilkan gambar asli
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.axis('off')
plt.title('Gambar Asli')
plt.imshow(img)

# Mendefinisikan rentang warna rendah dan tinggi untuk masking
low = np.array([0, 0, 0])
high = np.array([215, 51, 51])

# Membuat masker
mask = cv2.inRange(img, low, high)

# Menampilkan masker
plt.subplot(1, 3, 2)
plt.axis('off')
plt.title('Masker Warna')
plt.imshow(mask, cmap='gray')

# Menerapkan masker pada gambar
result = cv2.bitwise_and(img, img, mask=mask)

# Menampilkan hasil masking
plt.subplot(1, 3, 3)
plt.axis('off')
plt.title('Hasil Color Masking')
plt.imshow(result)

# Menampilkan semua plot
plt.tight_layout()
plt.show()
