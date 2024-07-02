import requests
import platform
import cv2
import time
import os

headers = {'Content-Type': 'application/json'}
name_devices = platform.node()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Ошибка: не удалось открыть веб-камеру")
    exit()

while True:
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_file = os.path.join('output.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (frame_width, frame_height))

    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame is not None:
            out.write(frame)
        else:
            pass        
        if (time.time() - start_time) > 20 or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

    url = 'http://192.168.1.104:3000/api/upload_video'
    files = {'video': open(output_file, 'rb')}  
    response = requests.post(url, files=files)
    print(response.json())

    break
