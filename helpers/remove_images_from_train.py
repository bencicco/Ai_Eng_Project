import os
import shutil
import sys

def move_images_back(destination_dir, source_dir):
    """
    Move all images from the destination directory back to the source directory.
    
    Args:
        destination_dir: Directory containing the copied images
        source_dir: Original source directory where to move images back to
    """
    # Ensure both directories exist
    if not os.path.isdir(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist")
        sys.exit(1)
    
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist")
        sys.exit(1)
    
    # Get list of all files in the destination directory
    image_files = [f for f in os.listdir(destination_dir) if os.path.isfile(os.path.join(destination_dir, f))]
    print(f"Found {len(image_files)} files in {destination_dir}")
    
    # Count for tracking progress
    moved_count = 0
    skipped_count = 0
    skipped_files = []
    
    # Process each file
    for image_file in image_files:
        dest_path = os.path.join(destination_dir, image_file)
        source_path = os.path.join(source_dir, image_file)
        
        # Check if file already exists in source directory
        if os.path.exists(source_path):
            # File exists in source, ask what to do
            print(f"\nFile '{image_file}' already exists in source directory.")
            print("Options: (o)verwrite, (s)kip, (q)uit")
            
            while True:
                choice = input("Your choice [o/s/q]: ").strip().lower()
                
                if choice == 'o':
                    # Overwrite the file
                    shutil.move(dest_path, source_path)
                    moved_count += 1
                    print(f"Overwritten: {image_file}")
                    break
                elif choice == 's':
                    # Skip this file
                    skipped_count += 1
                    skipped_files.append(image_file)
                    print(f"Skipped: {image_file}")
                    break
                elif choice == 'q':
                    # Quit the program
                    print("\nOperation aborted by user.")
                    print(f"Moved {moved_count} files, skipped {skipped_count} files")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter 'o', 's', or 'q'.")
        else:
            # File doesn't exist in source, safe to move
            shutil.move(dest_path, source_path)
            moved_count += 1
            
            # Progress update for every 100 files
            if moved_count % 100 == 0:
                print(f"Progress: Moved {moved_count} images so far")
    
    # Print summary
    print(f"\nComplete! Moved {moved_count} images back to {source_dir}")
    if skipped_count > 0:
        print(f"Skipped {skipped_count} images that already existed in the source")
        
        # Print skipped files (up to 10) if any
        print("\nSkipped files:")
        for i, skipped in enumerate(skipped_files[:10]):
            print(f"  - {skipped}")
        if len(skipped_files) > 10:
            print(f"  ... and {len(skipped_files) - 10} more")

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python move_images_back.py <destination_dir> <source_dir>")
        print("  <destination_dir>: Directory containing the copied images")
        print("  <source_dir>: Original source directory where to move images back to")
        sys.exit(1)
    
    # Get arguments
    destination_dir = sys.argv[1]
    source_dir = sys.argv[2]
    
    # Run the function
    move_images_back(destination_dir, source_dir)