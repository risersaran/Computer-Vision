import cv2
import numpy as np
def add_watermark(original_image_path, watermark_text, output_path):
    original_img = cv2.imread(original_image_path)
    height, width = original_img.shape[:2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  
    overlay = np.zeros((height, width, 3), dtype=np.uint8)
    (text_width, text_height), baseline = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
    x_position = int((width - text_width) / 2)
    y_position = int((height + text_height) / 2)
    cv2.putText(overlay, watermark_text, (x_position, y_position), font, font_scale, font_color, font_thickness, cv2.LINE_AA)
    alpha = 0.5 
    watermarked_image = cv2.addWeighted(original_img, 1, overlay, alpha, 0)
    cv2.imwrite(output_path, watermarked_image)
    cv2.imshow('Watermarked Image', watermarked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
original_image_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/German-Shepherd-dog-Alsatian.webp"
watermark_text = 'German sheperd'
output_path = "C:/Users/dinak/OneDrive/Pictures/Camera imports/German-Shepherd-dog-Alsatian.webp"
add_watermark(original_image_path, watermark_text, output_path)
