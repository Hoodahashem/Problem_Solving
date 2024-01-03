from datetime import datetime, timedelta

def cuckoo_clock(initial_time, n):
    time = datetime.strptime(initial_time, "%I:%M")
    chimes = 0

    while chimes < n:
        if time.minute in [15, 30, 45]:
            chimes += 1
        if time.minute == 0:
            if time.hour == 12:
                chimes += 12
            else:
                chimes += time.hour % 12
        time = time + timedelta(minutes=1)
    time = time - timedelta(minutes=1)

    return time.strftime("%I:%M")

print(cuckoo_clock("08:17", 200))
