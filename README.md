# cgai-time

#### 介绍
简单又实用的时间python处理库

#### 注意

非时分秒日期格式：    
1. 推荐的日期格式为%Y-%m-%d，比如：2021-07-20
2. 也支持数字数组格式表示，比如： (2021,7,20)

时分秒格式：
1. 仅支持%Y-%m-%d %H:%M:%S，比如："2021-07-20 09:43:49"
2. 建议以时间戳的形式计算时间计算，最后显示格式化日期

#### 安装教程

```python
pip install cgai-time
```

#### 案例

说明：案例中演示了多个函数不同参数的实现方式，结果一致

#### 实例时间工具
```python
from cgai_time.Time import TimeHandler
ct = TimeHandler()
```

#### 日期格式转化

##### 字符串格式转成数组格式: "2021-07-16" -> (2021,7,16)
```python
t_date = ct.strDate2TupleDate('2021-07-16')
print(t_date) # (2021,7,16)
```

##### 数组格式转成字符串格式:  (2021,7,16) -> "2021-07-16"
```python
s_date = ct.tupleDate2StrDate((2021,7,16))
print(s_date) # "2021-07-16"
```

##### 格式化日期转时间戳 
```python
str_time = '2021-07-18 17:19:44'
time_stamp = ct.strTime2TimeStamp(str_time)
print(time_stamp) # 1626599984.0
```

##### 时间戳转格式化日期时间 
```python
time_stamp = 1626599984.0
str_time = ct.timeStamp2StrTime(time_stamp)
print(str_time) # "2021-07-18 17:19:44"
```

##### 将斜杠/日期转成减号-日期 
```python
slash_date = '2023/3/6'
sdate = ct.slashDate2StrDate(slash_date)
print(sdate)  # 2023-03-06
```
##### 将减号-日期转成斜杠/日期
```python
date = '2023-03-06'
slash_date = ct.strDate2SlashDate(date)
print(slash_date) # 2023/3/6
```


##### 秒数转分钟 
```python
seconds = 70
minutes = ct.s2m(seconds)
int_minutes = ct.s2m(seconds,getInt=True)  # 获取整数部分
print(minutes) # 1.1666666666666667
print(int_minutes) # 1
```

##### 分钟转秒数 
```python
minutes = 12.015
seconds = ct.m2s(minutes)
int_seconds = ct.m2s(minutes,getInt=True)
print(seconds)  # 720.9000000000001
print(int_seconds)  # 720
```

##### 秒转小时 
```python
seconds = 1244
hours = ct.s2h(seconds)
int_hours = ct.s2h(seconds,getInt=True)
print(hours)  # 0.34555555555555556
print(int_hours)  # 0
```

##### 小时转秒 
```python
hours = 0.342
seconds = ct.h2s(hours)
int_seconds = ct.h2s(hours,getInt=True)
print(seconds)  # 1231.2000000000003
print(int_seconds)  # 1231
```

##### 秒转天数 
```python
seconds = 112341
days = ct.s2d(seconds)
int_days = ct.s2d(seconds,getInt=True)
print(days)  # 1.3002430555555555
print(int_days) # 1
```

##### 天数转秒 
```python
days = 0.451
seconds = ct.d2s(days)
int_seconds = ct.d2s(days,getInt=True)
print(seconds)  # 38966.399999999994
print(int_seconds)  # 38966
```

##### 分钟转小时 
```python
minutes = 1234
hours = ct.m2h(minutes)
int_hours = ct.m2h(minutes,getInt=True)
print(hours)  # 20.566666666666666
print(int_hours)  # 20
```

##### 小时转分钟
```python
hours = 0.241
minutes = ct.h2m(hours)
int_minutes = ct.h2m(hours,getInt=True)
print(minutes)  #  14.459999999999999
print(int_minutes)  # 14

```

##### 分钟转天数 
```python
minutes = 421321
days = ct.m2d(minutes)
int_days = ct.m2d(minutes,getInt=True)
print(days)  # 292.5840277777778
print(int_days) # 292
```

