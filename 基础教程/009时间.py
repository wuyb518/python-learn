#!/usr/bin/python
# _*_ coding:UTF-8 _*_

import time
import calendar

#time
ticks=time.time()
print '当前时间戳为:',ticks
localtime=time.localtime(time.time())
print '本地时间为:',localtime
print time.asctime(time.localtime(time.time()))
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  
print time.mktime(time.strptime('2018-01-01 12:00:20','%Y-%m-%d %H:%M:%S'))

# calendar
cal=calendar.month(2018,3)
print cal

# time内置函数
# time.altzone
# time.clock() 用以浮点数计算的描述返回当前cpu时间,用来衡量不同程序的耗时,比time.time()更有用
# time.sleep(secs) 退出调用线程的运行,secs指秒数






