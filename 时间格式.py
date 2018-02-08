##
#python程序，以多种格式显示当前时间和日期
import time
from time import gmtime, strftime

t = time.localtime()
print(time.asctime(t))
print(strftime("%a,%d %b %Y %h:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%y", gmtime()))

#将秒转换为格林威治标准时间
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(1234567890)))
