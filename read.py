import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://192.168.1.4:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        frame = footage_socket.recv_string()
        # print(str(frame))
        img = base64.b64decode(frame)
        print(img)
        # npimg = np.fromstring(img, dtype=np.uint8)
        # source = cv2.imdecode(str(img), 1)
        # cv2.imshow("Stream", source)
        # cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break