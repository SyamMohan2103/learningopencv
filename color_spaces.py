import cv2

# program to conver the input image into different color spaces (GRAY, YUV, HSV)
img = cv2.imread("D:\projects\learningopencv\scene.jpg")
converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow('Y_channel', converted_img[:,:, 0])
cv2.imshow('U_channel', converted_img[:,:, 1])
cv2.imshow('V_channel', converted_img[:,:, 2])
cv2.imshow('YUV image', converted_img)
cv2.waitKey()