##### 天数转分钟 
```python
days = 0.912
minutes = ct.d2m(days)
int_minutes = ct.d2m(days,getInt=True)
print(minutes)  # 1313.2800000000002
print(int_minutes)  # 1313
```

##### 小时转天数 
```python
hours = 482
days = ct.h2d(hours)
int_days = ct.h2d(hours,getInt=True)
print(days)  # 20.083333333333332
print(int_days)  # 20
```

##### 天转小时 
```python
days = 0.924
hours = ct.d2h(days)
int_hours = ct.d2h(days,getInt=True)
print(hours)  #  22.176000000000002
print(int_hours)  # 22
```

##### 小时转毫秒
```python
hours = 2.5
int_h,left_ms = ct.h2ms(hours)
```

##### 毫秒转小时
```python
ms = 4600
int_h,left_ms = ct.ms2h(ms)
```


##### 分钟转毫秒
```python
minutes = 1.5
ms = ct.m2ms(minutes)
```

##### 毫秒转分钟
```python
ms = 4600
int_m,left_ms = ct.ms2m(ms)
```

##### 秒转毫秒
```python
seconds = 2.5
ms = ct.s2ms(seconds)
```

##### 毫秒转秒
```python
ms = 4600
int_s,left_ms = ct.ms2s(ms)
```

##### 输入天数，小时，分钟转成秒 
```python
seconds = ct.getSeconds(d=1,h=3,m=25)
print(seconds)  # 98700
seconds = ct.getSeconds(h=3,m=25)
print(seconds)  # 12300
```

##### 将秒数转成以天,小时,分钟,秒对应值 
```python
seconds = 3600*24+3599
dhms = ct.DHMS(seconds)
print(dhms) #{'day': 1, 'hour': 0, 'minute': 59, 'second': 59}
```


##### 字幕时间转毫秒
```python
srt = '00:02:42,950'
ms= ct.srt2ms(srt)
print(ms)  # 162950
```

##### 毫秒转字幕时间
```python
ms = 4600
srt= ct.ms2srt(ms)
print(srt) # 00:00:04,600
```


#### 时间计算

##### 获取当前时间戳 
```python
cts = ct.CTS()
print(cts)  #  1626660957.2461472
```

##### 获取当前格式化日期时间 
```python
str_time = ct.StrTime()
print(str_time)  #  2021-07-20 09:43:49
```

##### 计算两格式化日期之间的所差秒数 
```python
start_date = '2021-07-18 17:19:44'
end_date = '2021-07-18 22:32:11'
dt = ct.deltaTime(end_date,start_date)
print(dt)  # 18747.0
```

##### 格式化日期直接进行时间增减 
```python
str_time = '2021-07-18 17:19:44'
new_str_time = ct.addTime(str_time,d=1)  # 增加一天
print(new_str_time)  # 2021-07-19 17:19:44
new_str_time = ct.addTime(str_time,h=8)  # 增加8小时
print(new_str_time)  # 2021-07-19 01:19:44
new_str_time = ct.subTime(str_time,m=50)  # 减少50分钟
print(new_str_time)  # 2021-07-18 16:29:44
new_str_time = ct.subTime(str_time,s=21)  # 减少21秒
print(new_str_time)  # 2021-07-18 17:18:23
new_str_time = ct.addTime(str_time,d=1,h=8,m=50,s=21) 
print(new_str_time)  # 2021-07-21 18:48:37
```

##### 字幕时间增减毫秒
```python
start_srt_time = '00:02:42,950'
ms = 4600
end_srt_time = ct.srt_add(start_srt_time,ms)
print(end_srt_time)  # 00:02:47,550

end_srt_time = ct.srt_sub(start_srt_time,ms)
print(end_srt_time)  #  00:02:38,350
```



#### 日计算

