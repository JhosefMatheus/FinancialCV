from VideoHandler import VideoHandler

video_path = "SuperDOM Simples.mkv"

video_handler = VideoHandler(video_path)

frames = video_handler.get_frames()
frames_selection = video_handler.sliced_frames(frames)
prices = video_handler.get_prices(frames_selection)

print(prices)
