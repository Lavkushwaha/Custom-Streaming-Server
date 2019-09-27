import cv2
import zmq
import base64
import numpy as np
# from StringIO import StringIO
from io import StringIO
from PIL import Image

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://192.168.1.4:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))


# def readb64(uri):
#     encoded_data = uri.split(',')[0]
#     nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     return img

# cvimg = readb64('R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7')
# cv2.imshow(cvimg)


count = 0
while True:
    count += 1
    try:
        
        frame1 = footage_socket.recv_string()
        img = base64.b64decode(frame1[1:])
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break
