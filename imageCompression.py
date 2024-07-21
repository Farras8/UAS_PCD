import cv2
import os

# Baca gambar dari file
img = cv2.imread('pcd.jpeg')

# Simpan gambar dengan kompresi lossless (format PNG)
cv2.imwrite('lossless_compressed_image.png', img)

# Simpan gambar dengan kompresi lossy (format JPEG) dengan kualitas 90
# (Nilai antara 0 dan 100, nilai lebih tinggi berarti kualitas lebih baik tetapi ukuran file lebih besar)
jpeg_quality = 90
cv2.imwrite('lossy_compressed_image.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])

# Hitung ukuran file asli dan file yang terkompresi
original_size = os.path.getsize('pcd.jpeg')
lossless_size = os.path.getsize('lossless_compressed_image.png')
lossy_size = os.path.getsize('lossy_compressed_image.jpg')

# Tampilkan ukuran file
print(f'Original image size: {original_size} bytes')
print(f'Lossless compressed image size: {lossless_size} bytes')
print(f'Lossy compressed image size: {lossy_size} bytes')

# Baca kembali gambar yang telah disimpan
lossless_img = cv2.imread('lossless_compressed_image.png')
lossy_img = cv2.imread('lossy_compressed_image.jpg')

# Tampilkan gambar asli, terkompresi lossless, dan terkompresi lossy
cv2.imshow('Original Image', img)
cv2.imshow('Lossless Compressed Image', lossless_img)
cv2.imshow('Lossy Compressed Image', lossy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
