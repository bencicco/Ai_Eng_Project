import os

def replace_data_with_dataset(input_file, output_file):
    """
    Process paths in text file:
    1. Replace 'data/' prefix with 'dataset/'
    2. Replace 'dataset/' prefix with 'data/' (new requirement)
    3. Remove folder_2/ or folder_4/ from the path
    
    Args:
        input_file: Path to the original file
        output_file: Path where the corrected file will be saved
    """
    try:
        # Read all lines from the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Count original lines
        original_count = len(lines)
        print(f"Read {original_count} lines from {input_file}")
        
        # Process each line
        fixed_lines = []
        for line in lines:
            line = line.strip()
            
            # Handle both Unix and Windows style paths - now CONVERTING dataset to data
            if line.startswith('dataset/'):
                # Replace 'dataset/' with 'data/'
                line = 'data/' + line[8:]  # 'dataset/' is 8 characters
            elif line.startswith('dataset\\'):
                # Handle Windows-style paths
                line = 'data\\' + line[8:]  # 'dataset\' is 8 characters
            elif line.startswith('data/'):
                # Already has 'data/' prefix, keep as is
                pass
            elif line.startswith('data\\'):
                # Already has 'data\' prefix, keep as is
                pass
            else:
                # No prefix, add 'data/' prefix
                line = 'data/' + line
            
            # Remove folder_2/ or folder_4/ from the path
            line = line.replace('/folder_2/', '/')
            line = line.replace('/folder_4/', '/')
            line = line.replace('\\folder_2\\', '\\')
            line = line.replace('\\folder_4\\', '\\')
            
            fixed_lines.append(line)
        
        # Write the corrected lines to the output file
        with open(output_file, 'w') as f:
            for line in fixed_lines:
                f.write(f"{line}\n")
        
        print(f"Successfully wrote {len(fixed_lines)} lines to {output_file}")
        print(f"\nYou can now replace {input_file} with {output_file} if everything looks good")
        
        # Show a sample of before and after
        print("\nSample of changes (first 3 lines):")
        for i in range(min(3, len(lines))):
            print(f"Original: {lines[i].strip()}")
            print(f"Fixed:    {fixed_lines[i]}")
            print()
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")

def replace_train_with_val(input_file, output_file):
    """
    Process paths in text file:
    1. Replace 'train' with 'val' in paths
    
    Args:
        input_file: Path to the original file
        output_file: Path where the corrected file will be saved
    """
    try:
        # Read all lines from the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Count original lines
        original_count = len(lines)
        print(f"Read {original_count} lines from {input_file}")
        
        # Process each line
        fixed_lines = []
        for line in lines:
            line = line.strip()
            
            # Replace 'train' with 'val' for both Unix and Windows style paths
            line = line.replace('/train/', '/val/')
            line = line.replace('\\train\\', '\\val\\')
            
            # For cases where train might be at the end of the path
            if line.endswith('/train'):
                line = line[:-6] + '/val'
            elif line.endswith('\\train'):
                line = line[:-6] + '\\val'
            
            fixed_lines.append(line)
        
        # Write the corrected lines to the output file
        with open(output_file, 'w') as f:
            for line in fixed_lines:
                f.write(f"{line}\n")
        
        print(f"Successfully wrote {len(fixed_lines)} lines to {output_file}")
        print(f"\nYou can now replace {input_file} with {output_file} if everything looks good")
        
        # Show a sample of before and after
        print("\nSample of changes (first 3 lines):")
        for i in range(min(3, len(lines))):
            print(f"Original: {lines[i].strip()}")
            print(f"Fixed:    {fixed_lines[i]}")
            print()
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")

if __name__ == "__main__":
    # Define file paths
    original_file = 'data/val_fixed.txt'
    corrected_file = 'val.txt'
    
    # Run the function
    replace_train_with_val(original_file, corrected_file)