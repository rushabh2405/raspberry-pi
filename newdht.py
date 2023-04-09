import board
import time
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D4)
while(1):
	temp = dhtDevice.temperature
	hum = dhtDevice.humidity
	print("Temperature : {}*C	Humidity : {}%".format(temp,hum))
	time.sleep(5)
