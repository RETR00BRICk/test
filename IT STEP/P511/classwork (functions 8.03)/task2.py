def is_leap_year(year : int):
    return year%4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    if month in [4,6,9,11]: #квітень, червень, вересень, листопад
        return 30
    elif month == 2: #любий
        return 29 if is_leap_year(year) else 28 #січень, березень, липень, серпень, жовтень, грудень
    else:
        return 31

def days_diff(d1, m1, y1, d2, m2, y2):
    if(y1,m1,d1) > (y2,m2,d2):
        return days_diff(d2, m2, y2, d1, m1, y1)