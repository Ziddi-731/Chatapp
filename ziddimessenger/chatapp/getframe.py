import cv2
import base64
import asyncio
cap = cv2.VideoCapture(0)  # Start capturing from the webcam
async def getf():   
   
      
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_data = base64.b64encode(buffer).decode('utf-8')
            print("Frame : ",frame_data)
            return frame_data
        # await asyncio.sleep(0.33)
# print(getf())