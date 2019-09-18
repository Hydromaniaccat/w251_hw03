import numpy as np
import cv2 as cv
import paho.mqtt.client as mq
import time
import _pickle as pk

broker = "172.18.0.3"
#broker = "localhost"
#broker = "iot.eclipse.org"

client = mq.Client("python1")

def on_log(client, userdata, level, buf):
    print("log: " + buf)
    
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected results code " + str(rc))
        
def on_publish(client, userdata, result):
    print("Data published")
        
def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("Message received ", m_decode)

#client.on_connect = on_connect
#client.on_disconnect=on_disconnect
#client.on_log = on_log
#client.on_message = on_message
client.on_publish = on_publish
    
face_cascade = cv.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:     
        crop_img = gray[y:y+h, x:x+w]
        client.connect(broker)
        client.loop_start()
        #client.subscribe("pictures/faces",1)
        client.publish("pictures/faces",pk.dumps(crop_img))
        time.sleep(5)
        client.loop_stop()
        client.disconnect()
    time.sleep(5)
    

