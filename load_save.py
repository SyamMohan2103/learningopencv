import cv2

# read and image in gray scale and save the image
gray_img = cv2.imread("D:\projects\learningopencv\scene.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale',gray_img)
cv2.imwrite('gray_scene.jpg', gray_img)
cv2.waitKey()