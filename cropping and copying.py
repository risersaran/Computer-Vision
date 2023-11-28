import cv2

# Function to crop and paste region of interest (ROI)
def crop_and_paste(source_image_path, destination_image_path, x, y, width, height):
    # Read the source image
    source_image = cv2.imread(source_image_path)

    # Extract the region of interest (ROI)
    roi = source_image[y:y+height, x:x+width]

    # Create a blank destination image with the same size as the ROI
    destination_image = 255 * np.ones_like(roi, dtype=np.uint8)

    # Paste the ROI onto the destination image
    destination_image[0:height, 0:width] = roi

    # Save the result
    cv2.imwrite(destination_image_path, destination_image)

# Example usage
source_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/download (2).jpeg"
destination_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/download (2).jpeg"

# Specify the region of interest (x, y, width, height)
x = 100
y = 50
width = 200
height = 150

crop_and_paste(source_path, destination_path, x, y, width, height)
