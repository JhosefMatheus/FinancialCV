import cv2
import numpy as np
import easyocr as ocr

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

    
    def __get_coordinates(self, contours):
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
        
        return x, y, w, h


    def sliced_frames(self, frames):
        lower_bound = np.array([22, 93, 0])
        upper_bound = np.array([45, 255, 255])

        new_array = []

        for frame in frames:
            blur_frame = cv2.blur(frame, (7, 7))
            hsv_frame = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

            cnts, __ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            coordinates = self.__get_coordinates(cnts)

            x, y, w, h = coordinates

            new_frame = frame[y:y+h, x:x+w]

            new_array.append(new_frame)
        
        return new_array

    
    def __get_text_image(self, image):
        reader = ocr.Reader(["en"], gpu=True)
        result = reader.readtext(image)

        text = result[0][1]
        
        return text


    def __convert_text(self, text):
        text = text.replace(".", "")
        text = text.replace(",", "")

        text_number = float(text)

        return text_number


    def get_prices(self, images_array):
        prices = np.array([])

        for image in images_array:
            text = self.__get_text_image(image)
            price = self.__convert_text(text)

            prices = np.append(prices, price)
        
        return prices

