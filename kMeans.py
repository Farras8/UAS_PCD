import matplotlib.pyplot as plt
import numpy as np
import cv2

# Membaca gambar
sample_image = cv2.imread('pcd.jpeg')

# Periksa jika gambar berhasil dibaca
if sample_image is None:
    raise ValueError("Gambar tidak ditemukan atau tidak dapat dibaca.")

# Mengubah dari BGR ke RGB
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

# Mengubah gambar menjadi array 2D
twoDimage = img.reshape((-1, 3))
twoDimage = np.float32(twoDimage)

# Kriteria dan parameter K-Means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 6
attempts = 10

# Menerapkan K-Means
ret, label, center = cv2.kmeans(twoDimage, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)

# Mengubah center ke uint8
center = np.uint8(center)

# Membangun hasil gambar
res = center[label.flatten()]
result_image = res.reshape((img.shape))

# Menampilkan gambar hasil segmentasi
plt.imshow(result_image)
plt.title('Hasil K = 6')
plt.axis('off')
plt.show()
