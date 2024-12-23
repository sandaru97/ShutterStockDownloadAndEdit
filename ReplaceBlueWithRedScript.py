import cv2
import numpy as np
import os

def replace_blue_with_red(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Define blue color range
    lower_blue = np.array([100, 0, 0])  # Adjust these values
    upper_blue = np.array([255, 150, 150])  # Adjust these values
    
    # Create a mask for blue areas
    blue_mask = cv2.inRange(image, lower_blue, upper_blue)
    
    # Debug: Display the mask
    cv2.imshow("Blue Mask", blue_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Replace blue with red
    image[blue_mask > 0] = [0, 0, 255]  # Red in BGR

    # Save the modified image
    cv2.imwrite(output_path, image)

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.jpg'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            replace_blue_with_red(input_path, output_path)
            print(f"Processed: {file_name}")

# Specify input and output directories
input_folder = r"C:\Users\cashies\Desktop\Renamed Exercise Images"
output_folder = r"C:\Users\cashies\Desktop\Modified Exercise Images"

process_images(input_folder, output_folder)
