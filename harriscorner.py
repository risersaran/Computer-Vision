import cv2
import numpy as np
image_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/HD-wallpaper-nature-scenery-scenery-nature.jpg" 
original_image = cv2.imread(image_path)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
corner_image = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
threshold = 0.01 * corner_image.max()
corner_image[corner_image < threshold] = 0
dilated_corners = cv2.dilate(corner_image, None)
original_image[dilated_corners > 0.01 * dilated_corners.max()] = [0, 0, 255]  # Red color for corners
cv2.imshow('Corners Detected', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
