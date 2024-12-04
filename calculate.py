import cv2
import os

def get_total_video_length(folder_path):
    total_duration = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv')):
                file_path = os.path.join(root, file)
                try:
                    cap = cv2.VideoCapture(file_path)
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    duration = frame_count / fps
                    total_duration += duration
                    print(f"Processed: {file} ({duration:.2f} seconds)")
                    cap.release()
                except Exception as e:
                    print(f"Could not process {file}: {e}")

    # Convert total duration to hours, minutes, and seconds
    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600) // 60)
    seconds = int(total_duration % 60)

    print("\nTotal video length:")
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
    return total_duration

# Replace with your folder path
folder_path = input("Enter the folder path: ")
get_total_video_length(folder_path)
