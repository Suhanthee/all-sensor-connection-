from machine import Pin,time_pulse_us,ADC
from utime import sleep
from utime import time
import dht
dhtsen=dht.DHT22(Pin(32))
dhtsen.measure()
temp=dhtsen.temperature()
pirsensor=Pin(14,Pin.IN)
print(temp)
if pirsensor.value() == 1:
    print("Motion is detected")
else:
    print("Motion is not detected")

import time
trig=Pin(5,Pin.OUT)
echo=Pin(4,Pin.IN)
def measure_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, 30000) 

    distance = (duration / 2) * 0.0343  
    return distance


print(measure_distance())
time.sleep(3)

LDR_Pin = ADC(Pin(26, Pin.IN))
LED = Pin(33, Pin.OUT)

LDR = LDR_Pin.read()
print('LDR:',LDR)

