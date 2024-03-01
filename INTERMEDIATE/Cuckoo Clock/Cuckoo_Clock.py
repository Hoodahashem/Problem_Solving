from datetime import datetime, timedelta
import time
dic={
    "01":1,
    "02":2,
    "03":3,
    "04":4,
    "05":5,
    "06":6,
    "07":7,
    "08":8,
    "09":9,
    "10":10,
    "11":11,
    "12":12
}
def cuckoo_clock(initial_time, n):
    compo = initial_time.split(":")
    hours = int(compo[0])
    mins = int(compo[1])
    sec = (hours * 3600) + (mins * 60)
    chimes = 0
    while chimes < n:
        clock = time.strftime("%I:%M", time.gmtime(sec))
        if clock[-2:] == "00":
            chimes += dic.get(clock[:2])
        if clock[-2:] == "15":
            chimes += 1
        if clock[-2:] == "30":
            chimes += 1
        if clock[-2:] == "45":
            chimes += 1
        sec += 60
    return clock

print(cuckoo_clock("08:17",200)) # 05:45
