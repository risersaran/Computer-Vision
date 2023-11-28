import cv2


image_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/HD-wallpaper-nature-scenery-scenery-nature.jpg"
original_image = cv2.imread(image_path)


rotated_image = cv2.transpose(original_image)
rotated_image = cv2.flip(rotated_image, flipCode=1)  


cv2.imshow('Original Image', original_image)
cv2.imshow('Rotated Image', rotated_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
