# h-rm_tan 25Aug2016

filepath = '~/dsp/python/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''
    
    

'''
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
''' 

#==============================================================================
# PANDAS opt
#==============================================================================

import pandas as pd

fball = pd.read_csv(filepath + 'football.csv') 

'''
>>> fball.head(10)
                Team  Games  Wins  Losses  Draws  Goals  Goals Allowed  Points
                                                [scored]         [lost]
0            Arsenal     38    26       9      3     79             36      87
1          Liverpool     38    24       8      6     67             30      80
2  Manchester United     38    24       5      9     87             45      77
3          Newcastle     38    21       8      9     74             52      71
4              Leeds     38    18      12      8     53             37      66
5            Chelsea     38    17      13      8     66             38      64
6           West_Ham     38    15       8     15     48             57      53
7        Aston_Villa     38    12      14     12     46             47      50
8          Tottenham     38    14       8     16     49             53      50
9          Blackburn     38    12      10     16     55             51      46

ref http://stackoverflow.com/questions/15006298/how-to-preview-a-part-of-a-large-pandas-dataframe

>>> fball.shape
(20, 8)

'''

# colN = list(fball.columns)
# abs(fball[['Goals','Goals Allowed']].diff(-1,1)).idxmin(skipna=True)

absDiff = abs(fball['Goals']-fball['Goals Allowed'])
#minDiff_info = fball.iloc[absDiff.idxmin()]
minDiffTeam = fball['Team'].iloc[absDiff.idxmin()]

print( 'Team with least for vs. against goal difference is : {}' .format(minDiffTeam) )


#==============================================================================
# non-PANDAS opt 

#** http://stackoverflow.com/questions/7657457/finding-key-from-value-in-python-dictionary
#==============================================================================

import csv

with open(filepath + 'football.csv', "r") as f:
    fbD = csv.DictReader(f)
    
    absDiffD = {} #as dictionary   
    for row in fbD:
        absDiffD[row['Team']] = abs(int(row['Goals']) - int(row['Goals Allowed']))

#minDiffTeam = min(absDiffD.items())

minDiffTeamName = [key for key, value in absDiffD.items() if value == min(absDiffD.values()) ][0]

print ('Team with least for vs. against goal difference is : {}'  .format(minDiffTeamName) )



#==============================================================================
# non-PANDAS read cvs opt 2

# ref http://stackoverflow.com/questions/14365542/read-csv-file-and-return-data-frame-in-python
# ref https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files
# http://opentechschool.github.io/python-data-intro/core/csv.html
#==============================================================================

import csv, pandas as pd

with open(filepath + 'football.csv', "r") as f:
    #    reader=csv.reader(f,delimiter=',')    
    reader = csv.reader(f)
    headers = next(reader)
    column = {h:[] for h in headers}
    #    data=[]
    for row in reader:
        #   data.append(row) ## this creates a list of lists...
        for c, r in zip(headers, row):
            column[c].append(r)
   

T = column['Team']
G = list(map(int, column['Goals']))
GA = list(map(int, column['Goals Allowed']))
diff = abs(pd.DataFrame(G)-pd.DataFrame(GA))    

print( 'Team with least for vs. against goal difference is : {}' .format(T[diff.idxmin()[0]]) )
 
