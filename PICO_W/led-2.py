import time
from machine import Pin
led = Pin("LED", Pin.OUT)

while True:
    led.on()
    #print('run')
    #time.sleep(1)		#"1"sec
    #time.sleep_ms(200)	#"0.5"sec
    time.sleep_ms(100)
    led.off()
    #print('not run')
    time.sleep_ms(100)