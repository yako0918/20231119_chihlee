import network
import time
#from machine import WDT,Timer
#from machine import Timer
#ssid = 'k51S_yako'
#password = '0911767035'

def connect():
    # enable station interface and connect to WiFi access point
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect('k51S_yako', '0911767035')

    max_wait = 15

    #處理正在連線
    while max_wait > 0:
        max_wait -= 1
        status = nic.status()
        if status < 0 or status >=3:
            break
        print("等待連線")
        time.sleep(1)


        
    #沒有wifi的處理
    if nic.status() != 3:
        #連線失敗,重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError('連線失敗')
        
    else:
        print("成功連線")
        print(nic.ifconfig())

connect()
