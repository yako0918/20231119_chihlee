from machine import Pin
import time

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)

while True:
    print(btn.value())
    
    if btn.value() ==1:
        print("按下")
        red_led.value(1)
    else:
        print("放開")
        red_led.value(0)
        
    time.sleep_ms(100) 


#p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
#p0.on()                 # set pin to "on" (high) level
#p0.off()                # set pin to "off" (low) level
#p0.value(1)             # set pin to on/high

#p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
#print(p2.value())       # get value, 0 or 1

#p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
#p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation