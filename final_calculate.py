#author: rajoan_d_dinosaur
import os
import cv2

def convert_seconds_to_hms(seconds):
    """Convert total seconds to hours, minutes, and seconds."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)
    return hours, minutes, remaining_seconds

def process_video_files(root_dir):
    total_duration = 0
    video_count = 0

    # Traverse through the root directory and process video files
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv')):
                video_count += 1
                file_path = os.path.join(root, file)
                try:
                    cap = cv2.VideoCapture(file_path)
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    duration = frame_count / fps
                    total_duration += duration
                    cap.release()
                except Exception as e:
                    print(f"Could not process {file}: {e}")
    
    # Convert total duration to hours, minutes, and seconds
    hours, minutes, seconds = convert_seconds_to_hms(total_duration)

    # Calculate watch times at different speeds
    time_1_25x = total_duration / 1.25
    time_1_50x = total_duration / 1.50
    time_2x = total_duration / 2.00

    # Convert times at different speeds to hours, minutes, and seconds
    h1_25x, m1_25x, s1_25x = convert_seconds_to_hms(time_1_25x)
    h1_50x, m1_50x, s1_50x = convert_seconds_to_hms(time_1_50x)
    h2x, m2x, s2x = convert_seconds_to_hms(time_2x)

    # Print the results
    print(f"\nTotal videos found: {video_count}")
    print(f"Total video length: {hours} hours, {minutes} minutes, {seconds} seconds")
    print(f"Total watch time at 1.25x speed: {h1_25x} hours, {m1_25x} minutes, {s1_25x} seconds")
    print(f"Total watch time at 1.50x speed: {h1_50x} hours, {m1_50x} minutes, {s1_50x} seconds")
    print(f"Total watch time at 2.00x speed: {h2x} hours, {m2x} minutes, {s2x} seconds")

# Replace with the folder you want to start from
root_folder = input("Enter the root folder path: ")
process_video_files(root_folder)
