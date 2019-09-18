import paho.mqtt.client as mq
import time

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
    print("Message received")    
    send_to_cloud(msg.payload, topic=msg.topic)

def send_to_cloud(msg, topic='pictures/faces', broker="169.62.13.213"):
    client = mq.Client("python3")
    client.on_publish = on_publish
    client.connect(broker)
    client.loop_start()
    client.publish(topic,msg)
    client.loop_stop()
    client.disconnect()
    
broker = "172.18.0.3"
#broker = "localhost"
broker_cloud = "169.62.13.213"

#broker = "iot.eclipse.org"

client = mq.Client("python2")

#client2.on_connect = on_connect
#client2.on_disconnect=on_disconnect
#client.on_log = on_log
client.on_message = on_message

client.connect(broker)
while True:
    client.loop_start()
    client.subscribe("pictures/faces",1)
    time.sleep(5)
    client.loop_stop()
time.sleep(3)
# client2.loop_stop()
#client2.disconnect()

