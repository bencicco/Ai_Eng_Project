import os
import shutil
import random
from math import ceil



def split_images_into_folders(source_folder, dest_base_folder, num_folders=6):
    """
    Split images from source_folder into num_folders equal folders.
    
    Parameters:
    - source_folder: Path to the folder containing images
    - dest_base_folder: Base path where to create the destination folders
    - num_folders: Number of equal folders to create (default: 6)
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    image_files = []
    
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in image_extensions:
                image_files.append(file)
        random.shuffle(image_files)
    
    # Calculate how many images per folder
    total_images = len(image_files)
    images_per_folder = ceil(total_images / num_folders)
    
    print(f"Found {total_images} images. Will distribute ~{images_per_folder} images per folder.")
    
    # Create destination folders if they don't exist
    dest_folders = []
    for i in range(1, num_folders + 1):
        folder_name = os.path.join(dest_base_folder, f"folder_{i}")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        dest_folders.append(folder_name)
    
    # Distribute files to folders
    for i, image_file in enumerate(image_files):
        folder_index = min(i // images_per_folder, num_folders - 1)
        source_path = os.path.join(source_folder, image_file)
        dest_path = os.path.join(dest_folders[folder_index], image_file)
        shutil.copy2(source_path, dest_path)
        
    # Print summary
    for i, folder in enumerate(dest_folders, 1):
        folder_files = os.listdir(folder)
        print(f"Folder {i}: {len(folder_files)} images")

if __name__ == "__main__":
    # Set your source and destination folders here
    source_folder = "rubbish"
    dest_base_folder = "rubbish_split"
    
    # Run the function
    split_images_into_folders(source_folder, dest_base_folder)