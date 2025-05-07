import os
import shutil
from pathlib import Path

'''
def copy_jpgs(input_dir, output_dir):
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    for root, dirs, files in os.walk(input_dir):
        # Skip the output directory if it's within the input
        if os.path.commonpath([output_dir]).startswith(root):
            continue
        
        for file in files:
            if file.lower().endswith('.jpg'):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(output_dir, file)

                # Only copy if the file doesn't already exist in destination
                if not os.path.exists(dest_path):
                    shutil.copy2(source_path, dest_path)
                else:
                    print(f"Skipping {file} - already exists in destination")
'''
def copy_jpgs_to_output(source_dir, output_dir):
    """
    Copies all JPG images from nested subdirectories to an output directory.
    Skips files that already exist in the output directory.
    Handles cases where output directory is within the source directory.
    """
    # Convert to Path objects for easier path handling
    source_dir = Path(source_dir).resolve()
    output_dir = Path(output_dir).resolve()
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Walk through the source directory
    for root, _, files in os.walk(source_dir):
        root_path = Path(root).resolve()
        
        # Skip the output directory if it's within the source directory
        if output_dir.is_relative_to(root_path):
            continue
            
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                source_file = root_path / file
                dest_file = output_dir / file
                
                # Skip if file already exists in output
                if dest_file.exists():
                    print(f"Skipped (already exists): {source_file}")
                    continue
                
                # Copy the file
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {source_file} -> {dest_file}")

if __name__ == "__main__":
    input_directory = "chosen_vid_frames"
    output_directory = "chosen_vid_frames/all_chosen_frames"

    os.makedirs(output_directory, exist_ok=True)
    copy_jpgs_to_output(input_directory, output_directory)
    #copy_jpgs(input_directory, output_directory)