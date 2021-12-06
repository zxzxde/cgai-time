# -*- coding:utf-8 -*-
from cgai_time.Time import TimeHandler



ct = TimeHandler()

# """ ***** 日期格式转化 ***** """
#
# # 字符串格式转成数组格式 "2021-07-16" -> (2021,7,16)
# t_date = ct.strDate2TupleDate('2021-07-16')
# print(t_date) #(2021,7,16)
#
# # 数组格式转成字符串格式 (2021,7,16) -> "2021-07-16"
# s_date = ct.tupleDate2StrDate((2021,7,16))
# print(s_date) #"2021-07-16"
#
# # 格式化日期转时间戳
# str_time = '2021-07-18 17:19:44'
# time_stamp = ct.strTime2TimeStamp(str_time)
# print(time_stamp) # 1626599984.0
#
# #时间戳转格式化日期时间
# time_stamp = 1626599984.0
# str_time = ct.timeStamp2StrTime(time_stamp)
# print(str_time) # "2021-07-18 17:19:44"
#
#
#
# # 秒数转分钟
# seconds = 70
# minutes = ct.s2m(seconds)
# int_minutes = ct.s2m(seconds,getInt=True)
# print(minutes) # 1.1666666666666667
# print(int_minutes) # 1
#
#
# #分钟转秒数
# minutes = 12.015
# seconds = ct.m2s(minutes)
# int_seconds = ct.m2s(minutes,getInt=True)
# print(seconds)  # 720.9000000000001
# print(int_seconds)  # 720
#
#
# # 秒转小时
# seconds = 1244
# hours = ct.s2h(seconds)
# int_hours = ct.s2h(seconds,getInt=True)
# print(hours)  # 0.34555555555555556
# print(int_hours)  # 0
#
#
# # 小时转秒
# hours = 0.342
# seconds = ct.h2s(hours)
# int_seconds = ct.h2s(hours,getInt=True)
# print(seconds)  # 1231.2000000000003
# print(int_seconds)  # 1231
#
# # 秒转天数
# seconds = 112341
# days = ct.s2d(seconds)
# int_days = ct.s2d(seconds,getInt=True)
# print(days)  # 1.3002430555555555
# print(int_days) # 1
#
# # 天数转秒
# days = 0.451
# seconds = ct.d2s(days)
# int_seconds = ct.d2s(days,getInt=True)
# print(seconds)  # 38966.399999999994
# print(int_seconds)  # 38966
#
# # 分钟转小时
# minutes = 1234
# hours = ct.m2h(minutes)
# int_hours = ct.m2h(minutes,getInt=True)
# print(hours)  # 20.566666666666666
# print(int_hours)  # 20
#
# # 小时转分钟
# hours = 0.241
# minutes = ct.h2m(hours)
# int_minutes = ct.h2m(hours,getInt=True)
# print(minutes)  #  14.459999999999999
# print(int_minutes)  # 14
#
# # 分钟转天数
# minutes = 421321
# days = ct.m2d(minutes)
# int_days = ct.m2d(minutes,getInt=True)
# print(days)  # 292.5840277777778
# print(int_days) # 292
#
# # 天数转分钟
# days = 0.912
# minutes = ct.d2m(days)
# int_minutes = ct.d2m(days,getInt=True)
# print(minutes)  # 1313.2800000000002
# print(int_minutes)  # 1313
#
# # 小时转天数
# hours = 482
# days = ct.h2d(hours)
# int_days = ct.h2d(hours,getInt=True)
# print(days)  # 20.083333333333332
# print(int_days)  # 20
#
# # 天转小时
# days = 0.924
# hours = ct.d2h(days)
# int_hours = ct.d2h(days,getInt=True)
# print(hours)  #  22.176000000000002
# print(int_hours)  # 22
#
#
#
# # # 输入天数，小时，分钟转成秒
# seconds = ct.getSeconds(d=1,h=3,m=25)
# print(seconds)  # 98700
# seconds = ct.getSeconds(h=3,m=25)
# print(seconds)  # 12300
#
#
# #将秒数转成以天,小时,分钟,秒对应值
# seconds = 3600*24+3599
# dhms = ct.DHMS(seconds)
# print(dhms) #{'day': 1, 'hour': 0, 'minute': 59, 'second': 59}
#
#
# """ ***** 时间计算 ***** """
#
# # 获取当前时间戳
# cts = ct.CTS()
# print(cts)  #  1626660957.2461472
#
#
# # 获取当前格式化日期时间
# str_time = ct.StrTime()
# print(str_time)  #  2021-07-20 09:43:49
#
# # 计算两格式化日期之间的所差秒数
# start_date = '2021-07-18 17:19:44'
# end_date = '2021-07-18 22:32:11'
# dt = ct.deltaTime(end_date,start_date)
# print(dt)  # 18747.0
#
#
#
# # 格式化日期直接进行时间增减
# str_time = '2021-07-18 17:19:44'
# new_str_time = ct.addTime(str_time,d=1)  # 增加一天
# print(new_str_time)  # 2021-07-19 17:19:44
# new_str_time = ct.addTime(str_time,h=8)  # 增加8小时
# print(new_str_time)  # 2021-07-19 01:19:44
# new_str_time = ct.subTime(str_time,m=50)  # 减少50分钟
# print(new_str_time)  # 2021-07-18 16:29:44
# new_str_time = ct.subTime(str_time,s=21)  # 减少21秒
# print(new_str_time)  # 2021-07-18 17:18:23
# new_str_time = ct.addTime(str_time,d=1,h=8,m=50,s=21)
# print(new_str_time)  # 2021-07-21 18:48:37
#
#
# """ ***** 日计算 ***** """
#
# #获取今日日期
# today = ct.getToday()
# print(today)  # 2021-07-19

