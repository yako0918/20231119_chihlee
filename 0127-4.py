from machine import ADC, Pin
import time

adc_light = ADC(Pin(27))
#light_value = adc_light.read_u16()


while True:
    light_value = adc_light.read_u16()
    print(light_value)
    time.sleep_ms(100)