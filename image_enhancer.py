import cv2
import numpy as np

def enhance_visible_with_infrared(visible_path, infrared_path, output_path):
    # Load visible and infrared images
    visible_img = cv2.imread(visible_path)
    infrared_img = cv2.imread(infrared_path, cv2.IMREAD_GRAYSCALE)

    # Resize infrared image to match visible image size if necessary
    infrared_img = cv2.resize(infrared_img, (visible_img.shape[1], visible_img.shape[0]))

    # Convert the visible image to LAB color space
    visible_lab = cv2.cvtColor(visible_img, cv2.COLOR_BGR2LAB)

    # Extract the L channel from the LAB color space
    l_channel = visible_lab[:, :, 0]

    # Enhance the L channel using the infrared image
    enhanced_l_channel = cv2.addWeighted(l_channel, 0.5, infrared_img, 0.5, 0)

    # Replace the original L channel with the enhanced one
    visible_lab[:, :, 0] = enhanced_l_channel

    # Convert the enhanced LAB image back to BGR color space
    enhanced_visible_img = cv2.cvtColor(visible_lab, cv2.COLOR_LAB2BGR)

    # Save the enhanced visible image
    return enhanced_visible_img

visible_image_path = "visible.bmp"
infrared_image_path = "infrared.bmp"
# Replace this path with the desired output path for the enhanced visible image
output_image_path = "enhanced_image.bmp"
enhance_visible_with_infrared(visible_image_path, infrared_image_path, output_image_path)