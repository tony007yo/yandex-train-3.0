time_serv_beg = input()
time_user = input()
time_serv_end = input()
day_secs = 86400

def time_to_sec(time):
    hour, minutes, secs = map(int, time.split(":"))
    minutes = minutes + hour * 60
    return secs + minutes * 60

def sec_to_time(secs):
    sec = secs % 60
    minutes = secs // 60
    minute = minutes % 60
    hours = minutes // 60
    hour = hours % 24
    return f"{hour:02d}:{minute:02d}:{sec:02d}"

sec_serv_beg = time_to_sec(time_serv_beg)
sec_serv_end = time_to_sec(time_serv_end)
if sec_serv_end < sec_serv_beg:
    sec_serv_end += day_secs
sec_user = time_to_sec(time_user) + (sec_serv_end - sec_serv_beg) / 2
print(sec_to_time(round(sec_user+0.1)))