##### 获取今日日期
```python
today = ct.getToday()
print(today)  # 2021-07-19
```
##### 获取昨天日期
```python
yesterday = ct.getYesterday()
print(yesterday)  # 2021-07-18
```
##### 获取明天日期
```python
tomorrow = ct.getTomorrow()
print(tomorrow)  # 2021-07-20
```

##### 计算两日期之间的相差多少天数 
```python
start_date = '2021-05-15'
end_date = '2021-07-18'
days = ct.deltaDays(start_date,end_date)
print(days)  # 64
days = ct.deltaDays(start_date=(2021,7,15),end_date=(2021,7,18))
print(days)  # 3
```

##### 日期加减 
```python
new_date = ct.dateAdd('2021-07-20',5)
new_date = ct.dateAdd((2021,7,20),5)
print(new_date)  # 2021-07-25

new_date = ct.dateAdd('2021-07-20',-5)
new_date = ct.dateSub('2021-07-20',5)
print(new_date)  #  2021-07-15
```

##### 是否为周一 
```python
result = ct.isMonday('2021-07-19')
result = ct.isMonday(2021,7,19)
print(result)  # True
```

##### 是否为周二 
```python
result = ct.isTuesday('2021-07-20')
result = ct.isTuesday(2021,7,20)
print(result)  # True
```

##### 是否为周三 
```python
result = ct.isWednesday('2021-07-21')
result = ct.isWednesday(2021,7,21)
print(result)  # True
```

##### 是否为周四 
```python
result = ct.isThursday('2021-07-22')
result = ct.isThursday(2021,7,22)
print(result)  # True
```

##### 是否为周五 
```python
result = ct.isFriday('2021-07-23')
result = ct.isFriday(2021,7,23)
print(result)  # True
```

##### 是否为周六 
```python
result = ct.isSaturday('2021-07-24')
result = ct.isSaturday(2021,7,24)
print(result)  # True
```

##### 是否为周日/周末 
```python
result = ct.isSunday('2021-07-25')
result = ct.isSunday(2021,7,25)
result = ct.isWeekend('2021-07-25')
result = ct.isWeekend(2021,7,25)
print(result)  # True
```

##### 获取指定前后日期之间所有日期列表 
```python
start_date = '2021-06-28'
end_date = '2021-07-18'
date_list = ct.getDateList(start_date,end_date)
date_list = ct.getDateList(start_date=(2021,6,28),end_date=(2021,7,18))
print(date_list)
['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03',
 '2021-07-04', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09',
 '2021-07-10', '2021-07-11', '2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15',
 '2021-07-16', '2021-07-17', '2021-07-18']
```

##### 获取前后日期之间所跨年份 
```python
start_date = '2020-05-15'
end_date = '2021-07-18'
years = ct.acrossYears(start_date,end_date)
print(years)  # [2020, 2021]
years = ct.acrossYears(start_date=(2020,5,15),end_date=(2021,7,18))
print(years)  # [2020, 2021]
```

##### 获取前后日期之间所跨月份 
```python
start_date = '2020-05-15'
end_date = '2021-07-18'
months = ct.acrossMonths(start_date,end_date)
print(months)  # [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
months = ct.acrossMonths(start_date=(2020,5,15),end_date=(2021,7,18))
print(months)  # [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
```

##### 获取前后日期之间所跨周 
```python
start_date = '2021-05-15'
end_date = '2021-07-18'
weeks = ct.acrossWeeks(start_date,end_date)
weeks = ct.acrossWeeks(start_date=(2021,5,15),end_date=(2021,7,18))
print(weeks)  
[['2021-05-10', '2021-05-11', '2021-05-12', '2021-05-13', '2021-05-14', '2021-05-15', '2021-05-16'],
 ['2021-05-17', '2021-05-18', '2021-05-19', '2021-05-20', '2021-05-21', '2021-05-22', '2021-05-23'],
 ['2021-05-24', '2021-05-25', '2021-05-26', '2021-05-27', '2021-05-28', '2021-05-29', '2021-05-30'],
 ['2021-05-31', '2021-06-01', '2021-06-02', '2021-06-03', '2021-06-04', '2021-06-05', '2021-06-06'],
 ['2021-06-07', '2021-06-08', '2021-06-09', '2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13'],
 ['2021-06-14', '2021-06-15', '2021-06-16', '2021-06-17', '2021-06-18', '2021-06-19', '2021-06-20'],
 ['2021-06-21', '2021-06-22', '2021-06-23', '2021-06-24', '2021-06-25', '2021-06-26', '2021-06-27'],
 ['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'],
 ['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
 ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']]

```

