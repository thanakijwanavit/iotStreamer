import Adafruit_DHT
import time, pickle
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity and temperature:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        with open('temp.nic', 'wb') as f:
            pickle.dump({
                    "temp": temperature,
                    "humidity": humidity
                }, f)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
