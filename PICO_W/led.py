from machine import Pin
#import time
p25 = Pin("LED", Pin.OUT)
p25.value(1)   # LED亮
time.sleep(1)  # 等待1秒
p25.value(0)
time.sleep(1)  # LED滅