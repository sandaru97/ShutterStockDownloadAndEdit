import os
import re

def rename_files_and_create_folder(source_directory, target_directory):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Iterate through all files in the specified source directory
    for filename in os.listdir(source_directory):
        if filename.endswith(".jpg"):
            # Use regex to extract the exercise name
            match = re.search(r'man-doing-(.*?)-\d+nw', filename)
            if match:
                # Extract the exercise name and clean up
                exercise_name = match.group(1).replace('-', ' ')
                new_name = f"{exercise_name}.jpg"

                # Create full paths
                old_file = os.path.join(source_directory, filename)
                new_file = os.path.join(target_directory, new_name)

                # Copy and rename the file to the new directory
                with open(old_file, 'rb') as f_src, open(new_file, 'wb') as f_dst:
                    f_dst.write(f_src.read())
                print(f"Copied and renamed: {filename} -> {new_name}")
            else:
                print(f"Skipping file (no match): {filename}")

# Specify the source and target directories
source_directory = r"C:\Users\cashies\Desktop\Lio Putra Shutterstock exercise images"  # Replace with the path to your source directory
target_directory = r"C:\Users\cashies\Desktop\Renamed Exercise Images"  # Replace with the path to your target directory
rename_files_and_create_folder(source_directory, target_directory)
