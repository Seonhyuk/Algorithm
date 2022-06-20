from datetime import datetime

year = datetime.today().year
month = datetime.today().month

days = {1, 3, 5, 7, 8, 10, 12}

if month == 2:
    day = 28
    if not year % 4 and year % 100 or not year % 400:
        day = 29
elif month in days:
    day = 31
else:
    day = 30

print(day, 'days for', year, '-', month)