import time
#returns a time tuple
print(time.localtime(time.time()))
import time;
##returns the formatted time 
print(time.asctime(time.localtime(time.time())))

###python sleep time
import time;
for i in range(0,10):
  print(i)
  ##each element will be printed after 1 second
  time.sleep(1)
  
  ###date time module 
  import datetime
  ##returns the currrent datetime object 
  print(datetime.datetime.now())
  
  ###creating date objects
  import datetime
  ##returns the datetime object for the specified date
  print(datetime.datetime(2023,16,05))
  
  
  ###comparison of two dates
  from datetime import datetime as dt
  ####compares the time .if the time is in between 8PM AND 4pm then it prints working hours otherwis it prints fun hours 
  if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()    <dt(dt.now().year,dt.now().month,dt.now().day,16):
       print("working hours")
  else:
    print("fun hours")
    
    
    ####calendar module comment and code
    import calendar;
    cal=calendar.month(2023,3)
    ###printing the calendar of December 2023
    print(cal)
    
    ####printing the calendr  of the whole year 
    ##we use prcal() to print calendar of the whole year
    import calendar
    ###printing calendar of the year 2023
    s = calendar.prcal(2023)