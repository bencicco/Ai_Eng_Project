import os
import shutil
import sys

def extract_image_names_and_copy(list_file, source_dir1, source_dir2, destination_dir):
    """
    Extract image filenames from a text file and copy those images from multiple source directories to destination.
    
    Args:
        list_file: Text file containing image paths like 'data/obj_train_data/folder_1/image.jpg'
        source_dir1: First directory containing the actual images
        source_dir2: Second directory containing the actual images
        destination_dir: Directory where to copy the images
    """
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)
    
    # Count for tracking progress
    copied_count = 0
    not_found_count = 0
    not_found_files = []
    source1_count = 0
    source2_count = 0
    
    # Read the file paths from the text file
    with open(list_file, 'r') as f:
        file_paths = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(file_paths)} image paths in {list_file}")
    
    # Process each file path
    for file_path in file_paths:
        # Extract just the filename (ignore directory structure in the text file)
        image_name = os.path.basename(file_path)
        
        # Look for the image in the first source directory
        source_path1 = os.path.join(source_dir1, image_name)
        
        # Look for the image in the second source directory
        source_path2 = os.path.join(source_dir2, image_name)
        
        # Check if the image exists in either source directory
        if os.path.exists(source_path1):
            # Image found in first source directory, copy it
            destination_path = os.path.join(destination_dir, image_name)
            shutil.copy2(source_path1, destination_path)
            copied_count += 1
            source1_count += 1
            
            # Progress update for every 100 files
            if copied_count % 100 == 0:
                print(f"Progress: Copied {copied_count} images so far")
        
        elif os.path.exists(source_path2):
            # Image found in second source directory, copy it
            destination_path = os.path.join(destination_dir, image_name)
            shutil.copy2(source_path2, destination_path)
            copied_count += 1
            source2_count += 1
            
            # Progress update for every 100 files
            if copied_count % 100 == 0:
                print(f"Progress: Copied {copied_count} images so far")
        
        else:
            # Image not found in either source directory
            not_found_count += 1
            not_found_files.append(image_name)
    
    # Print summary
    print(f"\nComplete! Copied {copied_count} images to {destination_dir}")
    print(f"Found {source1_count} images in first source directory ({source_dir1})")
    print(f"Found {source2_count} images in second source directory ({source_dir2})")
    print(f"Could not find {not_found_count} images in either source directory")
    
    # Print missing files (up to 10) if any
    if not_found_count > 0:
        print("\nSome images were not found. First few missing files:")
        for i, missing in enumerate(not_found_files[:10]):
            print(f"  - {missing}")
        if not_found_count > 10:
            print(f"  ... and {not_found_count - 10} more")

if __name__ == "__main__":
    # Define default paths
    list_file = 'Folder5Annotations/train.txt'
    source_dir1 = 'data/images/folder_5'
    source_dir2 = 'data/images/folder_2'
    destination_dir = 'data/images/train'
    
    # Validate file and directories exist
    if not os.path.isfile(list_file):
        print(f"Error: List file '{list_file}' does not exist")
        sys.exit(1)
    
    # Check at least one source directory exists
    if not os.path.isdir(source_dir1) and not os.path.isdir(source_dir2):
        print(f"Error: Both source directories don't exist. At least one must exist.")
        sys.exit(1)
    
    # Warn if one directory is missing but continue with the other
    if not os.path.isdir(source_dir1):
        print(f"Warning: First source directory '{source_dir1}' does not exist. Will only check the second directory.")
    
    if not os.path.isdir(source_dir2):
        print(f"Warning: Second source directory '{source_dir2}' does not exist. Will only check the first directory.")
    
    # All validations passed, run the function
    extract_image_names_and_copy(list_file, source_dir1, source_dir2, destination_dir)