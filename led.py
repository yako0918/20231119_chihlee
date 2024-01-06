from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
  led.value(1)   # LED亮
  time.sleep(1)  # 等待1秒
  led.value(0)
  time.sleep(1)  # LED滅