##### 获取指定日期范围内所跨的月初日期
```python
start_date = "2024-01-02"
end_date = "2025-12-24"
month_start_dates = ct.getStartDateAcrossMonths(start_date,end_date)
print(month_start_dates)
['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01', 
 '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01', '2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', 
 '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01', '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01']
```




##### 获取前后日期之间的所有星期一 
```python
start_date = '2021-05-15'
end_date = '2021-07-18'
Mondays = ct.getMondays(start_date,end_date)
Mondays = ct.getMondays(start_date=(2021,5,15),end_date=(2021,7,18))
Mondays = ct.getDatesByNumber(start_date,end_date,1)
Mondays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=1)
print(Mondays)
['2021-05-17', '2021-05-24', '2021-05-31',
'2021-06-07', '2021-06-14', '2021-06-21',
'2021-06-28', '2021-07-05', '2021-07-12']
```

##### 获取前后日期之间的所有星期二 
```python
Tuesdays = ct.getTuesdays(start_date,end_date)
Tuesdays = ct.getTuesdays(start_date=(2021,5,15),end_date=(2021,7,18))
Tuesdays = ct.getDatesByNumber(start_date,end_date,2)
Tuesdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=2)
print(Tuesdays)
['2021-05-18', '2021-05-25', '2021-06-01', '2021-06-08', '2021-06-15',
 '2021-06-22', '2021-06-29', '2021-07-06', '2021-07-13']
```

##### 获取前后日期之间的所有星期三 
```python
Wednesdays = ct.getWednesdays(start_date,end_date)
Wednesdays = ct.getWednesdays(start_date=(2021,5,15),end_date=(2021,7,18))
Wednesdays = ct.getDatesByNumber(start_date,end_date,3)
Wednesdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=3)
print(Wednesdays)
['2021-05-19', '2021-05-26', '2021-06-02', '2021-06-09', '2021-06-16',
 '2021-06-23','2021-06-30', '2021-07-07', '2021-07-14']
```

##### 获取前后日期之间的所有星期四 
```python
Thursdays = ct.getThursdays(start_date,end_date)
Thursdays = ct.getThursdays(start_date=(2021,5,15),end_date=(2021,7,18))
Thursdays = ct.getDatesByNumber(start_date,end_date,4)
Thursdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=4)
print(Thursdays)
['2021-05-20', '2021-05-27', '2021-06-03', '2021-06-10', '2021-06-17',
 '2021-06-24', '2021-07-01', '2021-07-08', '2021-07-15']
```

##### 获取前后日期之间的所有星期五 
```python
Fridays = ct.getFridays(start_date,end_date)
Fridays = ct.getFridays(start_date=(2021,5,15),end_date=(2021,7,18))
Fridays = ct.getDatesByNumber(start_date,end_date,5)
Fridays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=5)
print(Fridays)
['2021-05-21', '2021-05-28', '2021-06-04', '2021-06-11',
 '2021-06-18', '2021-06-25', '2021-07-02', '2021-07-09', '2021-07-16']
```

##### 获取前后日期之间的所有星期六 
```python
Saturdays = ct.getSaturdays(start_date,end_date)
Saturdays = ct.getSaturdays(start_date=(2021,5,15),end_date=(2021,7,18))
Saturdays = ct.getDatesByNumber(start_date,end_date,6)
Saturdays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=6)
print(Saturdays)
['2021-05-15', '2021-05-22', '2021-05-29', '2021-06-05', '2021-06-12',
 '2021-06-19','2021-06-26', '2021-07-03', '2021-07-10', '2021-07-17']
```

