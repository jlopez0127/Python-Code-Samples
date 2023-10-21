str_time = int(input("What time is it now?"))
str_wait_time = int(input("What is the number of hours you haveto wait?"))
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + str_wait_time
print( "Your alarm will go off at: " + time_when_alarm_go_off)
