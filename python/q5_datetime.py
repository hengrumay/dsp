# h-rm_tan 24Aug2016

''' 
Q5. Datetime

Use Python to compute days between start and stop date.

## Ref 
## https://pymotw.com/2/datetime/
## http://www.tutorialspoint.com/python/time_strptime.htm
## https://blogs.harvard.edu/rprasad/2011/09/21/python-string-to-a-datetime-object/
## http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior

'''

#import time
from datetime import datetime as dt  # datetime.datetime.strptime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

DStart = dt.strptime(date_start, '%m-%d-%Y')
DStop = dt.strptime(date_stop, '%m-%d-%Y')
DStop - DStart 
# datetime.timedelta(937)

####b)  
date_start2 = '12312013'  
date_stop2 = '05282015'  

DStart2 = dt.strptime(date_start2, '%m%d%Y')
DStop2 = dt.strptime(date_stop2, '%m%d%Y')
DStop2 - DStart2 
# datetime.timedelta(513)



####c)  
date_start3 = '15-Jan-1994'  
date_stop3 = '14-Jul-2015'  

DStart3 = dt.strptime(date_start3, '%d-%b-%Y')
DStop3 = dt.strptime(date_stop3, '%d-%b-%Y')
DStop3 - DStart3
# datetime.timedelta(7850)