##### 获取前后日期之间的所有星期天 
```python
Sundays = ct.getSundays(start_date,end_date)
Sundays = ct.getSundays(start_date=(2021,5,15),end_date=(2021,7,18))
Sundays = ct.getDatesByNumber(start_date,end_date,7)
Sundays = ct.getDatesByNumber(start_date=(2021,5,15),end_date=(2021,7,18),number=7)
print(Sundays)
['2021-05-16', '2021-05-23', '2021-05-30', '2021-06-06', '2021-06-13',
 '2021-06-20', '2021-06-27', '2021-07-04', '2021-07-11', '2021-07-18']
```



#### 周计算

##### 获取指定日期的所在周几数值 
```python
weekday_number = ct.getWeekdayNumber(2021,7,16)
weekday_number = ct.getWeekdayNumber('2021-07-16')
print(weekday_number) # 5

```

##### 获取指定日期的周几名称 
```python
weekday_cname = ct.getWeekdayCName(2021,7,16)
weekday_cname = ct.getWeekdayCName('2021-07-16')
print(weekday_cname) # 周五
```

##### 判定是否为周末 也就是星期天 
```python
isWeekend = ct.isWeekend(2021,7,16)
print(isWeekend)  # False
isWeekend = ct.isWeekend('2021-07-18')
print(isWeekend)  # True
```

##### 获取本周起始日期与结束日期 
```python
current_week_start,current_week_end = ct.getCurrentWeekStartAndEnd()
print(current_week_start,current_week_end)  # 2021-07-19 2021-07-25
```

##### 获取上周起始日期与结束日期 
```python
last_week_start,last_week_end = ct.getLastWeekStartAndEnd()
print(last_week_start,last_week_end)  # 2021-07-12 2021-07-18
```

##### 获取下周起始日期与结束日期 
```python
next_week_start,next_week_end = ct.getNextWeekStartAndEnd()
print(next_week_start,next_week_end)  # 2021-07-26 2021-08-01
```

##### 获取指定日期所在周的起始与结束日期 
```python
week_start, week_end = ct.getWeekStartAndEnd(2021, 7, 16)
week_start, week_end = ct.getWeekStartAndEnd('2021-07-16')
print(week_start, week_end) # '2021-07-12', '2021-07-18'
```

##### 获取指定某天所在周的所有日期列表 
```python
weekdates = ct.getWeekDates('2021-07-16')
weekdates = ct.getWeekDates(2021,7,16)
print(weekdates)  # ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']
```

##### 获取指定两日期之间所跨周 
```python
start_date = '2021-07-15'
end_date = '2021-07-18'

weeks = ct.acrossWeeks(start_date,end_date)
weeks = ct.acrossWeeks(start_date=(2021,7,1),end_date=(2021,7,18))
print(len(weeks))
print(weeks)

3
[['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'], 
['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
 ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18']]
```


#### 月操作

##### 月份加减
```python
new_date = ct.monthAdd('2021-12-03',11)
print(new_date) #2022-11-3
new_date = ct.monthAdd('2021-12-03',-11)
print(new_date) #2021-01-03
```

##### 判定指定月份是否为31天 
```python
isMonth31 = ct.isMonth31(8)
isMonth31 = ct.isMonth31('8')
print(isMonth31)  # True
```

##### 获取本月起始与结束日期 
```python
current_month_start,current_month_end = ct.getCurrentMonthStartAndEnd()
print(current_month_start,current_month_end)  # 2021-07-01 2021-07-31
```

##### 获取上月起始与结束日期 
```python
last_month_start,last_month_end = ct.getLastMonthStartAndEnd()
print(last_month_start,last_month_end)  # 2021-06-01 2021-06-30
```

