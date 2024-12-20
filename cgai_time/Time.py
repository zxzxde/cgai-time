# -*- coding:utf-8 -*-
"""
日期处理类
"""

import time
import datetime
from dateutil.relativedelta import relativedelta
from functools import wraps

# 将字符串日期转成整数的数组日期
def cgai_time_args_tuple(fun):
    @wraps(fun)
    def new_func(*args):
        first_arg = args[0]
        if isinstance(first_arg,TimeHandler):  # 当是直接调用类函数时,首参数为self
            input_args = args if len(args) > 2 else [args[0]]
            if len(args) == 2:
                s_args = args[1].split('-')
                for arg in s_args:
                    input_args.append(int(arg))
        else:  # 当是类中函数调用时，不带self
            input_args = args if len(args) > 1 else []
            if len(args) == 1:
                s_args = args[0].split('-')
                # print('s_args:',s_args)
                for arg in s_args:
                    input_args.append(int(arg))
        return fun(*input_args)

    return new_func


def cgai_time_args_int(fun):
    @wraps(fun)
    def new_func(*args):
        input_args = args if len(args) > 2 else [args[0]]
        if len(args) == 2:
            if isinstance(args[1],str):
                s_args = args[1].split('-')
                input_args.append(int(s_args[0]))
            else:
                input_args.append(args[1])
        return fun(*input_args)
    return new_func

# 将数组日期转成字符串日期
def cgai_time_args_str(fun):
    """
    返回字符串格式
    :param fun:
    :return:
    """
    def int2str(number:int):
        '''
        如果day小于10，则返回加0字符串
        :param day:
        :return:
        '''
        if number < 10:
            return '0' + str(number)
        else:
            return str(number)

    @wraps(fun)
    def new_func(*args):
        first_arg = args[0]
        if isinstance(first_arg,TimeHandler):
            str_arg = args[1] if len(args) == 2 else ''
            input_args = []
            if len(args) > 2:
                for arg in args[1:]:
                    input_args.append(int2str(arg))
                str_arg = '-'.join(input_args)
            return fun(args[0],str_arg)
        else:  # 类中调用，不带self
            str_arg = first_arg if len(args) == 1 else ''
            input_args = []
            if len(args) > 1:
                for arg in args:
                    input_args.append(int2str(arg))
                str_arg = '-'.join(input_args)
            return fun(str_arg)

    return new_func

# 将输入的数组日期转成字符串格式,如果是字符串输入则不做处理
def cgai_time_args_strs(fun):
    """
    返回字符串格式
    :param fun:
    :return:
    """
    def int2str(number:int):
        '''
        如果day小于10，则返回加0字符串
        :param day:
        :return:
        '''
        if number < 10:
            return '0' + str(number)
        else:
            return str(number)

    def tuple2str(t:tuple):
        arg_list = []
        for i in t:
            arg_list.append(int2str(i))
        return '-'.join(arg_list)

    @wraps(fun)
    def new_func(*args,**kwargs):
        new_args = []
        for i in args:
            arg = i
            if not isinstance(i,TimeHandler):
                arg = i if not isinstance(i, tuple) else tuple2str(i)
            new_args.append(arg)

        new_kwargs = {}
        for k,v in kwargs.items():
            arg = v if not isinstance(v, tuple) else tuple2str(v)
            new_kwargs[k] = arg
        return fun(*new_args,**new_kwargs)

    return new_func




def clip_list(src_list,count):  #src_list为原列表，count为等分长度
    clip_back=[]
    if len(src_list) > count:
        for i in range(int(len(src_list) / count)):
            clip_a = src_list[count * i:count * (i + 1)]
            clip_back.append(clip_a)
        # last 剩下的单独为一组
        last = src_list[int(len(src_list) / count) * count:]
        if last:
            clip_back.append(last)
    else:  #如果切分长度不小于原列表长度，那么直接返回原列表
        clip_back = [src_list] # 如果返回结构保持一致可以返回clip_back = [src_list]

    return clip_back


S = 1
M = S * 60
H = M * 60
D = H * 24