# #获取昨日
# yesterday = ct.getYesterday()
# print(yesterday)

# #获取明天
# tomorrow = ct.getTomorrow()
# print(tomorrow)

# # 计算两日期之间的相差多少天数
# start_date = '2021-05-15'
# end_date = '2021-07-18'
# days = ct.deltaDays(start_date,end_date)
# print(days)  # 64
# days = ct.deltaDays(start_date=(2021,7,15),end_date=(2021,7,18))
# print(days)  # 3
#
# # 日期加减
# new_date = ct.dateAdd('2021-07-20',5)
# new_date = ct.dateAdd((2021,7,20),5)
# print(new_date)  # 2021-07-25
#
# new_date = ct.dateAdd('2021-07-20',-5)
# new_date = ct.dateSub('2021-07-20',5)
# print(new_date)  #  2021-07-15
#
#
# # 是否为周一
# result = ct.isMonday('2021-07-19')
# result = ct.isMonday(2021,7,19)
# print(result)  # True
#
# # 是否为周二
# result = ct.isTuesday('2021-07-20')
# result = ct.isTuesday(2021,7,20)
# print(result)  # True
#
# # 是否为周三
# result = ct.isWednesday('2021-07-21')
# result = ct.isWednesday(2021,7,21)
# print(result)  # True
#
# # 是否为周四
# result = ct.isThursday('2021-07-22')
# result = ct.isThursday(2021,7,22)
# print(result)  # True
#
# # 是否为周五
# result = ct.isFriday('2021-07-23')
# result = ct.isFriday(2021,7,23)
# print(result)  # True
#
# # 是否为周六
# result = ct.isSaturday('2021-07-24')
# result = ct.isSaturday(2021,7,24)
# print(result)  # True
#
# # 是否为周日/周末
# result = ct.isSunday('2021-07-25')
# result = ct.isSunday(2021,7,25)
# result = ct.isWeekend('2021-07-25')
# result = ct.isWeekend(2021,7,25)
# print(result)  # True
#
#
# # 获取指定前后日期之间所有日期列表
# start_date = '2021-06-28'
# end_date = '2021-07-18'
# date_list = ct.getDateList(start_date,end_date)
# date_list = ct.getDateList(start_date=(2021,6,28),end_date=(2021,7,18))
# print(date_list)
# ['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03',
#  '2021-07-04', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09',
#  '2021-07-10', '2021-07-11', '2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15',
#  '2021-07-16', '2021-07-17', '2021-07-18']
#
#
#
# # 获取前后日期之间所跨年份
# start_date = '2020-05-15'
# end_date = '2021-07-18'
# years = ct.acrossYears(start_date,end_date)
# print(years)  # [2020, 2021]
# years = ct.acrossYears(start_date=(2020,5,15),end_date=(2021,7,18))
# print(years)  # [2020, 2021]
#
#
# # 获取前后日期之间所跨月份
# start_date = '2020-05-15'
# end_date = '2021-07-18'
# months = ct.acrossMonths(start_date,end_date)
# print(months)  # [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
# months = ct.acrossMonths(start_date=(2020,5,15),end_date=(2021,7,18))
# print(months)  # [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
#
#
# # 获取前后日期之间所跨周
# start_date = '2021-05-15'
# end_date = '2021-07-18'
# weeks = ct.acrossWeeks(start_date,end_date)
# weeks = ct.acrossWeeks(start_date=(2021,5,15),end_date=(2021,7,18))
# print(weeks)
# [['2021-05-10', '2021-05-11', '2021-05-12', '2021-05-13', '2021-05-14', '2021-05-15', '2021-05-16'],
#  ['2021-05-17', '2021-05-18', '2021-05-19', '2021-05-20', '2021-05-21', '2021-05-22', '2021-05-23'],
#  ['2021-05-24', '2021-05-25', '2021-05-26', '2021-05-27', '2021-05-28', '2021-05-29', '2021-05-30'],
#  ['2021-05-31', '2021-06-01', '2021-06-02', '2021-06-03', '2021-06-04', '2021-06-05', '2021-06-06'],
#  ['2021-06-07', '2021-06-08', '2021-06-09', '2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13'],
#  ['2021-06-14', '2021-06-15', '2021-06-16', '2021-06-17', '2021-06-18', '2021-06-19', '2021-06-20'],
#  ['2021-06-21', '2021-06-22', '2021-06-23', '2021-06-24', '2021-06-25', '2021-06-26', '2021-06-27'],
#  ['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'],
#  ['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
#  ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']]
#
#
# # 获取前后日期之间的所有星期一
# start_date = '2021-05-15'
# end_date = '2021-07-18'
# Mondays = ct.getMondays(start_date,end_date)
# Mondays = ct.getMondays(start_date=(2021,5,15),end_date=(2021,7,18))
# Mondays = ct.getDatesByNumber(start_date,end_date,1)
# Mondays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=1)
# print(Mondays)
# ['2021-05-17', '2021-05-24', '2021-05-31',
# '2021-06-07', '2021-06-14', '2021-06-21',
# '2021-06-28', '2021-07-05', '2021-07-12']
#
# # 获取前后日期之间的所有星期二
# Tuesdays = ct.getTuesdays(start_date,end_date)
# Tuesdays = ct.getTuesdays(start_date=(2021,5,15),end_date=(2021,7,18))
# Tuesdays = ct.getDatesByNumber(start_date,end_date,2)
# Tuesdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=2)
# print(Tuesdays)
# ['2021-05-18', '2021-05-25', '2021-06-01', '2021-06-08', '2021-06-15',
#  '2021-06-22', '2021-06-29', '2021-07-06', '2021-07-13']
#
# # 获取前后日期之间的所有星期三
# Wednesdays = ct.getWednesdays(start_date,end_date)
# Wednesdays = ct.getWednesdays(start_date=(2021,5,15),end_date=(2021,7,18))
# Wednesdays = ct.getDatesByNumber(start_date,end_date,3)
# Wednesdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=3)
# print(Wednesdays)
# ['2021-05-19', '2021-05-26', '2021-06-02', '2021-06-09', '2021-06-16',
#  '2021-06-23','2021-06-30', '2021-07-07', '2021-07-14']
#
#
# # 获取前后日期之间的所有星期四
# Thursdays = ct.getThursdays(start_date,end_date)
# Thursdays = ct.getThursdays(start_date=(2021,5,15),end_date=(2021,7,18))
# Thursdays = ct.getDatesByNumber(start_date,end_date,4)
# Thursdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=4)
# print(Thursdays)
# ['2021-05-20', '2021-05-27', '2021-06-03', '2021-06-10', '2021-06-17',
#  '2021-06-24', '2021-07-01', '2021-07-08', '2021-07-15']
#
#
# # 获取前后日期之间的所有星期五
# Fridays = ct.getFridays(start_date,end_date)
# Fridays = ct.getFridays(start_date=(2021,5,15),end_date=(2021,7,18))
# Fridays = ct.getDatesByNumber(start_date,end_date,5)
# Fridays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=5)
# print(Fridays)
# ['2021-05-21', '2021-05-28', '2021-06-04', '2021-06-11',
#  '2021-06-18', '2021-06-25', '2021-07-02', '2021-07-09', '2021-07-16']
#
# # 获取前后日期之间的所有星期六
# Saturdays = ct.getSaturdays(start_date,end_date)
# Saturdays = ct.getSaturdays(start_date=(2021,5,15),end_date=(2021,7,18))
# Saturdays = ct.getDatesByNumber(start_date,end_date,6)
# Saturdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=6)
# print(Saturdays)
# ['2021-05-15', '2021-05-22', '2021-05-29', '2021-06-05', '2021-06-12',
#  '2021-06-19','2021-06-26', '2021-07-03', '2021-07-10', '2021-07-17']
#
#
# # 获取前后日期之间的所有星期天
# Sundays = ct.getSundays(start_date,end_date)
# Sundays = ct.getSundays(start_date=(2021,5,15),end_date=(2021,7,18))
# Sundays = ct.getDatesByNumber(start_date,end_date,7)
# Sundays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=7)
# print(Sundays)
# ['2021-05-16', '2021-05-23', '2021-05-30', '2021-06-06', '2021-06-13',
#  '2021-06-20', '2021-06-27', '2021-07-04', '2021-07-11', '2021-07-18']

