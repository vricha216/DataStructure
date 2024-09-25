# You are building a logic for a clock that requires you convert absolute time in minutes into a format
# supported by a digital clock. See examples below.
# 125 minutes can be displayed as 2:05
# 155 minutes can be displayed as 2:35
# (You can assume the maximum value of minutes will be less than 24 X 60)


def convert(mins: str):
    h = int(s)//60
    m = int(s)%60
    ms = f"0{m}" if m < 10 else str(m)
    time_str = str(h)+':'+str(ms)
    return time_str



s = '125'
print(convert(s))