class TimeHandler(object):
    def __init__(self):
        super(TimeHandler, self).__init__()


    """

        *******************************************
            格式转化
        *******************************************

    """
    def strDate2TupleDate(self,str_date:str):
        """
        将2021-07-18这种格式转化成(2021,7,18)这种格式
        :param str_date:
        :return:
        """

        return tuple(int(i) for i in str_date.split('-'))

    def tupleDate2StrDate(self,tuple_date:tuple):
        """
        将(2021,7,18)转化为'2021-07-18'
        :param tuple_date:
        :return:
        """

        def int2str(number: int):
            '''
            如果day小于10，则返回加0字符串
            :param day:
            :return:
            '''
            if number < 10:
                return '0' + str(number)
            else:
                return str(number)

        t_list = [int2str(i) for i in tuple_date]
        return '-'.join(t_list)

    def slashDate2StrDate(self,slash_date):
        """
        将斜杠/日期转成减号-日期
        :param slash_date: 2023/3/6
        :return: str   2023-03-06
        """
        s_date = slash_date
        if '/' in slash_date:
            year,month,day = slash_date.split('/')
            imonth = int(month)
            iday = int(day)
            s_date = f'{year}-{imonth:02d}-{iday:02d}'

        return s_date

    def strDate2SlashDate(self,date):
        """
        将减号-日期转成斜杠/日期
        :param date: 2023-03-06 
        :return: str   2023/3/6
        """
        s_date = date
        if '-' in date:
            year,month,day = date.split('-')
            imonth = int(month)
            iday = int(day)
            s_date = f'{year}/{imonth}/{iday}'

        return s_date


    def strTime2TimeStamp(self,str_time:str):
        """
        将字符串时间数据转成时间戳
        :param str_time:
        :return:
        """
        ts = time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S"))
        return ts
    
    def strTime2UTC(self,str_time:str):
        """
        将字符串时间数据转成UTC格式
        :param str_time:
        :return:
        """
        splist = str_time.split(' ')
        if len(splist) == 1: # 仅一个日期
            utc = str_time + 'T00:00:00Z'
        elif len(splist) == 2:  # 正常2个,带时间
            utc = f'{splist[0]}T{splist[1]}Z'
        return utc



    def timeStamp2StrTime(self, time_stamp: float):
        """
        将时间戳转成字符串日期时间
        :param time_stamp:
        :return:
        """
        strtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))

        return strtime

    def s2m(self,seconds:int,getInt=False):
        """
        秒转分钟
        :param seconds: 秒数
        :param getInt: 是否获取整数部分
        :return:
        """
        return seconds/M if not getInt else int(seconds/M)

    def m2s(self,minutes:float,getInt=False):
        """
        分钟数转秒数
        :param minute: 分钟数
        :param getInt: 是否获取整数部分
        :return:
        """

        return minutes*60 if not getInt else int(minutes*60)


    def s2h(self, seconds: object, getInt: object = False) -> object:
        """
        秒转小时
        :param seconds: 秒数
        :param getInt: 是否获取整数部分
        :return:
        """
        return seconds/H if not getInt else int(seconds/H)

    def h2s(self,hour:float,getInt=False):
        """
        小时转秒数
        :param hour: 小时数
        :param getInt: 是否获取整数部分
        :return:
        """

        return hour*60*60 if not getInt else int(hour*60*60)


    def s2d(self,seconds:int,getInt=False):
        """
        秒转天数
        :param seconds: 秒数
        :param getInt: 是否获取整数部分
        :return:
        """
        return seconds/D if not getInt else int(seconds/D)


    def d2s(self,days:float,getInt=False):
        """
        天数转秒数
        :param day: 天数
        :param getInt: 是否获取整数部分
        :return:
        """
        return days*24*60*60 if not getInt else int(days*24*60*60)


    def m2h(self,minutes:int,getInt=False):
        """
        分钟转小时
        :param minute:
        :param getInt: 是否获取整数部分
        :return:
        """
        return minutes/60 if not getInt else int(minutes/60)

    def h2m(self,hour:int,getInt=False):
        """
        小时转分钟
        :param hour: 小时数
        :param getInt: 是否获取整数部分
        :return:
        """

        return hour*60 if not getInt else int(hour*60)

    def m2d(self,minutes:int,getInt=False):
        """
        分钟转天数
        :param minute: 分钟数
        :param getInt: 是否获取整数部分
        :return:
        """
        return minutes/(60*24) if not getInt else int(minutes/(60*24))

    def d2m(self,days:int,getInt=False):
        """
        天数转分钟数
        :param day: 天数
        :param getInt: 是否获取整数部分
        :return:
        """

        return days*24*60 if not getInt else int(days*24*60)

    def h2d(self,hours:int,getInt=False):
        """
        小时转天数
        :param hour: 小时数
        :param getInt: 是否获取整数部分
        :return:
        """
        return hours/24 if not getInt else int(hours/24)


    def d2h(self,day:int,getInt=False):
        """
        天数转小时数
        :param day: 天数
        :param getInt: 是否获取整数部分
        :return:
        """

        return day*24 if not getInt else int(day*24)


    def h2ms(self,h:float):
        """
        小时转毫秒
        """

        return int(float(h)*3600*1000)

    def ms2h(self,ms:int):
        """
        毫秒转小时
        """
        int_h = ms//(3600*1000)
        left_ms = ms - self.h2ms(int_h) 

        return int_h,left_ms

    def ms2m(self,ms:int):
        """
        毫秒转分钟
        """

        int_m = ms//(60*1000)
        left_ms = ms - self.m2ms(int_m)

        return int_m,left_ms

    def m2ms(self,m:int):
        """
        分钟转毫秒
        """
        return int(float(m)*60*1000)


    def s2ms(self,s:int):
        """
        秒转毫秒
        """
    
        return int(float(s)*1000)
    
    def ms2s(self,ms:int):
        """
        毫秒转秒
        """
        int_s = int(ms)//1000
        left_ms = ms - self.s2ms(int_s)

        return int_s,left_ms

    def f2s(self,frame,fps,getInt=False):
        """
        帧数转秒
        """
        return frame/fps if not getInt else frame//fps

    def s2f(self,second,fps):
        """
        秒转帧数
        """
        return second * fps

    def srt2ms(self,srt:str):
        """
        字幕转毫秒
        srt: 字幕格式 "00:02:45,440"
        """
        hms,ms = srt.split(',')
        h,m,s = hms.split(':')

        all_ms = int(ms) + self.h2ms(h) + self.m2ms(m) + self.s2ms(s)

        return all_ms


    def ms2srt(self,ms:int):
        """
        毫秒转字幕格式
        """
        int_h,left_ms = self.ms2h(ms)
        int_m,left_ms = self.ms2m(left_ms)
        int_s,left_ms = self.ms2s(left_ms)

        return f"{int_h:02d}:{int_m:02d}:{int_s:02d},{left_ms:03d}"


    def srt_add(self,start_srt:str,ms:int):
        """
        字幕时间添加
        start_srt : "00:02:45,440"
        ms : 毫秒
        """
        srt_time = self.srt2ms(start_srt)
        ms = srt_time + ms

        return self.ms2srt(ms)


    def srt_sub(self,start_srt,ms):
        """
        字幕时间相减
        start_srt : "00:02:45,440"
        ms : 毫秒
        """
        srt_time = self.srt2ms(start_srt)
        ms = srt_time - ms

        return self.ms2srt(ms)


    def tc2f(self,timecode,fps):
        """
        时间码转帧数
        """
        h,m,s,f = timecode.split(':')
        alls = self.h2s(int(h)) + self.m2s(int(m)) + int(s)
        frames = alls * fps + int(f)
        return frames

    def f2tc(self,frames,fps):
        """
        帧数转时间码
        """
        s = int(frames/fps)
        left_f = frames - s*fps   # 剩余不足一秒的帧数
        dhms = self.DHMS(s)
        timecode = f'{dhms["hour"]:02d}:{dhms["minute"]:02d}:{dhms["second"]:02d}:{left_f:02d}'
        return timecode

    def tc_add_tc(self,start_timecode,timecode,fps):
        """
        时间码加时间码
        """
        start_frames = self.tc2f(start_timecode,fps)
        frames = self.tc2f(timecode,fps)
        all_frames = start_frames + frames
        timecode = self.f2tc(all_frames,fps)
        return timecode

    def tc_sub_tc(self,start_timecode,timecode,fps):
        """
        时间码减时间码
        """
        start_frames = self.tc2f(start_timecode,fps)
        frames = self.tc2f(timecode,fps)
        all_frames = start_frames - frames
        timecode = self.f2tc(all_frames,fps)
        return timecode

    def tc_add_f(self,start_timecode,frames,fps):
        """
        时间码加帧数
        """
        start_frames = self.tc2f(start_timecode,fps)
        all_frames = start_frames + int(frames)
        timecode = self.f2tc(all_frames,fps)
        return timecode

    def tc_sub_f(self,start_timecode,frames,fps):
        """
        时间码减帧数
        """
        start_frames = self.tc2f(start_timecode,fps)
        all_frames = start_frames - int(frames)
        timecode = self.f2tc(all_frames,fps)
        return timecode


    def tc_add_s(self,start_timecode,second,fps):
        """
        时间码加秒
        """
        start_frames = self.tc2f(start_timecode,fps)
        all_frames = start_frames + second * fps
        timecode = self.f2tc(all_frames,fps)
        return timecode

    def tc_sub_s(self,start_timecode,second,fps):
        """
        时间码减秒
        """
        start_frames = self.tc2f(start_timecode,fps)
        all_frames = start_frames - second * fps
        timecode = self.f2tc(all_frames,fps)
        return timecode

    def getSeconds(self,d=0,h=0,m=0):
        """
        将天，小时，分钟转成秒
        :return:
        """
        return d*24*60*60 + h*60*60 + m*60

    def DHMS(self,seconds:int):
        """
        将给定秒数，转成 多少天,多少小时，多少分钟，多少秒描述
        :param seconds: 秒数
        :return:
        """

        dhms = {}
        _day = 0
        int_day = 0
        int_hour = 0
        int_minute = 0
        left_second = 0
        day = seconds/D
        int_day = self.s2d(seconds, getInt=True)
        left_day = day-int_day
        hour = left_day*24
        int_hour = self.d2h(left_day,getInt=True)
        left_hour = hour - int_hour
        int_minute = self.h2m(left_hour,getInt=True)

        int_seconds = seconds -(int_day*D + int_hour*H + int_minute*M)
        if int_seconds == 60:
            int_minute += 1
            int_seconds = 0

        dhms['day'] = int_day
        dhms['hour'] = int_hour
        dhms['minute'] = int_minute
        dhms['second'] = int_seconds

        return dhms




    """

        *******************************************
            时间计算
        *******************************************

    """

    def CTS(self):
        """
        获取当前时间戳
        :return:
        """
        return time.time()

    def StrTime(self):
        """
        获取当前格式化日期
        :return:
        """

        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def deltaTime(self,start_str_time,end_str_time):
        """
        计算两字符串日期时间相差秒数
        :param start_str_time: '2021-07-18 17:19:44'
        :param end_str_time:   '2021-07-18 22:32:11'
        :return:
        """

        delta_s = self.strTime2TimeStamp(start_str_time) - self.strTime2TimeStamp(end_str_time)
        return delta_s


    def addTime(self,str_time,d:int=0,h:int=0,m:int=0,s:int=0):
        """
        格式化字符串时间加法计算
        :param str_time: 字符串格式日期时间
        :param d:  天数
        :param h:  小时
        :param m:  分钟
        :param s:  秒
        :return:
        """
        ts = self.strTime2TimeStamp(str_time)
        _add = d*24*60*60 + h*60*60 + m*60 +s
        new_ts = ts + _add

        return self.timeStamp2StrTime(new_ts)


    def subTime(self,str_time,d:int=0,h:int=0,m:int=0,s:int=0):
        """
        格式化字符串时间减法计算
        :param str_time: 字符串格式日期时间
        :param d:  天数
        :param h:  小时
        :param m:  分钟
        :param s:  秒
        :return:
        """
        ts = self.strTime2TimeStamp(str_time)
        _add = d*24*60*60 + h*60*60 + m*60 +s
        new_ts = ts - _add

        return self.timeStamp2StrTime(new_ts)




    """
    
        *******************************************
            周计算
        *******************************************
    
    """

    @cgai_time_args_tuple
    def getWeekdayNumber(self, int_year:int, int_month:int, int_day:int):
        """
        获取星期几
        注意：星期一为1，日期一一对应，星期日为7
        :return:
        """
        weekday = datetime.datetime(int_year, int_month, int_day).strftime("%w")
        if weekday == '0':
            return 7
        else:
            return int(weekday)

    @cgai_time_args_tuple
    def getWeekdayCName(self,int_year:int,int_month:int,int_day:int):
        """
        根据日期返回当前中文星期名称
        :param date:
        :return:
        """

        weekday_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
        num = int(datetime.datetime(int_year, int_month, int_day).strftime("%w"))
        return weekday_list[num]

    @cgai_time_args_tuple
    def isWeekend(self, int_year:int,int_month:int,int_day:int):
        """
        该函数用来判断给定日期是否为周末.
        :param date: 格式类似 2019-06-05
        :return:
        """
        weekday = self.getWeekdayNumber(int_year, int_month, int_day)
        if weekday == 7:
            return True
        else:
            return False

    def getCurrentWeekStartAndEnd(self):
        """
        返回该周的开始和结束时间
        """
        now = datetime.datetime.now()
        this_week_start = now - datetime.timedelta(days=now.weekday())
        this_week_end = now + datetime.timedelta(days=6 - now.weekday())

        return this_week_start.strftime("%Y-%m-%d"), this_week_end.strftime("%Y-%m-%d")

    def getLastWeekStartAndEnd(self):
        """
        获取上周起始与结束日期
        :return:
        """
        now = datetime.datetime.now()
        last_week_start = now - datetime.timedelta(days=now.weekday() + 7)
        last_week_end = now - datetime.timedelta(days=now.weekday() + 1)

        return last_week_start.strftime("%Y-%m-%d"), last_week_end.strftime("%Y-%m-%d")

    def getNextWeekStartAndEnd(self):
        """
        获取下周起始与结束日期
        :return:
        """
        now = datetime.datetime.now()
        next_week_start = now - datetime.timedelta(days=now.weekday() - 7)
        next_week_end = now - datetime.timedelta(days=now.weekday() - 13)
        return next_week_start.strftime("%Y-%m-%d"), next_week_end.strftime("%Y-%m-%d")


    @cgai_time_args_tuple
    def getWeekStartAndEnd(self,year:int,month:int,day:int):
        """
        传入指定日期，返回该日期所在周的起始日期与结束日期
        :param year:
        :param month:
        :param day:
        :return:
        """
        target_date = datetime.date(year,month,day)
        week_start = target_date - datetime.timedelta(days=target_date.weekday())
        week_end = target_date + datetime.timedelta(days=6 - target_date.weekday())

        return week_start.strftime("%Y-%m-%d"), week_end.strftime("%Y-%m-%d")

    @cgai_time_args_str
    def getWeekDates(self,date):
        """
        获取某日所在整周日期列表
        :param date:
        :return:
        """
        week_start,week_end = self.getWeekStartAndEnd(date)

        date_list = self.getDateList(week_start,week_end)
        return date_list





    """

        *******************************************
            月计算
        *******************************************

    """


    def isMonth31(self, month):
        """
        判定该月是否为31天
        :param month: 月份
        :return:
        """
        have31 = [1, 3, 5, 7, 8, 10, 12]

        if int(month) in have31:
            return True
        else:
            return False

    @cgai_time_args_strs
    def monthAdd(self, date,count):
        """
        给定日期与月数差值，返回该月数过后的日期
        :param year:
        :param month:
        :param day:
        :param count:
        :return:
        """
        year,month,day = self.strDate2TupleDate(date)
        new_month = month + count
        _y = (new_month - 1) // 12
        lm = new_month % 12
        lm = lm if lm != 0 else 12
        new_date = (year + _y, lm, day)
        new_date = self.tupleDate2StrDate(new_date)
        return new_date

    @cgai_time_args_strs
    def monthSub(self, date,count):
        """
        给定日期与月数差值，返回该月数过后的日期
        :param year:
        :param month:
        :param day:
        :param count:
        :return:
        """
        year,month,day = self.strDate2TupleDate(date)
        new_month = month - count
        _y = (new_month - 1) // 12
        lm = new_month % 12
        lm = lm if lm != 0 else 12
        new_date = (year + _y, lm, day)
        new_date = self.tupleDate2StrDate(new_date)
        return new_date

    def getMonthDayCount(self, int_year:int, int_month:int):
        """
        该函数获取给定月的所有日期数
        :param int_year:
        :param int_month:
        :return:
        """
        day31 = [1, 3, 5, 7, 8, 10, 12]
        if int_month == 2:
            if self.isLeapyear(int_year):  # 当是闰年时
                return 29
            else:
                return 28

        elif int_month in day31:
            return 31
        else:
            return 30


    def getCurrentMonthStartAndEnd(self):
        """
        计算本月起始与结束日期
        :return:
        """
        now = datetime.datetime.now()
        next_month = now.month + 1
        year = now.year

        if now.month == 12:
            next_month = 1


        if now.month + 2 >= 13:
            next_month = 1
            year += 1

        this_month_start = datetime.datetime(now.year, now.month, 1)
        this_month_end = datetime.datetime(year, next_month, 1) - datetime.timedelta(
            days=1) + datetime.timedelta(
            hours=23, minutes=59, seconds=59)

        return this_month_start.strftime("%Y-%m-%d"), this_month_end.strftime("%Y-%m-%d")

    def getLastMonthStartAndEnd(self):
        """
        计算上月起始与结束日期
        :return:
        """
        now = datetime.datetime.now()
        this_month_start = datetime.datetime(now.year, now.month, 1)
        last_month_end = this_month_start - datetime.timedelta(days=1) + datetime.timedelta(
            hours=23, minutes=59, seconds=59)
        last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)

        return last_month_start.strftime("%Y-%m-%d"), last_month_end.strftime("%Y-%m-%d")

    def getNextMonthStartAndEnd(self):
        """
        计算下月起始与结束日期
        :return:
        """
        now = datetime.datetime.now()
        next_month = now.month + 1
        year = now.year

        if now.month == 12:
            next_month = 1

        if now.month + 2 >= 13:
            next_month = 1
            year += 1

        next_month_start = datetime.datetime(year, next_month, 1)

        next_month_end = datetime.datetime(year, next_month+1, 1) - datetime.timedelta(
            days=1) + datetime.timedelta(
            hours=23, minutes=59, seconds=59)

        return next_month_start.strftime("%Y-%m-%d"), next_month_end.strftime("%Y-%m-%d")

    @cgai_time_args_tuple
    def getMonthStartAndEnd(self,int_year:int,int_month:int,int_day:int):
        """
        获取指定日期所在月份的起始与结束日期
        :param date:
        :return:
        """
        target_date = datetime.date(int_year,int_month,int_day)
        next_month = target_date.month + 1
        year = target_date.year

        if target_date.month == 12:
            next_month = 1


        if target_date.month + 2 >= 13:
            next_month = 1
            year += 1

        this_month_start = datetime.datetime(target_date.year, target_date.month, 1)
        this_month_end = datetime.datetime(year, next_month, 1) - datetime.timedelta(
            days=1) + datetime.timedelta(
            hours=23, minutes=59, seconds=59)

        return this_month_start.strftime("%Y-%m-%d"), this_month_end.strftime("%Y-%m-%d")


    def getLastMonth(self, month):
        '''
        给定month获取上一个月的month
        :param month:
        :return:
        '''
        if month == 1:
            return 12
        else:
            return month - 1

    def getNextMonth(self, int_month):
        '''
        获取给定月份下一个月分
        :param month:
        :return:
        '''
        if int_month == 12:
            return 1
        else:
            return int_month + 1

    """

        *******************************************
            季度计算
        *******************************************

    """
    @cgai_time_args_str
    def getQuarter(self,date):
        """
        获取指定日期所在季度信息
        return: tuple     eg: 1,[1,2,3]
        """
        quarter_map = {1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[10,11,12]}
        month = int(date.split('-')[1])
        index = qlist = None
        for i,q in quarter_map.items():
            if month in q:
                index = i
                qlist = q
                break
        return index,qlist

    @cgai_time_args_str
    def getQuarterStartDates(self,date):
        """
        获取指定日期所在的季度的各月起始日期
        return: []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        s_year,s_month,s_day = date.split('-')
        year = int(s_year)
        month = int(s_month)
        index,qlist = self.getQuarter(date)
        start_dates = []
        for m in qlist:
            start_date = f'{year}-{m:02d}-01'
            start_dates.append(start_date)
        return start_dates

    def getCurrentQuarterStartDates(self):
        """
        获取本季度的各月第一天
        return: []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        today = self.getToday()
        return self.getQuarterStartDates(today)

    def getLastQuarterStartDates(self):
        """
        获取上季度的各月第一天
        return: []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        start,_,_ = self.getCurrentQuarterStartDates()
        last_start = self.dateSub(start,1)
        return self.getQuarterStartDates(last_start)

    def getNextQuarterStartDates(self):
        """
        获取下季度的各月第一天
        return: []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        _,_,last = self.getCurrentQuarterStartDates()
        next_start = self.monthAdd(last,1)
        return self.getQuarterStartDates(next_start)

    @cgai_time_args_strs
    def quarterAdd(self,date,count):
        """
        季度相加
        date:  具体日期
        count: 相加的季度数
        return:  []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        start,_,end = self.getQuarterStartDates(date)
        next_start = self.monthAdd(start,count*3)
        return self.getQuarterStartDates(next_start)

    @cgai_time_args_strs
    def quarterSub(self,date,count):
        """
        季度相减
        date:  具体日期
        count: 相减的季度数
        return:  []  eg:['2023-01-01', '2023-02-01', '2023-03-01']
        """
        start,_,end = self.getQuarterStartDates(date)
        last_end = self.monthSub(end,count*3)
        return self.getQuarterStartDates(last_end)



    """

        *******************************************
            年计算
        *******************************************

    """


    def isLeapyear(self, year:int):
        """
        判定是否为闰年
        :param year:
        :return:
        """
        year = int(year)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0: # 整百年能被400整除的是闰年
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    def getYearDays(self,year:int):
        """
        获取指定年份的天数
        :param yea:
        :return:
        """
        return 366 if self.isLeapyear(year) else 365

    def getYearWeeks(self,year):
        """
        获取某一年的所有周
        :param year: 
        :return: list
        """
        year_start_date = f'{year}-01-01'
        year_end_date = f'{year}-12-31'
        weeks = self.acrossWeeks(year_start_date,year_end_date)
        return weeks

    @cgai_time_args_strs
    def getWeekNumberInYear(self,date):
        """
        获取该天在该年中所在第几周
        """
        week_num = None
        year = date.split('-')[0] 
        year_start_date = f'{year}-01-01'
        year_end_date = f'{year}-12-31'
        weeks = self.acrossWeeks(year_start_date,year_end_date)
        for i in range(len(weeks)):
            week = weeks[i]
            if date in week:
                week_num = i + 1
                break
        return week_num

    """

        *******************************************
            日计算
        *******************************************

    """

    def getToday(self):
        """
        获取今日日期 格式
        :return:
        """
        today = time.strftime("%Y-%m-%d")
        return today

    def getYesterday(self):
        """
        获取昨日日期
        :return:
        """
        yesterday = self.dateSub(self.getToday(),1)
        return yesterday

    def getTomorrow(self):
        """
        获取明天日期
        :return:
        """
        tomorrow = self.dateAdd(self.getToday(),1)
        return tomorrow

    @cgai_time_args_strs
    def dateAdd(self,start_date,days):
        """
        最正确的日期加法
        :param start_date:
        :param days:
        :return:
        """
        d = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        delta = datetime.timedelta(days=days)
        n_days = d + delta
        return (n_days.strftime('%Y-%m-%d'))


    @cgai_time_args_strs
    def dateSub(self,start_date,days):
        """
        最正确的日期加法
        :param start_date:
        :param days:
        :return:
        """
        d = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        delta = datetime.timedelta(days=days)
        n_days = d - delta
        return (n_days.strftime('%Y-%m-%d'))


    @cgai_time_args_strs
    def getDateList(self,start_date=None,end_date=None):
        """
        给定任意2个日期返回其中之间的所有日期
        :param start_date:
        :param end_date:
        :return:
        """
        date_list = []
        begin_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        return date_list


    @cgai_time_args_strs
    def deltaDays(self,start_date=None,end_date=None):
        """
        计算起始与结束日期长度
        :param start_date: 起始日期   '2021-05-15' 或 (2021,5,15)
        :param end_date:   结束日期   '2021-05-15' 或 (2021,5,15)
        :return:
        """
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        delta_day = (end - start).days
        return delta_day

    @cgai_time_args_strs
    def acrossYears(self,start_date=None,end_date=None):
        """
        获取给定前后日期之间所跨年
        :param start_date: 起始日期   '2021-05-15' 或 (2021,5,15)
        :param end_date:   结束日期   '2021-05-15' 或 (2021,5,15)
        :return:
        """
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        return [i for i in range(start.year,end.year+1)]

    @cgai_time_args_strs
    def acrossMonths(self,start_date=None,end_date=None):
        """
        获取给定前后日期之间所跨月份
        :param start_date:  起始日期   '2021-05-15' 或 (2021,5,15)
        :param end_date:    结束日期   '2021-05-15' 或 (2021,5,15)
        :return:
        """

        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        start_year = start.year
        end_year = end.year
        delta_year = end_year - start_year
        start_month = start.month
        end_month = end.month
        start_month_to_end_list = [s for s in range(start_month, 13)]
        end_month_to_start_list = [_e for _e in range(1, end_month + 1)]
        months = [m for m in range(1, 13)]
        cross_months = []
        if delta_year:
            if delta_year == 1:
                months.clear()
                delta_year += 1
            cross_months.extend(start_month_to_end_list)
            cross_months.extend((delta_year - 1) * months)
            cross_months.extend(end_month_to_start_list)
        else:
            cross_months = [m for m in range(start_month, end_month + 1)]

        return cross_months

    @cgai_time_args_strs
    def acrossWeeks(self,start_date=None,end_date=None):
        """
        获取指定前后日期所跨周
        :param start_date:
        :param end_date:
        :return:
        """
        weeks = []
        date_list = self.getDateList(start_date,end_date)
        week_start = self.getWeekDates(start_date)
        week_end = self.getWeekDates(end_date)
        if week_start != week_end:
            conect_start_end = week_start+week_end
            for date in conect_start_end:
                if date in date_list:
                    date_list.remove(date)
            cliped_data_list = clip_list(date_list, 7)

            weeks.append(week_start)
            if cliped_data_list!=[[]]:
                weeks.extend(cliped_data_list)
            weeks.append(week_end)
        else:
            weeks = [week_start]
        return weeks


    @cgai_time_args_strs
    def getStartDateAcrossMonths(self,start_date=None, end_date=None):
        """
        获取指定日期范围内所有月份的第一天
        
        Args:
            start_date: 起始日期，格式为'YYYY-MM-DD'
            end_date: 结束日期，格式为'YYYY-MM-DD'
        
        Returns:
            包含所有月份第一天的日期列表
        """
        # 将输入字符串转换为datetime对象
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        
        # 获取开始月份的第一天
        current = start.replace(day=1)
        
        # 获取结束月份的第一天
        end = end.replace(day=1)
        
        result = []
        
        # 循环直到超过结束月份
        while current <= end:
            result.append(current.date().strftime('%Y-%m-%d'))
            # 添加一个月
            current += relativedelta(months=1)
        
        return result




    @cgai_time_args_strs
    def getDatesByNumber(self,start_date=None,end_date=None,number=0):
        """
        获取前后日期之间为星期几的日期
        :param start_date:
        :param end_date:
        :param number:
        :return:
        """
        days = []
        date_list = self.getDateList(start_date,end_date)
        for i in date_list:
            if self.getWeekdayNumber(i) == number:
                days.append(i)

        return days


    @cgai_time_args_strs
    def getMondays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期一的日期
        :param start_date: 起始日期
        :param end_date:   结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,1)

    @cgai_time_args_strs
    def getTuesdays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期二的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,2)

    @cgai_time_args_strs
    def getWednesdays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期三的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,3)

    @cgai_time_args_strs
    def getThursdays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期四的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,4)

    @cgai_time_args_strs
    def getFridays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期五的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,5)

    @cgai_time_args_strs
    def getSaturdays(self,start_date=None,end_date=None):
        """
        获取前后日期之间为星期六的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,6)

    @cgai_time_args_strs
    def getSundays(self,start_date,end_date):
        """
        获取前后日期之间为星期天的日期
        :param start_date:  起始日期
        :param end_date:    结束日期
        :return:
        """

        return self.getDatesByNumber(start_date,end_date,7)

    @cgai_time_args_tuple
    def isMonday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期一
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 1 else False


    @cgai_time_args_tuple
    def isTuesday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期二
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 2 else False


    @cgai_time_args_tuple
    def isWednesday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期三
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 3 else False


    @cgai_time_args_tuple
    def isThursday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期四
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 4 else False

    @cgai_time_args_tuple
    def isFriday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期五
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 5 else False

    @cgai_time_args_tuple
    def isSaturday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期一
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 6 else False

    @cgai_time_args_tuple
    def isSunday(self,int_year:int, int_month:int, int_day:int):
        """
        是否为星期一
        :param date:
        :return:
        """

        return True if self.getWeekdayNumber(int_year,int_month,int_day) == 7 else False


    def getLastMonthDay(self, year, month):
        month31 = [1, 3, 5, 7, 8, 10, 12]
        if month == 3:  # 主要判断给定月是不是3月即可知道上月是不是2月
            # 当是3月时，则要判定是不是闰年
            if self.isLeapyear(year):  # 当是闰年时
                return 29

            else:
                return 28

        else:  # 不是三月的话，那么判定该月的上一月是不是31天即可
            if month in month31:  # 在上月是2月排除的情况下，如果给定月是属于31天组，那么上月就只能是30天
                return 31

            else:
                return 30



    def str2int(self, str_day):
        '''
        将当前日数转成整数,eg: str 05 => int 5
        :param day:
        :return:
        '''
        if str_day.startswith('0'):
            return int(str_day[1:])
        else:
            return int(str_day)

    def int2str(self, day):
        '''
        如果day小于10，则返回加0字符串
        :param day:
        :return:
        '''
        if day < 10:
            return '0' + str(day)
        else:
            return str(day)


    def getMonthDateList(self,int_year=None,int_month=None,date=None):
        """
        给定年份与月份，返回当前月份里的所有日期
        注意：当给定date后将以date作为具体输入而无视int_year和int_month
        :param int_year:  年份
        :param int_month: 月份
        :param date:  具体日期
        :return:
        """
        year = int_year
        month = int_month
        if isinstance(date,str):
            year,month,_day = self.strDate2TupleDate(date)
        elif isinstance(date,tuple):
            year,month,_day = date
        month_all_day_list = []
        month_count = self.getMonthDayCount(year, month)  # 返回当前月数
        format_month = self.int2str(month)
        for i in range(1, month_count + 1):
            format_i = self.int2str(i)
            day = '{}-{}-{}'.format(year, format_month, format_i)
            month_all_day_list.append(day)

        return month_all_day_list




    def getMonthWeeks(self, int_year=None, int_month=None,date=None):
        """
        给定年与月，或者直接给一个具体日期date,返回该月所占周
        注意：当给定date后将以date作为具体输入而无视int_year和int_month
        :param int_year:  年份
        :param int_month: 月份
        :param date:  具体日期
        :return:
        """

        month_dates = self.getMonthDateList(int_year, int_month,date)

        weeks_list = []
        for i in month_dates:
            if self.isWeekend(i):
                weeklist = self.getWeekDates(i)
                weeks_list.append(weeklist)
        
        return weeks_list


    #########下面实现date日期，日增减，周增减，月增减




