from machine import Timer,Pin
from machine import ADC, Pin
import time

def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle() #狀態反轉
    
def fun100ms(t:Timer):
    print(f'vr:{light_value}')    
    
    
    
led = Pin(15, Pin.OUT)
adc_light = ADC(Pin(27))
vr = adc_light.read_u16()
timer10 = timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer100ms = Timer(period=100, mode=Timer.PERIODIC, callback=fun100ms)
fun10()


while True:
    print(light_value_26)
    pass



