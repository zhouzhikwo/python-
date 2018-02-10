##
#python程序，打印指定年份日历

import calendar
cal_display = calendar.TextCalendar(calendar.MONDAY)
#年：2019
#列宽：1
#每周行数：1
#月列之间的空格数：0
#每一行月份数：4
print(cal_display.formatyear(2018, 1, 1, 0, 4))
