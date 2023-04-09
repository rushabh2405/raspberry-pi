import board
import time
import adafruit_dht
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import mysql.connector

def main():
        dhtDevice = adafruit_dht.DHT11(board.D4)
        db =mysql.connector.connect(host="localhost",user="myuser2",password="mysql",database="mydb2")
        
        data = {"Sr_no":0, "Temperature" : 0, "Humidity":0, "Version":0}
        
        data["Temperature"]=str(dhtDevice.temperature)+" C /"+str(dhtDevice.temperature*(9/5)+32)+" F"
        data["Humidity"]=str(dhtDevice.humidity)+" %"
        data["Version"]="version-2"
                
        cursor=db.cursor()
        query="insert into mytable2(Temperature,Humidity,Version) values (%s,%s,%s)"
        cursor.execute(query,(data["Temperature"],data["Humidity"],data["Version"]))
        
        cursor.close()
        db.commit()
        
if __name__=="__main__":
        main()
