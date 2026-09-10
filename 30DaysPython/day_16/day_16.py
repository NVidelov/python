# Day 16 - 30 Days of Python Challenge
from datetime import datetime, date

# 1
now = datetime.now()
timestamp = now.timestamp()

# 2
t = now.strftime("%d/%m/%Y, %H:%M:%S")
print(t)

# 3
date_string = "5 December, 2019"
time = datetime.strptime(date_string, "%d %B, %Y")
print(time)

# 4
now = datetime.now()
today = date(year=now.year, month=now.month, day=now.day)
new_year = date(year=2027, month=1, day=1)
time_to_ny = new_year - today
print(time_to_ny)

# 5
now = datetime.now()
today = date(year=now.year, month=now.month, day=now.day)
date_string = "1 January 1970"
time = datetime.strptime(date_string, "%d %B %Y")
old_date = date(year=time.year, month=time.month, day=time.day)
print(today - old_date)