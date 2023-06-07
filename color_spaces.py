import cv2

# program to conver the input image into different color spaces (GRAY, YUV, HSV)
img = cv2.imread("D:\projects\learningopencv\scene.jpg")
converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale image', converted_img)
cv2.waitKey()