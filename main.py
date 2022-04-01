from VideoHandler import VideoHandler
import cv2
import easyocr

video_path = "SuperDOM Simples.mkv"

video_handler = VideoHandler(video_path)

frames = video_handler.get_frames()
frames_selection = video_handler.sliced_frames(frames)
