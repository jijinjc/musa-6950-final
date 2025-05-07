import os

def rename_images_in_folders(root_directory):
    """
    Renames all JPG images in subfolders of root_directory according to the specified pattern.
    New filename will be: [folder_name]_[last_part_after_split].jpg
    """
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)
        
        # Skip if not a directory
        if not os.path.isdir(folder_path):
            continue
            
        # Process each file in the folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith('.jpg'):
                # Split the filename by underscores
                parts = filename.split('_')
                
                if len(parts) > 1:
                    # Get the last part after splitting
                    last_part = parts[-1]
                    
                    # Construct new filename
                    new_filename = f"{folder_name}_{last_part}"
                    
                    # Full paths for old and new names
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_filename)
                    
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                else:
                    print(f"Skipped (no underscores): {filename}")

# Example usage:
rename_images_in_folders('C:/Users/super/Downloads/School Work/MUSA 6950/Final/youtube_frames')