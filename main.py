from VideoHandler import VideoHandler
import cv2
import easyocr

video_path = "SuperDOM Simples.mkv"

video_handler = VideoHandler(video_path)

frames = video_handler.get_frames()

first_frame = frames[0]

cv2.imshow("Frame", first_frame)
cv2.waitKey(0)
