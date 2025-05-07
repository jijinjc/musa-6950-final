import os
import re
import shutil

def clean_folder_name(name):
    # Remove ALL non-ASCII, non-alphanumeric, and non-space characters
    #name = re.sub(r'[^a-zA-Z0-9 \-_()]', '', name)
    name = re.sub(r'[^a-zA-Z0-9 \-_]', '', name)
    # Replace multiple spaces with a single space
    name = re.sub(r' +', ' ', name).strip()
    return name

def sort_images_into_folders(source_dir):
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            parts = filename.split('_')
            if parts:
                folder_name = clean_folder_name(parts[0])
                if not folder_name:  # Fallback if name is empty after cleaning
                    folder_name = "Other"
                
                dest_folder = os.path.join(source_dir, folder_name)
                try:
                    os.makedirs(dest_folder, exist_ok=True)
                    src_path = os.path.join(source_dir, filename)
                    dest_path = os.path.join(dest_folder, filename)
                    shutil.move(src_path, dest_path)
                    print(f"Moved: {filename} → {folder_name}/")
                except Exception as e:
                    print(f"ERROR moving {filename}: {e}")

# Example usage:
source_directory = "C:/Users/super/Downloads/School Work/MUSA 6950/Final/youtube_frames"
sort_images_into_folders(source_directory)