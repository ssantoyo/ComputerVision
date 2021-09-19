import cv2


img = cv2.imread('FlowerBoy.jpeg', 0)
#resize dimensions of image
img = cv2.resize(img, (0,0), fx=2, fy=2)
#rotates the images by 90 in different orientations
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
#stores writable changes in new files (img)
cv2.imwrite('new_img.jpeg', img)

#displays the image
cv2.imshow('Image', img)
#set how many sec image appears, set to 0(infinite)
cv2.waitKey(0)
#closes all windows
cv2.destroyAllWindows()
