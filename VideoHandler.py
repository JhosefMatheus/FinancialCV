import cv2
import numpy as np

class VideoHandler:

    def __init__(self, video_path):
        self.__video_path = video_path

    def get_frames(self):
        c = 1
        video = cv2.VideoCapture(self.__video_path)

        ret, frames = video.read()
        while ret:
            ret, frame = video.read()
            try:
                frames = np.append(frames, frame, axis=0)
                c +=1

            except Exception as e:
                pass
        frames = np.array(np.split(frames, c))
        frames = np.delete(frames, 0,0)

        return frames  




