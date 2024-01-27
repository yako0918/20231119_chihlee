import network  #無線網路
import time #延遲
from machine import WDT

ssid = 'k51S_yako'
password = '0911767035'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)  #
wlan.connect(ssid,password)#帳號密碼
#
#if wlan.isconnected():
#    print("連線成功")
#else:
#    print("連線失敗")

#連線,並檢查內線狀態資訊
#status < 0 等待連線
#status = 0,1,2正在等待連線
#status = 3連線成功
#status <=3失敗的連線
#
max_wait=10
#處理正在連線
while max_wait >0:#連線時間 10秒
    #pass
    status = wlan.status()
    if status <0 or status >=3:
        break
    max_wait -=1 #減法算時間
    print("等待連線:..........")
    #print(max_wait())

    time.sleep(1) #延遲
   
    
#沒有連線的處理    
if wlan.status() != 3:
    raise RuntimeError("連線失敗")
    #連線失敗重新開機
    wdt = WDT(timeout=2000)
    wdt.feed()
else:    

    print(f'連線成功 {wlan.ifconfig()}')
    #print("連線成功:")
    #print(wlan.ifconfig())
    #print(f'ip={status[0]}')