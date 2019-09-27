import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://192.168.1.4:5555')

camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        (grabbed, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        
        # bytes(data['imageData'], 'utf-8')
        # print(encoded)
        encoded_string = str(base64.b64encode(buffer))
        # print(encoded_string)
        # if len(encoded_string)%4 ==0:
        footage_socket.send_string(str(encoded_string))

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break