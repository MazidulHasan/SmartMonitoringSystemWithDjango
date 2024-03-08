import subprocess
import datetime
import os

rtsp_url = "rtsp://admin:Ab12Ab12@192.168.50.78:554/live/ch00_1"
output_folder = "/home/pi/Desktop/VataProject/videos"
os.makedirs(output_folder, exist_ok=True)

# Generate timestamp for the video file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
video_filename = os.path.join(output_folder, f"video_{timestamp}.mp4")

# Run FFmpeg command to record the RTSP stream with audio
ffmpeg_cmd = [
    "ffmpeg",
    "-rtsp_transport", "tcp",  # Use TCP transport for RTSP (more reliable)
    "-i", rtsp_url,
    "-c:v", "copy",  # Copy video stream without re-encoding
    "-c:a", "aac",  # Specify AAC audio codec for encoding audio
    "-af", "volume=2.0",  # Adjust audio volume level (e.g., double the volume)
    "-t", "30",  # Record for 30 seconds (adjust as needed)
    "-y",  # Overwrite output file if it exists
    video_filename
]

try:
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"Video saved: {video_filename}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while recording video: {e}")
