import cv2
import numpy as np

# Read the input image
image = cv2.imread("C:/Users/dinak/OneDrive/Pictures/Camera imports/HD-wallpaper-nature-scenery-scenery-nature.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter along the X-axis
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter along the Y-axis
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the absolute values of Sobel X and Sobel Y
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# Convert the result to uint8
sobel_combined = np.uint8(sobel_combined)

# Display the original and combined Sobel images
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Combined (XY)", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
