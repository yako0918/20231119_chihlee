from machine import Timer,Pin

def fun10(t:Time):
    print('10秒ㄌ')
    pass

timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10 )

#t1 = t1+1


#timer10 = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))執行一次
#timer11 = tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))連續執行