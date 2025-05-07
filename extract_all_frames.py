import os
import cv2

def extract_frames_from_subfolders(root_folder, target_fps=30):
    """
    Extract frames from all MP4 files in all subfolders of root_folder.
    Frames are saved in the same subfolder as the source video.
    
    Args:
        root_folder: Path to the root folder containing subfolders with videos
        target_fps: Target frames per second for extraction
    """
    # Walk through all subfolders
    for foldername, subfolders, filenames in os.walk(root_folder):
        mp4_files = [f for f in filenames if f.lower().endswith('.mp4')]
        
        if not mp4_files:
            continue
            
        print(f"\nProcessing folder: {foldername}")
        
        for mp4_file in mp4_files:
            input_path = os.path.join(foldername, mp4_file)
            base_name = os.path.splitext(mp4_file)[0]
            
            # Create a subfolder for frames if it doesn't exist
            frames_folder = os.path.join(foldername, f"{base_name}_frames")
            os.makedirs(frames_folder, exist_ok=True)
            
            cap = cv2.VideoCapture(input_path)
            
            # Get video properties
            original_fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = total_frames / original_fps
            
            print(f"\nProcessing: {mp4_file}")
            print(f"Original FPS: {original_fps:.2f}, Duration: {duration:.2f}s, Total frames: {total_frames}")
            
            # Calculate frame interval based on target FPS
            if original_fps <= target_fps:
                frame_interval = 1
                actual_fps = original_fps
            else:
                frame_interval = round(original_fps / target_fps)
                actual_fps = original_fps / frame_interval
            
            print(f"Extracting at {actual_fps:.2f} FPS (taking 1 every {frame_interval} frames)")
            print(f"Saving frames to: {frames_folder}")
            
            frame_count = 0
            saved_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                    
                if frame_count % frame_interval == 0:
                    timestamp = frame_count / original_fps
                    output_name = f"frame{frame_count:06d}_{timestamp:.3f}s.jpg"
                    output_path = os.path.join(frames_folder, output_name)
                    cv2.imwrite(output_path, frame)
                    saved_count += 1
                    
                frame_count += 1
                
                if frame_count % 1000 == 0:
                    print(f"Processed {frame_count}/{total_frames} frames...")
            
            print(f"Finished. Saved {saved_count} frames from {mp4_file}")
            cap.release()

if __name__ == "__main__":
    root_folder = "C:/Users/super/Downloads/School Work/MUSA 6950/Final/chosen_vid_frames"  # Change to your root folder containing subfolders with videos
    target_fps = 1  # Change this to your desired frame rate
    
    extract_frames_from_subfolders(root_folder, target_fps)