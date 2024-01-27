from machine import Timer,Pin
from machine import ADC, Pin
import utime
#
# ADCs: GP26, GP27, GP28 and GP29-to VSYS
#       ADC0, ADC1, ADC2 and ADC3 ，ADC4道連接內建溫度感測器，可用於測量溫度。
#
#
adc_light_GP26 = ADC(Pin(26)) #ADC0
adc_light_GP27 = ADC(Pin(27)) #ADC1
adc_light_GP28 = ADC(Pin(28)) #ADC2
adc_light_GP29 = ADC(Pin(29)) #ADC2

light_value_26 = adc_light_GP26.read_u16()
light_value_27 = adc_light_GP27.read_u16()
light_value_28 = adc_light_GP28.read_u16()
light_value_29 = adc_light_GP29.read_u16()

def fun10(t:Time):
    #print('1秒ㄌ')
    #print(f"{abc}")
    #print(light_value_26)
    #print(light_value_27)
    #print(light_value_28)
    #print(light_value_29)
    print(light_value_27)
    print('-------------------------')
    pass

timer10 = Timer(period=1000, mode=Timer.PERIODIC, callback=fun10 )
