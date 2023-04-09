import board
import time
import adafruit_dht
import json
dhtDevice = adafruit_dht.DHT11(board.D4)

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")
# For Websocket connection

# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a2d7b4vsi90j5r-ats.iot.eu-north-1.amazonaws.com", 8883)
# For Websocket


myMQTTClient.configureCredentials("/home/raspberrypi/awsiot/aws/RootCA1.pem", "/home/raspberrypi/awsiot/aws/private.pem.key", "/home/raspberrypi/awsiot/aws/certificate.pem.crt")
# For Websocket, we only need to configure the root CA

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
data = {"sr_no" : 0,"temperature" : 0,"humidity":0}
i=0

while(True):
    try:
        i=i+1
        data["sr_no"]=i
        data["temperature"]=str(dhtDevice.temperature)+" C /"+str(dhtDevice.temperature*(9/5)+32)+" F"
        data["humidity"]=str(dhtDevice.humidity)+" %"
        data_temp = json.dumps(data)
        myMQTTClient.publish(topic="myTopic",QoS=1,payload=data_temp)
        
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5)

#myMQTTClient.subscribe("myTopic", 1, customCallback)
#myMQTTClient.unsubscribe("myTopic")
myMQTTClient.disconnect()
