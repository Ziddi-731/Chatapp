import cv2
import base64
cap = cv2.VideoCapture("lofi.mp4")  # Start capturing from the webcam
        
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        _, buffer = cv2.imencode('.jpg', frame)
        frame_data = base64.b64encode(buffer).decode('utf-8')
        print("Frame : ",frame_data)
# import cv2
# import base64
# import asyncio
# import json
# from moviepy.editor import VideoFileClip

# class VideoAudioStream:
#     def __init__(self, group_name, channel_layer):
#         self.group_name = group_name
#         self.channel_layer = channel_layer

#     async def capture_video_audio(self, video_file="lofi.mp4"):
#         # Load the video file using moviepy to access both video and audio
#         clip = VideoFileClip(video_file)
#         audio = clip.audio
        
#         cap = cv2.VideoCapture(video_file)  # Capture video frames
        
#         frame_rate = 30  # Assume a frame rate (adjust to your needs)
#         audio_frame_duration = 1 / frame_rate

#         # Total time of the video
#         duration = clip.duration
        
#         for t in range(0, int(duration * frame_rate)):
#             if cap.isOpened():
#                 ret, frame = cap.read()
#                 if ret:
#                     _, buffer = cv2.imencode('.jpg', frame)
#                     frame_data = base64.b64encode(buffer).decode('utf-8')
                    
#                     # Get the corresponding audio chunk
#                     audio_chunk = audio.subclip(t / frame_rate, (t + 1) / frame_rate).to_soundarray(fps=44100)
#                     audio_b64 = base64.b64encode(audio_chunk.tobytes()).decode('utf-8')
                    
#                     # Send video and audio together
#                     await self.channel_layer.group_send(
#                         self.group_name,
#                         {
#                             'type': 'live.stream',
#                             'frame': frame_data,
#                             'audio': audio_b64
#                         }
#                     )
                    
#                 await asyncio.sleep(audio_frame_duration)

#     async def live_stream(self):
#         await self.capture_video_audio()

#     async def send_frame_audio(self, event):
#         frame = event['frame']
#         audio = event['audio']
#         await self.send(text_data=json.dumps({
#             'type': 'live',
#             'frame': frame,
#             'audio': audio
#         }))
