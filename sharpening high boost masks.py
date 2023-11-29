import cv2
import numpy as np

# Read the input image
original_image = cv2.imread("C:/Users/dinak/OneDrive/Pictures/Camera imports/download (2).jpeg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Set the boost factor (adjust as needed)
boost_factor = 2.0

# Perform high-boost filtering
result = cv2.addWeighted(gray_image, 1 + boost_factor, blurred_image, -boost_factor, 0)

# Convert the result back to BGR for display
result_bgr = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

# Display the original and sharpened images
cv2.imshow("Original Image", original_image)
cv2.imshow("Sharpened Image", result_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
