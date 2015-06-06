'''
12.11.1
'''

import calendar

print("The year 2014 in _SANE_VIEW_")
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2014)                   # What happens here?
print("The year 2014 in _ADVENTUROUS_VIEW_")
cal_startfrom_thursday = calendar.TextCalendar(firstweekday=3)
cal_startfrom_thursday.pryear(2014)


d = calendar.LocaleTextCalendar(6, "ja_JP")
d.pryear(2012)

for i in range(2000, 2015):
    isleapyearornot = calendar.isleap(i)
    print(isleapyearornot)