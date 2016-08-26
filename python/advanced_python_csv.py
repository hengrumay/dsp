# h-rm_tan 26Aug2016

## REFs
# https://pythonprogramming.net/python-pandas-data-analysis/
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
# http://chrisalbon.com/python/pandas_saving_dataframe_as_csv.html


'''
---

###Part II - Write to CSV File


####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```
'''


filepath = '/Users/hrm/Documents/Dropbox/DSrelated/GIThub/dsp/python/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''



## PLACE YOUR CODE HERE


### LOAD Libraries & DATA

import pandas as pd

faculty = pd.read_csv(filepath + 'faculty.csv')

# Retrieve from DF and save panda DF as CSV
F_email = faculty[' email']

F_email.to_csv('Faculty_email.csv', index=False)



### Alternatively using csv

import csv

# open and read list of emails
with open (filepath + 'faculty.csv') as f:
    emails = []
    facultyD = csv.DictReader(f)
    for row in facultyD:
        emails.append(row[' email'])

# write emails to new csv
with open ('F_emails.csv', 'w') as csvF:
	csvWriter = csv.writer(csvF)
	for e in emails:
		csvWriter.writerow([e])
	csvF.close()

