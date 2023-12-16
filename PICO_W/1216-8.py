from machine import Pin,Timer
LED=Pin("LED",Pin.OUT)

def led_switch(x):
    LED.value(not LED.value())
    
tim1=Timer(1)
tim1.init(period=500, mode=Timer.PERIODIC, callback=led_switch)
try:
    while 1:
        pass
except:
    tim1.deinit()
    print('stopping')