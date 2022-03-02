
import numpy as np
import cv2
from matplotlib import pyplot as plt

class Render:
    def render_func(self, image, H, W, classes, net):  
        blob = cv2.dnn.blobFromImage(image, 1/255, (320, 320), (0,0,0), swapRB=True, crop=False )
        print( type(blob) )
        #plt.imshow(blob)
        #plt.waitforbuttonpress(0)

        net.setInput(blob)
        output_layes_name = net.getUnconnectedOutLayersNames()
        layeroutput = net.forward(output_layes_name)

        boxes = []
        confidences = []
        class_ids = []

        for output in layeroutput:
            for detection in output:
                score = detection[5:]
                class_id = np.argmax(score)
                confidence = score[class_id]
                if confidence > 0.7:
                    box = detection[0:4] * np.array([W, H, W,H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width/2) )
                    y = int(centerY - (height/2) ) 

                    #center_x = int(detection[0] * width)
                    #center_y = int(detection[0] * height)
                    #w = int(detection[0] * width)
                    #h = int(detection[0] * height)
                    #x = int(center_x - w/2)
                    #y = int(center_y - h/2)

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(1, 200, size = (len(boxes), 3))

        if len(indexes) > 0:
            for i in indexes.flatten():
                (x, y) = ( boxes[i][0], boxes[i][1] )
                (w, h) = ( boxes[i][2], boxes[i][3] )
                
                #x,y,w,h = boxes[i]
                label = str( classes[ class_ids[i] ])
                confi = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle( image, (x,y), (x+w, y+h), (color), 1 )
                cv2.putText(image, label+" "+confi, (x, y+30), font, 2, (100,255,100), 2)

        cv2.imshow("image", image)