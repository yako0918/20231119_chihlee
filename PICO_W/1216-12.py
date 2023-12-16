import network
import time

ssid = 'Robert_iPhone'
password = '0926656000'

#machine.RTC()
#print(f'{machine.RTC()}')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect() 
wlan.connect(ssid,password)


#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#<0,>3失敗的連線

max_wait = 5	#連線時間限制
while max_wait > 0:
    status = wlan.status()
    print(f'status= {status}') #印出狀態
    if status < 0 or status >= 3:
        break
    max_wait -= 1
    print("等待連線")
    
    time.sleep(1) #延時

#檢查目前連線狀態
    
if wlan.status() != 3:
    raise RuntimeError('連線失敗  ')

else:
    print('連線成功')
    configure = wlan.ifconfig()
    print(f'ip={configure[0]}')