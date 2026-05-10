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
    
    if y1 == y2 and m1 == m2:
        return d2 - d1
    
    if d1 == 1 and m1 == 1 and y1 < y2:
        days_in_curr_year = 366 if is_leap_year(y1) else 365
        return days_diff(d1, m1, y1 + 1, d2, m2, y2) + days_in_curr_year
    
    days_left_in_month = get_days_in_month(m1, y1) - d1
    next_m = m1 + 1
    next_y = y1
    if next_m > 12:
        next_m = 1
        next_y += 1
    
    return days_left_in_month + 1 + days_diff(1, mext_m, next_y, d2, m2, y2)

print(days_diff(10, 3, 2026, 29, 3, 2026))