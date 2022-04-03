from VideoHandler import VideoHandler
from ProcessData import ProcessData

video_path = "SuperDOM Simples.mkv"

video_handler = VideoHandler(video_path)
processor = ProcessData()

frames = video_handler.get_frames()
frames_selection = video_handler.sliced_frames(frames)
prices = video_handler.get_prices(frames_selection)
steps = processor.get_prices_step(prices)
