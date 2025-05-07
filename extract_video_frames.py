import os
import cv2

def extract_frames_every_10_seconds(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all mp4 files in input folder
    mp4_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mp4')]
    
    for mp4_file in mp4_files:
        input_path = os.path.join(input_folder, mp4_file)
        cap = cv2.VideoCapture(input_path)
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps
        
        # Skip if video is too short (less than 20 seconds)
        if duration <= 20:
            print(f"Skipping {mp4_file} - duration ({duration:.1f}s) is too short (needs >20s)")
            cap.release()
            continue
        
        # Calculate frame interval for 10 seconds
        frame_interval = int(10 * fps)
        
        # Start from 10s and end at (duration - 10s)
        start_time = 10
        end_time = duration - 10
        
        # Extract and save frames every 10 seconds (skipping first & last 10s)
        base_name = os.path.splitext(mp4_file)[0]
        saved_count = 0
        
        for time_sec in range(start_time, int(end_time), 10):
            frame_num = int(time_sec * fps)
            
            # Ensure we don't go beyond video length (safety check)
            if frame_num >= total_frames:
                break
                
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()
            
            if ret:
                output_name = f"{base_name}_time{time_sec:04d}s.jpg"
                output_path = os.path.join(output_folder, output_name)
                cv2.imwrite(output_path, frame)
                saved_count += 1
        
        print(f"Saved {saved_count} frames (every 10s, skipping first & last 10s) from {mp4_file}")
        cap.release()


input_folder = "C:/Users/super/Downloads/School Work/MUSA 6950/Final/videos/20250420_181646"  # Change to your input folder path
output_folder = "C:/Users/super/Downloads/School Work/MUSA 6950/Final/youtube_frames"  # Change to your output folder path

extract_frames_every_10_seconds(input_folder, output_folder)