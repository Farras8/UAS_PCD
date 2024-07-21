import cv2

# Baca gambar input RGB sebagai format BGR
bgr_img = cv2.imread('pcd.jpeg')

# Periksa apakah gambar berhasil dibaca
if bgr_img is None:
    print('Could not open or find the image: pcd.jpeg')
    exit(0)

# Konversi gambar BGR ke HSV
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

# Simpan gambar hasil konversi
cv2.imwrite('hsv_image.jpeg', hsv_img)

# Tampilkan gambar HSV
cv2.imshow('HSV image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