##### 获取下月起始与结束日期 
```python
next_month_start,next_month_end = ct.getNextMonthStartAndEnd()
print(next_month_start,next_month_end)  # 2021-08-01 2021-08-31
```

##### 获取指定某天所在月份的起始与结束日期 
```python
start_day,end_day = ct.getMonthStartAndEnd(2021,7,16)
start_day,end_day = ct.getMonthStartAndEnd('2021-07-16')
print(start_day,end_day)  #  2021-07-01 2021-07-31

```

##### 获取指定年指定月的所有日期列表 
```python
month_dates = ct.getMonthDateList(2021,2)
month_dates = ct.getMonthDateList(date='2021-02-01')
month_dates = ct.getMonthDateList(date=(2021,2,12))
print(month_dates)
['2021-02-01', '2021-02-02', '2021-02-03', '2021-02-04', '2021-02-05', '2021-02-06', '2021-02-07',
 '2021-02-08', '2021-02-09', '2021-02-10', '2021-02-11', '2021-02-12', '2021-02-13', '2021-02-14',
 '2021-02-15', '2021-02-16', '2021-02-17', '2021-02-18', '2021-02-19', '2021-02-20', '2021-02-21',
 '2021-02-22', '2021-02-23', '2021-02-24', '2021-02-25', '2021-02-26', '2021-02-27', '2021-02-28']

```

##### 获取指定年月所有周 
```python
month_weeks = ct.getMonthWeeks(2021,7)
month_weeks = ct.getMonthWeeks(date='2021-07-02')
month_weeks = ct.getMonthWeeks(date=(2021,7,2))
print(month_weeks)
[['2021-06-28', '2021-06-29', '2021-06-30', '2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04'],
 ['2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11'],
 ['2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18'],
 ['2021-07-19', '2021-07-20', '2021-07-21', '2021-07-22', '2021-07-23', '2021-07-24', '2021-07-25']]

```

#### 季度计算

##### 获取指定天所在的季度信息
```python
date = '2023-03-23'
quarter_number,quarter_list = ct.getQuarter(date)
print(quarter_number,quarter_list)  # 1  [1,2,3]    表示是在第一季度,该季度有1,2,3个月

```

##### 获取指定天所在的季度的各月起始日期
```python
date = '2023-03-23'
quarter_start_dates = ct.getQuarterStartDates(date)
print(quarter_start_dates)  # ['2023-01-01', '2023-02-01', '2023-03-01']   
```
##### 获取本季度的各月起始日期
```python
quarter_start_dates = ct.getCurrentQuarterStartDates()
print(quarter_start_dates)  # ['2023-01-01', '2023-02-01', '2023-03-01'] 
```
##### 获取上季度的各月起始日期
```python
quarter_start_dates = ct.getLastQuarterStartDates()
print(quarter_start_dates)  # ['2022-10-01', '2022-11-01', '2022-12-01'] 
```

##### 获取下季度的各月起始日期
```python
quarter_start_dates = ct.getNextQuarterStartDates()
print(quarter_start_dates)  # ['2023-04-01', '2023-05-01', '2023-06-01'] 
```

##### 基于指定天进行季度相加，返回季度的各月起始日期
```python
date = '2022-02-02'
quarter_start_dates = ct.quarterAdd(date,3)   # 该天所在季度向后再加3个季度
print(quarter_start_dates)  # ['2022-10-01', '2022-11-01', '2022-12-01']  
```

##### 基于指定天进行季度相减，返回季度的各月起始日期
```python
date = '2022-03-23'
quarter_start_dates = ct.quarterSub(date,3)   # 该天所在季度向前再减3个季度
print(quarter_start_dates)  # ['2021-04-01', '2021-05-01', '2021-06-01'] 
```


#### 年计算

##### 判定是否为闰年 
```python
result = ct.isLeapyear(2021)
print(result)  # False
```
##### 获取指定年份的天数 
```python
days = ct.getYearDays(2020)
print(days)  # 366
```

