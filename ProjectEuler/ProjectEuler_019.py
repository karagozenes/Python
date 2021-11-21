import datetime

start_date = datetime.date(1901,1,1)
end_date = datetime.date(2000,12,31)

tdelta = datetime.timedelta(days=0)
sundays = 0
for i in range(36525):
    current = start_date + tdelta
    if current.weekday() == 6 and int(current.strftime("%d")) == 1:
        sundays += 1
    tdelta += datetime.timedelta(days=1)
print(sundays)