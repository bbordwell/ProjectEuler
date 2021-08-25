from itertools import cycle

#This program solves Project Euler #19
months = cycle([31,28,31,30,31,30,31,31,30,31,30,31])
daysElapsed = 0
monthsElapsed = 0
ans = 0
year = 1901

for month in months:
    if year >= 2001:
        break       #End the loop once we get to 2001
    if month == 28: #If Feb, check for a leap year
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 == 0):
            month += 1        
    if daysElapsed % 7 == 5: #1901 starts on a Tuesday so 5 days after is sunday
        ans += 1
    daysElapsed += month
    monthsElapsed += 1
    if monthsElapsed % 12 == 0:
        year += 1
    
print(ans)
        
        

