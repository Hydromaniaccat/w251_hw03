import paho.mqtt.client as mq
import time
import pickle as pk
import cv2 as cv
import uuid

def on_message(client, userdata, msg):
    print("Message received ")    
    #print(msg.payload)
    send_to_cloud(msg.payload)
    

def save_to_cloud(text):
    filename = str(uuid.uuid4())+'.png'
    print("Writing... /mnt/mybucket/" + filename)
    frame = pk.loads(text)
    print(type(frame))
    cv.imwrite("/mnt/mybucket/" + filename, frame)
    print("Wrote file /mnt/mybucket/" + filename)

broker = "172.18.0.2"
#broker = "localhost"
#broker_cloud = "169.62.13.213"

client = mq.Client("python4")
client.on_message = on_message

client.connect(broker)
while True:
    client.loop_start()
    client.subscribe("pictures/faces",1)
    time.sleep(5)
    client.loop_stop()
time.sleep(3)
#client.disconnect()

