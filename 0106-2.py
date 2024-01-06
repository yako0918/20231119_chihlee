import time
import network

ssid = 'k51S_yako'
password = '0911767035'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#<1,>=3失敗的連線

max_wait = 10
while max_wait > 0:
    status = wlan.status()
    if status < 0 or status >= 3:
        break
    max_wait -= 1
    print("等待連線.........")
    time.sleep(1)

#處理錯誤
if wlan.status() != 3:
    #raise RuntimeError('連線失敗')
    print('連線 失敗')
    pass
else:
    print('連線成功')
    status = wlan.ifconfig()
    print(f'ip={status[0]}')