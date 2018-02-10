from delorean import Delorean #调用Delorean
import delorean               #调用delorean

#频率为HOURLY，次数为10次
for stop in stops(freq=delorean.HOURLY,count=10):
    print(stop)
