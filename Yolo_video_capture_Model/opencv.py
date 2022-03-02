# eval "$(/Users/blue/miniforge3/bin/conda shell.zsh hook)"
# conda activate tf_m1_test

import numpy as np
import cv2
from matplotlib import pyplot as plt
from Render import Render

Render = Render()
cap = cv2.VideoCapture(0)

classes = []

with open("../yolo_config/data/coco.names", 'r') as f:
    print('Loading coco Names...')
    classes = f.read().splitlines()
    f.close()
    print('Coco Name OK. ', len(classes), " founded..." )


print('Loading weights and cfg')
yolo = cv2.dnn.readNet("../yolov3.weights", "../yolov3.cfg")
print('Loading weights and cfg OK')

while(True):
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #cv2.imshow('frame', frame)
    #cv2.imshow('ret', ret)
    #cv2.imshow('image', image)
    height, width = frame.shape[0:2]

    Render.render_func(frame, height, width, classes, yolo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()