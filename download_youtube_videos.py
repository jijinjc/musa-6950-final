import yt_dlp
# import opencv
import cv2
import random
import os
from datetime import datetime

def download_youtube_videos(url, output_dir, quality='best'):
    """Download YouTube videos from a playlist or single URL with dynamic naming"""
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        'format': f'{quality}video[ext=mp4]+bestaudio/best' if quality != 'worst' else 'worstvideo[ext=mp4]',
        'outtmpl': os.path.join(output_dir, '%(title)s_%(id)s.%(ext)s'),
        'ignoreerrors': True,
        'nooverwrites': True,
        'retries': 3,
        'merge_output_format': 'mp4',
    }
    
    print(f"Downloading video(s) from {url}...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        if 'entries' in info:  # Playlist
            video_paths = [ydl.prepare_filename(entry) for entry in info['entries'] if entry is not None]
        else:  # Single video
            video_paths = [ydl.prepare_filename(info)]
    
    print(f"\nDownloaded {len(video_paths)} video(s)")
    return video_paths

base_dir = "output directory"
youtube_url = "https://www.youtube.com/watch?v=QQTujE5qb_U&list=PLLGT0cEMIAzeq_YFR_iHm831-GuOWlwUJ&index=2"
num_frames = 240
frame_scale = 3.0  # Increase this to make frames bigger (1.0 = original size)
video_quality = 'best'  # 'best', 'hd1080', 'hd720', 'medium', 'worst'

# Create directories
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
video_dir = os.path.join(base_dir, "videos", timestamp)
frames_dir = os.path.join(base_dir, "youtube_frames", timestamp)

try:
    # Download videos
    video_paths = download_youtube_videos(youtube_url, video_dir, quality=video_quality)
    
    # Process each video
    '''
    all_saved_frames = []
    for video_path in video_paths:
        if os.path.exists(video_path):  # Only process successfully downloaded videos        
            saved_frames = extract_random_frames(
                video_path, 
                frames_dir, 
                num_frames=num_frames, 
                scale_factor=frame_scale
            )
            all_saved_frames.extend(saved_frames)
            '''
    
    print("\nProcess completed successfully!")
    print(f"Videos location: {video_dir}")
    #print(f"Frames location: {frames_dir}")
    #print(f"Total frames extracted: {len(all_saved_frames)}")
    
except Exception as e:
    print(f"\nError occurred: {str(e)}")


def extract_random_frames(video_path, output_folder, num_frames=10, scale_factor=1.5):
    """Extract random frames from video and save to output folder with optional scaling"""
    print(f"\nProcessing video: {os.path.basename(video_path)}")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception(f"Could not open video file: {video_path}")
    
    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"Video info: {width}x{height} @ {fps:.2f}fps, {total_frames} frames total")
    
    num_frames = min(num_frames, total_frames)
    random_frames = random.sample(range(total_frames), num_frames)
    
    # Create output folder with video name
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_folder = os.path.join(output_folder, video_name)
    os.makedirs(video_output_folder, exist_ok=True)
    
    saved_frames = []
    for i, frame_num in enumerate(random_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if ret:
            # Scale frame if requested
            if scale_factor != 1.0:
                frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, 
                                 interpolation=cv2.INTER_CUBIC)
            
            frame_path = os.path.join(video_output_folder, f"frame_{i+1:03d}.jpg")
            cv2.imwrite(frame_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            saved_frames.append(frame_path)
    
    cap.release()
    print(f"Saved {len(saved_frames)} frames to: {video_output_folder}")
    return saved_frames
