#You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)

#! /usr/bin/env python

time_now = 1400
hoursset = 5100

days_gone_bye = (1400+5100)//2400
time_alarm_will_go_off = (1400+5100)%2400


print(days_gone_bye, "days would have gone by...")
print("alarm would have gone off at", time_alarm_will_go_off, "hrs.")