import cv2

img = cv2.imread('FlowerBoy.jpeg', -1)

#channels run in BGR (blue, green, red) [0,0,0]
print(type(img))