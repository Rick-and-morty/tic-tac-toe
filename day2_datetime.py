
import datetime  # its ok to import like this

# 3-1-2015
day = datetime.datetime(year=2004, month=3, day=1)
print(day - datetime.timedelta(hours=12))
now = datetime.datetime.now()
print(now.day)
now_formatted = now.strftime("%A, %B %d %Y %H:%M:%S")
print(now_formatted)

now_obj = (datetime.strptime(now_formatted, "%A, %B %d %Y %H:%M:%S"))
print(type(now_obj))
print(now_obj)