#
#
#
#
# """ ***** 周 ***** """
#
# #获取指定日期的所在周几数值
# weekday_number = ct.getWeekdayNumber(2021,7,16)
# weekday_number = ct.getWeekdayNumber('2021-07-16')
# print(weekday_number) # 5
#
#
# # 获取指定日期的周几名称
# weekday_cname = ct.getWeekdayCName(2021,7,16)
# weekday_cname = ct.getWeekdayCName('2021-07-16')
# print(weekday_cname)  # 周五
#
#
# # 判定是否为周末 也就是星期天
#
# isWeekend = ct.isWeekend(2021,7,16)
# print(isWeekend)  # False
# isWeekend = ct.isWeekend('2021-07-18')
# print(isWeekend)  # True
#
#
#
# #获取本周起始日期与结束日期
# current_week_start,current_week_end = ct.getCurrentWeekStartAndEnd()
# print(current_week_start,current_week_end) # 2021-07-19 2021-07-25
#
# #获取上周起始日期与结束日期
# last_week_start,last_week_end = ct.getLastWeekStartAndEnd()
# print(last_week_start,last_week_end)
#
# #获取下周起始日期与结束日期
# next_week_start,next_week_end = ct.getNextWeekStartAndEnd()
# print(next_week_start,next_week_end)
#
# #获取指定日期所在周的起始与结束日期
# week_start, week_end = ct.getWeekStartAndEnd(2021, 7, 16)
# week_start, week_end = ct.getWeekStartAndEnd('2021-07-16')
# print(week_start, week_end) # '2021-07-12', '2021-07-18'
#
#
# # 获取指定某天所在周的所有日期列表
# weekdates = ct.getWeekDates('2021-07-16')
# weekdates = ct.getWeekDates(2021,7,16)
# print(weekdates)  # ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']
#
#
#
#
# # 获取指定两日期之间所跨周
# start_date = '2021-07-01'
# end_date = '2021-07-18'
#
# weeks = ct.acrossWeeks(start_date,end_date)
# weeks = ct.acrossWeeks(start_date=(2021,7,1),end_date=(2021,7,18))
# print(len(weeks))
# print(weeks)
#
# 3
# [['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'],
#  ['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
#  ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']]
#


