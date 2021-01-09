from datetime import datetime, timedelta, timezone 
JST = timezone(timedelta(hours=+9))
print(JST)

print(datetime.now())


def calculate_age():
    now = datetime.now()
    year = int(input('Enter year'))
    months = int(input('Enter months '))
    day = int(input('Enter days '))
    then = datetime(year=year , month=months , days= day)
    return (now - then)

print(dir(datetime.day()))