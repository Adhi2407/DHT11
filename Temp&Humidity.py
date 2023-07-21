import Adafruit_DHT
import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin = 23
while True:
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is None and temperature is None:
        print("Failed to get reading. Try Again!")
    else:
        print("Temp={0:0.1f}*c Humidity={1:0.2f}%".format(temperature,humidity))
    time.sleep(1)

