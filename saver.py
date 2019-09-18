import paho.mqtt.client as mq
import time
import pickle as pk
import cv2 as cv
import uuid

def on_message(client, userdata, msg):
    print("Message received ")    
    filename = str(uuid.uuid4())+'.png'
    cv.imwrite("/mnt/mybucket/" + filename, pk.loads(msg.payload))

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

