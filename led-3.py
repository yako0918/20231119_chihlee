import time
from machine import Pin
led = Pin("LED", Pin.OUT)

#    
#time1= timer(mode=Timer.PERIODIC, freq=1000, callback=mycallback)
#time2= timer()
#time3= timer()
#classmachine.Timer(id, /, ...)
# periodic at 1kHz   秒執行1000次max
#tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback)

# periodic with 100ms period  100ms秒執行次
#tim.init(period=100, callback=mycallback)

# one shot firing after 1000ms 一次
#tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)

led = Pin("LED", Pin.OUT)

while True:
    #pass
    led.on()
    print('run')
    #time.sleep(1)		#"1"sec
    #time.sleep_ms(200)	#"0.5"sec
    time.sleep_ms(100)
    led.off()
    print('not run')
    time.sleep_ms(100)