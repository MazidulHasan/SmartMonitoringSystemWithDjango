import os
import requests

# Django server URL
SERVER_URL = 'http://192.168.50.92:8000/api-upload/'

# Directory containing video files
VIDEO_DIRECTORY = '/home/pi/Videos/vataVidoes'

# Iterate through files in the directory
for filename in os.listdir(VIDEO_DIRECTORY):
    if filename.endswith('.mp4'):  
        filepath = os.path.join(VIDEO_DIRECTORY, filename)
         
        # Send file to Django server
        with open(filepath, 'rb') as file:
            files = {'file_name': (filename, file)}
            data = {
                'file_location': 'Raspberry Pi',
                'camera_number': 1,  
                'video_record_time': '2024-02-23T12:00:00', 
            }
            response = requests.post(SERVER_URL, files=files, data=data)
            
            if response.status_code == 200:
                print(f"File {filename} uploaded successfully.")
                os.remove(filepath)  # Delete file after successful upload
            else:
                print(f"Failed to upload file {filename}. Status code: {response.status_code}")
