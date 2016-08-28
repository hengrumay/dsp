# h-rm_tan 26/28Aug2016

## REFs
# http://www.mysamplecode.com/2013/05/python-read-csv-file-list-dictionary.html
# http://stackoverflow.com/questions/18695605/python-pandas-dataframe-to-dictionary

### http://stackoverflow.com/questions/26716616/convert-pandas-dataframe-to-dictionary
# http://chrisalbon.com/python/pandas_dropping_column_and_rows.html
### http://chrisalbon.com/python/pandas_indexing_selecting.html
# http://stackoverflow.com/questions/30250715/how-do-you-get-the-first-3-elements-in-python-ordereddict

# http://www.python-course.eu/python3_dictionaries.php
# http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
# http://www.python-course.eu/dictionaries.php

'''
---

### Part III - Dictionary


Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

---
'''


filepath = '~/dsp/python/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''


#PLACE YOUR CODE HERE

import pandas as pd

faculty = pd.read_csv(filepath + 'faculty.csv')

#faculty.columns
#>>> Index(['name', ' degree', ' title', ' email'], dtype='object')

## TIDY pd DF:

#Fn_tmp = faculty['name']
#Fname = pd.DataFrame([s.split(' ')[-1] for s in faculty['name']], columns = ['first','middle','last']) #[0]1st & [2]last names
### Rectify  No Last names due to MISSING/NO 'middle' names
#NoLastIDX = Fname.loc[Fname['last'].isnull()]
#Fname.loc[Fname['last'].isnull(),'last'] = Fname.loc[Fname['last'].isnull(),'middle']
#Fname.loc[NoLastIDX.index,'middle'] = NoLastIDX['last']
##Fname.loc[NoLastIDX.index]
#
FnameF = pd.DataFrame([s.split(' ')[0] for s in faculty['name']], columns = ['first'])
FnameL = pd.DataFrame([s.split(' ')[-1] for s in faculty['name']], columns = ['last'])


#Fd_tmp = faculty[' degree']
Fdegree = pd.DataFrame([s.strip() for s in faculty[' degree']], columns = ['Degree'])

#Ft_tmp = faculty[' title']
Ft_tmp = [s.replace(' is ', ' of ') for s in faculty[' title']]
Ftitle = pd.DataFrame([ft.split(' of ')[0] for ft in Ft_tmp], columns = ['Title'])


faculty = faculty.join([FnameF, FnameL, Fdegree, Ftitle])


#==============================================================================
# ####Q6.  Create a dictionary in the below format:
# ```
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#               'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# ```
# Print the first 3 key and value pairs of the dictionary:
#
#==============================================================================


DF1 = faculty[['last', 'Degree', 'Title', ' email']]

faculty_dict = DF1.set_index('last').T.to_dict('list')

print (list(faculty_dict.items())[:3] )
'''
[('Ellenberg', ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']), ('Bilker', ['Ph.D.', 'Professor', 'warren@upenn.edu']), ('Ross', ['PhD', 'Assistant Professor', 'michross@upenn.edu'])]
'''

#==============================================================================
# ####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
#
# ```
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
# ```
#
# Print the first 3 key and value pairs of the dictionary:
#==============================================================================

DF2 = faculty[['first', 'last', 'Degree', 'Title', ' email']]

professor_dict = DF2.set_index(['first','last']).T.to_dict('list')

print (list(professor_dict.items())[:3] )
'''
[(('Jonas', 'Ellenberg'), ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']), (('Yimei', 'Li'), ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']), (('Pamela', 'Shaw'), ['PhD', 'Assistant Professor', 'shawp@upenn.edu'])]

'''


#==============================================================================
# ####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
#
#==============================================================================


sortKeysbyLastName = sorted(professor_dict, key=lambda name:name[-1])
#sortValsbyLastName = [professor_dict[sortKeysbyLastName[k]] for k in range(len(sortKeysbyLastName))]

for k in sortKeysbyLastName:
    print(k, list(professor_dict[k]) )

'''
('Scarlett', 'Bellamy') ['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker') ['Ph.D.', 'Professor', 'warren@upenn.edu']
('Matthew', 'Bryan') ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']
('Jinbo', 'Chen') ['Ph.D.', 'Associate Professor', 'jinboche@upenn.edu']
('Jonas', 'Ellenberg') ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
('Susan', 'Ellenberg') ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
('Rui', 'Feng') ['Ph.D', 'Assistant Professor', 'ruifeng@upenn.edu']
('Benjamin', 'French') ['PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu']
('Phyllis', 'Gimotty') ['Ph.D', 'Professor', 'pgimotty@upenn.edu']
('Wensheng', 'Guo') ['Ph.D', 'Professor', 'wguo@mail.med.upenn.edu']
('Yenchih', 'Hsu') ['Ph.D.', 'Assistant Professor', 'hsu9@mail.med.upenn.edu']
('Rebecca', 'Hubbard') ['PhD', 'Associate Professor', 'rhubb@mail.med.upenn.edu']
('Wei-Ting', 'Hwang') ['Ph.D.', 'Associate Professor', 'whwang@mail.med.upenn.edu']
('Marshall', 'Joffe') ['MD MPH Ph.D', 'Professor', 'mjoffe@mail.med.upenn.edu']
('J.', 'Landis') ['B.S.Ed. M.S. Ph.D.', 'Professor', 'jrlandis@mail.med.upenn.edu']
('Yimei', 'Li') ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
('Hongzhe', 'Li') ['Ph.D', 'Professor', 'hongzhe@upenn.edu']
('Mingyao', 'Li') ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
('A.', 'Localio') ['JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu']
('Nandita', 'Mitra') ['Ph.D.', 'Associate Professor', 'nanditam@mail.med.upenn.edu']
('Knashawn', 'Morales') ['Sc.D.', 'Associate Professor', 'knashawn@mail.med.upenn.edu']
('Kathleen', 'Propert') ['Sc.D.', 'Professor', 'propert@mail.med.upenn.edu']
('Mary', 'Putt') ['PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu']
('Sarah', 'Ratcliffe') ['Ph.D.', 'Associate Professor', 'sratclif@upenn.edu']
('Michelle', 'Ross') ['PhD', 'Assistant Professor', 'michross@upenn.edu']
('Jason', 'Roy') ['Ph.D.', 'Associate Professor', 'jaroy@mail.med.upenn.edu']
('Mary', 'Sammel') ['Sc.D.', 'Professor', 'msammel@cceb.med.upenn.edu']
('Pamela', 'Shaw') ['PhD', 'Assistant Professor', 'shawp@upenn.edu']
('Russell', 'Shinohara') ['Ph.D.', 'Assistant Professor', 'rshi@mail.med.upenn.edu']
('Haochang', 'Shou') ['Ph.D.', 'Assistant Professor', 'hshou@mail.med.upenn.edu']
('Justine', 'Shults') ['Ph.D.', 'Professor', 'jshults@mail.med.upenn.edu']
('Alisa', 'Stephens') ['Ph.D.', 'Assistant Professor', 'alisaste@mail.med.upenn.edu']
('Andrea', 'Troxel') ['ScD', 'Professor', 'atroxel@mail.med.upenn.edu']
('Rui', 'Xiao') ['PhD', 'Assistant Professor', 'rxiao@mail.med.upenn.edu']
('Dawei', 'Xie') ['PhD', 'Assistant Professor', 'dxie@upenn.edu']
('Sharon', 'Xie') ['Ph.D.', 'Associate Professor', 'sxie@mail.med.upenn.edu']
('Wei', 'Yang') ['Ph.D.', 'Assistant Professor', 'weiyang@mail.med.upenn.edu']
'''


