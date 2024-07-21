# Importing the required libraries
import cv2
import numpy as np

# Converting types to binary
def msg_to_bin(msg):
    if isinstance(msg, str):
        return ''.join([format(ord(i), "08b") for i in msg])
    elif isinstance(msg, (bytes, np.ndarray)):
        return [format(i, "08b") for i in msg]
    elif isinstance(msg, (int, np.uint8)):
        return format(msg, "08b")
    else:
        raise TypeError("Input type not supported")

# Defining function to hide the secret message into the image
def hide_data(img, secret_msg):
    # Calculating the maximum bytes for encoding
    nBytes = img.shape[0] * img.shape[1] * 3 // 8
    print("Maximum Bytes for encoding:", nBytes)
    
    # Checking whether the number of bytes for encoding is less than the maximum bytes in the image
    if len(secret_msg) > nBytes:
        raise ValueError("Error encountered: insufficient bytes, need bigger image or less data!!")
    
    secret_msg += '#####'  # We can utilize any string as the delimiter
    dataIndex = 0
    
    # Converting the input data to binary format using the msg_to_bin() function
    bin_secret_msg = msg_to_bin(secret_msg)
    
    # Finding the length of data that needs to be hidden
    dataLen = len(bin_secret_msg)
    
    for values in img:
        for pixels in values:
            # Converting RGB values to binary format
            r, g, b = msg_to_bin(pixels)
            
            # Modifying the LSB only if there is data remaining to store
            if dataIndex < dataLen:
                # Hiding the data into LSB of Red pixel
                pixels[0] = int(r[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            if dataIndex < dataLen:
                # Hiding the data into LSB of Green pixel
                pixels[1] = int(g[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            if dataIndex < dataLen:
                # Hiding the data into LSB of Blue pixel
                pixels[2] = int(b[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            
            # If data is encoded, break out of the loop
            if dataIndex >= dataLen:
                break
    
    return img

def show_data(img):
    bin_data = ""
    
    for values in img:
        for pixels in values:
            # Converting the Red, Green, Blue values into binary format
            r, g, b = msg_to_bin(pixels)
            
            # Data extraction from the LSB of Red, Green, and Blue pixels
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]
    
    # Split by 8-bits
    allBytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
    
    # Converting from bits to characters
    decodedData = ""
    for bytes in allBytes:
        decodedData += chr(int(bytes, 2))
    
    # Checking if we have reached the delimiter which is "#####"
    if decodedData[-5:] == "#####":
        return decodedData[:-5]  # Removing the delimiter to display the actual hidden message
    
    return decodedData

# Defining function to encode data into Image
def encodeText():
    img_name = "pcd.jpeg"  # Fixed image name
    # Reading the input image using OpenCV-Python
    img = cv2.imread(img_name)
    
    if img is None:
        raise FileNotFoundError("Image not found. Please check the file path.")
    
    # Printing the details of the image
    print("The shape of the image is: ", img.shape)  # Checking the image shape to calculate the number of bytes in it
    print("The original image is as shown below: ")
    
    # Resizing the image as per the need
    resizedImg = cv2.resize(img, (500, 500))
    # Displaying the image
    cv2.imshow("Original Image", resizedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    data = input("Enter data to be encoded: ")
    if len(data) == 0:
        raise ValueError('Data is Empty')
    
    file_name = input("Enter the name of the new encoded image (with extension): ")
    # Calling the hide_data() function to hide the secret message into the selected image
    encodedImage = hide_data(img, data)
    cv2.imwrite(file_name, encodedImage)

# Defining the function to decode the data in the image
def decodeText():
    # Reading the image containing the hidden message
    img_name = input("Enter the name of the Steganographic image that has to be decoded (with extension): ")
    img = cv2.imread(img_name)  # Reading the image using the imread() function
    
    if img is None:
        raise FileNotFoundError("Image not found. Please check the file path.")
    
    print("The Steganographic image is as follow: ")
    resizedImg = cv2.resize(img, (500, 500))  # Resizing the actual image as per the needs
    cv2.imshow("Steganographic Image", resizedImg)  # Displaying the Steganographic image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    text = show_data(img)
    return text

# Image steganography
def steganography():
    n = int(input("Image Steganography \n1. Encode the data \n2. Decode the data \nSelect the option: "))
    if n == 1:
        print("\nEncoding...")
        encodeText()
    elif n == 2:
        print("\nDecoding...")
        print("Decoded message is: " + decodeText())
    else:
        raise ValueError("Inserted value is incorrect!")

steganography()  # Run the steganography function
