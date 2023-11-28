import cv2


image_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/download (2).jpeg" 
original_image = cv2.imread(image_path)


scale_factor_larger = 2
larger_image = cv2.resize(original_image, None, fx=scale_factor_larger, fy=scale_factor_larger, interpolation=cv2.INTER_LINEAR)


scale_factor_smaller = 0.5
smaller_image = cv2.resize(original_image, None, fx=scale_factor_smaller, fy=scale_factor_smaller, interpolation=cv2.INTER_LINEAR)


cv2.imshow('Original Image', original_image)
cv2.imshow('Larger Image', larger_image)
cv2.imshow('Smaller Image', smaller_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
