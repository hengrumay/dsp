# h-rm_tan 25Aug2016

#==============================================================================
# ## REFs
#==============================================================================
# https://www.shortcutfoo.com/app/dojos/python-regex/cheatsheet
# http://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://docs.python.org/3/howto/regex.html
# https://wiki.python.org/moin/RegularExpression
# https://pymotw.com/2/re/
## https://github.com/pydata/pandas/issues/2905
## http://stackoverflow.com/questions/15411158/pandas-countdistinct-equivalent

## USED Refs
# http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
## https://www.reddit.com/r/Python/comments/3tipqq/is_there_a_pandasonly_way_to_do_this_count_unique/

#==============================================================================
# '''
# ---
#
# The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)
#
# This data is available in this file:  [faculty.csv](python/faculty.csv)
#
# ---
# ###Part I - Regular Expressions
# ---
# '''
#==============================================================================

filepath = '~/dsp/python/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''



## PLACE YOUR CODE HERE


#==============================================================================
# ### LOAD Libraries & DATA
#==============================================================================

import pandas as pd
import itertools
# import re

faculty = pd.read_csv(filepath + 'faculty.csv')

# faculty.columns
# Index(['name', ' degree', ' title', ' email'], dtype='object')


#==============================================================================
# ####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
#==============================================================================

Fdeg = faculty[' degree']
# Fdeg.unique()

# 1 Remove spaces at the beginning of each row of strings &
# 2 remove periods(.)
Fdeg1 = [s.strip().replace('.', '') for s in Fdeg]

# 3 Split rows|strings with multiple degrees into separate strings:
Fdeg2 = [s.split() for s in Fdeg1]

# 4 combine lists and sublists into a single list --> dataframe array:
merged = pd.DataFrame(list(itertools.chain(*Fdeg2)), columns = ['Fdeg'])  # cols default to np.index e.g. [0]

'''
>>> merged['Fdeg'].nunique()
8
'''
# uniqueFdeg = merged['Fdeg'].unique()
'''
>>> list(merged['Fdeg'].unique())
['ScD', 'PhD', 'MD', 'MPH', 'BSEd', 'MS', 'JD', 'MA']
'''

DegreeFreq = merged.groupby(['Fdeg']).size()
'''
>>> merged.groupby(['Fdeg']).size()
Fdeg
BSEd     1
JD       1
MA       1
MD       1
MPH      2
MS       2
PhD     32
ScD      6
dtype: int64
'''


#==============================================================================
# ####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor
#==============================================================================

Ftitle = faculty[' title']

## 1st check:
'''
>>> Ftitle.nunique()
4
>>> Ftitle.unique()
array(['Associate Professor of Biostatistics',
       'Professor of Biostatistics',
       'Assistant Professor of Biostatistics',
       'Assistant Professor is Biostatistics'], dtype=object)
'''
## Seems to be a "typo"... ' of ' --> ' is '
Ft_tidy = pd.DataFrame([s.replace(' is ', ' of ') for s in Ftitle], columns=['title']) #[0]

'''
>>> Ft_tidy['title'].unique()
array(['Associate Professor of Biostatistics',
       'Professor of Biostatistics',
       'Assistant Professor of Biostatistics'], dtype=object)
'''
TitleFreq = Ft_tidy.groupby(['title']).size()
'''
>>> Ft_tidy.groupby(['title']).size()
title
Assistant Professor of Biostatistics    12
Associate Professor of Biostatistics    12
Professor of Biostatistics              13
dtype: int64
'''


#==============================================================================
# ####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
#==============================================================================


F_email = faculty[' email']


'''
>>> print(F_email)
0     bellamys@mail.med.upenn.edu
1                warren@upenn.edu
2               bryanma@upenn.edu
3              jinboche@upenn.edu
4              sellenbe@upenn.edu
5     jellenbe@mail.med.upenn.edu
6               ruifeng@upenn.edu
7     bcfrench@mail.med.upenn.edu
8              pgimotty@upenn.edu
9         wguo@mail.med.upenn.edu
10        hsu9@mail.med.upenn.edu
11       rhubb@mail.med.upenn.edu
12      whwang@mail.med.upenn.edu
13      mjoffe@mail.med.upenn.edu
14    jrlandis@mail.med.upenn.edu
15            liy3@email.chop.edu
16     mingyao@mail.med.upenn.edu
17              hongzhe@upenn.edu
18             rlocalio@upenn.edu
19    nanditam@mail.med.upenn.edu
20    knashawn@mail.med.upenn.edu
21     propert@mail.med.upenn.edu
22       mputt@mail.med.upenn.edu
23             sratclif@upenn.edu
24             michross@upenn.edu
25       jaroy@mail.med.upenn.edu
26     msammel@cceb.med.upenn.edu
27                shawp@upenn.edu
28        rshi@mail.med.upenn.edu
29       hshou@mail.med.upenn.edu
30     jshults@mail.med.upenn.edu
31    alisaste@mail.med.upenn.edu
32     atroxel@mail.med.upenn.edu
33       rxiao@mail.med.upenn.edu
34        sxie@mail.med.upenn.edu
35                 dxie@upenn.edu
36     weiyang@mail.med.upenn.edu
Name:  email, dtype: object


>>> print(list(F_email))
['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']


'''



#==============================================================================
# ####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
#==============================================================================

'''
>>> F_email[0].split()
['bellamys@mail.med.upenn.edu']
>>> F_email[0].split('@')
['bellamys', 'mail.med.upenn.edu']
>>> F_email[0].split('@')[1]
'mail.med.upenn.edu'

'''

Unique_EmailServers =set([e.split('@')[1] for e in F_email])
# equivalent to {e.split('@')[1] for e in F_email}

'''
>>> set([e.split('@')[1] for e in F_email])
{'mail.med.upenn.edu', 'cceb.med.upenn.edu', 'upenn.edu', 'email.chop.edu'}

'''

