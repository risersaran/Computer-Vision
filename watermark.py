import cv2
import numpy as np

def add_watermark(original_image_path, watermark_image_path, output_image_path, position=(0, 0), transparency=0.3):
    # Read the original image and the watermark image
    original_image = cv2.imread(original_image_path)
    watermark_image = cv2.imread(watermark_image_path, cv2.IMREAD_UNCHANGED)

    # Resize watermark image to fit the original image
    watermark_image = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))

    # Split the watermark image into channels
    b, g, r, alpha = cv2.split(watermark_image)

    # Normalize alpha channel to range [0, 1]
    alpha = alpha / 255.0

    # Blend the images using alpha blending
    blended_image = cv2.addWeighted(original_image, 1.0, cv2.merge((b, g, r)), 1.0 - alpha, 0)

    # Save the output image
    cv2.imwrite(output_image_path, blended_image)

if __name__ == "__main__":
    original_image_path = "path/to/original/image.jpg"
    watermark_image_path = "path/to/watermark/logo.png"
    output_image_path = "path/to/output/result.jpg"

    add_watermark(original_image_path, watermark_image_path, output_image_path)
