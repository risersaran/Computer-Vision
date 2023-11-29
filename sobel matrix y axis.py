import cv2
import numpy as np

# Read the input image
image = cv2.imread("C:/Users/dinak/OneDrive/Pictures/Camera imports/HD-wallpaper-nature-scenery-scenery-nature.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter along the Y-axis
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Convert the result to uint8
sobel_y = np.uint8(np.absolute(sobel_y))

# Display the original and Sobel Y images
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()