""" ***** 月 ***** """


# # 月份加减
# new_date = ct.monthAdd('2021-12-03',11)
# print(new_date) #2022-11-3
# new_date = ct.monthAdd('2021-12-03',-11)
# print(new_date) #2021-01-03
# new_date = ct.monthSub('2021-12-03',11)
# print(new_date)
# 判定指定月份是否为31天
# isMonth31 = ct.isMonth31(8)
# isMonth31 = ct.isMonth31('8')
# print(isMonth31)
#
#
#
# #获取月起始日期与结束日期
#
# #获取本月起始与结束日期
# current_month_start,current_month_end = ct.getCurrentMonthStartAndEnd()
# print(current_month_start,current_month_end)  # 2021-07-01 2021-07-31
#
# #获取上月起始与结束日期
# last_month_start,last_month_end = ct.getLastMonthStartAndEnd()
# print(last_month_start,last_month_end)  # 2021-06-01 2021-06-30
#
# #获取下月起始与结束日期
# next_month_start,next_month_end = ct.getNextMonthStartAndEnd()
# print(next_month_start,next_month_end)  # 2021-08-01 2021-08-31
#
#
# # 获取指定某天所在月份的起始与结束日期
# start_day,end_day = ct.getMonthStartAndEnd(2021,7,16)
# start_day,end_day = ct.getMonthStartAndEnd('2021-07-16')
# print(start_day,end_day)  #  2021-07-01 2021-07-31
#
#
#
# # 获取指定年月的所有日期列表
# month_dates = ct.getMonthDateList(2021,2)
# month_dates = ct.getMonthDateList(date='2021-02-01')
# month_dates = ct.getMonthDateList(date=(2021,2,12))
# print(month_dates)
# ['2021-02-01', '2021-02-02', '2021-02-03', '2021-02-04', '2021-02-05', '2021-02-06', '2021-02-07',
#  '2021-02-08', '2021-02-09', '2021-02-10', '2021-02-11', '2021-02-12', '2021-02-13', '2021-02-14',
#  '2021-02-15', '2021-02-16', '2021-02-17', '2021-02-18', '2021-02-19', '2021-02-20', '2021-02-21',
#  '2021-02-22', '2021-02-23', '2021-02-24', '2021-02-25', '2021-02-26', '2021-02-27', '2021-02-28']
#
#
#
# #获取指定年月所有周
# month_weeks = ct.getMonthWeeks(2021,7)
# month_weeks = ct.getMonthWeeks(date='2021-07-02')
# month_weeks = ct.getMonthWeeks(date=(2021,7,2))
# print(month_weeks)
# [['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'],
#  ['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
#  ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18'],
#  ['2021-07-19', '2021-07-20', '2021-07-21', '2021-07-22', '2021-07-23', '2021-07-24', '2021-07-25']]
#

#
# """ ***** 年 ***** """
#
# # 判定是否为闰年
#
# result = ct.isLeapyear(2021)
# print(result)  # False
#
#
# # 获取指定年份的天数
# days = ct.getYearDays(2020)
# print(days)  # 366


