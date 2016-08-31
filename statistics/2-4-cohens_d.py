#<!---
## h-rm_tan 30/31 Aug2016

#==============================================================================
# ## REFs
#==============================================================================
## http://stackoverflow.com/questions/33166332/running-python-code-in-markdown
#Save the file as markdown.Rmd, and use R to compile it. It will run the Python code using python.
#R command: rmarkdown::render('markdown.Rmd','output.html')
#EDIT: A native solution is apparently Pweave: it works with latex and markdown.

## http://stackoverflow.com/questions/38039697/using-an-r-markdown-style-document-rmd-as-input-for-pweave

# STATSMODELS
# http://stackoverflow.com/questions/21532471/how-to-calculate-cohens-d-in-python
# http://jpktd.blogspot.com/2013/03/statistical-power-in-statsmodels.html
## http://statsmodels.sourceforge.net/0.6.0/index.html
# https://pypi.python.org/pypi/statsmodels

# https://docs.python.org/3/tutorial/inputoutput.html

#==============================================================================

#---!>


'''
#[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
#[Variables Ref] (http://greenteapress.com/thinkstats2/html/thinkstats2002.html)
## https://en.wikipedia.org/wiki/Effect_size
'''

'''
>> Task: Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?
'''

#==============================================================================
# ## FILE PATHS
#==============================================================================
filepath = '/Users/hrm/Documents/Dropbox/DSrelated/GIThub/dsp/ThinkStats2/code/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''

#==============================================================================
# # LOAD FILEs
#==============================================================================
import nsfg
df = nsfg.ReadFemPreg()

# nsfg.CleanFemPreg(df)
# df.columns

#==============================================================================
# 1.5  Variables

#There are 244 variables in total. For the explorations in this book, I use the following variables:

#caseid is the integer ID of the respondent.

#prglngth is the integer duration of the pregnancy in weeks.

#outcome is an integer code for the outcome of the pregnancy. The code 1 indicates a live birth.

#pregordr is a pregnancy serial number; for example, the code for a respondent’s first pregnancy is 1, for the second pregnancy is 2, and so on.

#birthord is a serial number for live births; the code for a respondent’s first child is 1, and so on. For outcomes other than live birth, this field is blank.

#birthwgt_lb and birthwgt_oz contain the pounds and ounces parts of the birth weight of the baby.

#agepreg is the mother’s age at the end of the pregnancy.

#finalwgt is the statistical weight associated with the respondent. It is a floating-point value that indicates the number of people in the U.S. population this respondent represents.

#==============================================================================

#df[['caseid','pregordr','agepreg', 'prglngth','outcome','birthord', 'birthwgt_lb', 'finalwgt']]

#import pandas as pd

DFtmp = df[['caseid','outcome','birthord','prglngth', 'totalwgt_lb']]

## Exclude those where brithord == NaN --> likely early pregnancy termination...
DF = DFtmp.dropna()

livebirths = DF[DF.outcome == 1]

firstBorn = livebirths[livebirths.birthord == 1]
NOTfirstBorn = livebirths[livebirths.birthord != 1]

#group1, group2 = [firstBorn['totalwgt_lb'].dropna(), NOTfirstBorn['totalwgt_lb'].dropna()]

#==============================================================================
# Some Summary Stats
#==============================================================================
firstBWt_mstd = [format(firstBorn['totalwgt_lb'].mean(), '.2f') , format(firstBorn['totalwgt_lb'].std(), '.2f')]
#['7.20', '1.42']

NOTfirstBWt_mstd = [format(NOTfirstBorn['totalwgt_lb'].mean(), '.2f') , format(NOTfirstBorn['totalwgt_lb'].std(), '.2f')]
#['7.33', '1.39']


firstBprgL_mstd = [format(firstBorn['prglngth'].mean(), '.2f') , format(firstBorn['prglngth'].std(), '.2f')]
#['38.61', '2.79']

NOTfirstBprgL_mstd = [format(NOTfirstBorn['prglngth'].mean(), '.2f') , format(NOTfirstBorn['prglngth'].std(), '.2f')]
#['38.53', '2.58']


#==============================================================================
# Define Cohen's D
#==============================================================================
import math

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

#==============================================================================
# Assess Size Effects for Differences
#==============================================================================

cD_weight = CohenEffectSize(firstBorn['totalwgt_lb'], NOTfirstBorn['totalwgt_lb'])
# -0.088672927072602

cD_prgL = CohenEffectSize(firstBorn['prglngth'], NOTfirstBorn['prglngth'])
# 0.028879044654449883


#==============================================================================
# Assess Mean Differences by t-test
#==============================================================================

import statsmodels.api as sm

tt_wtDiff = sm.stats.ttest_ind(firstBorn['totalwgt_lb'], NOTfirstBorn['totalwgt_lb'], alternative='two-sided', usevar='pooled')
#tstat | pval | df : # (-4.2124577723189471, 2.5505957270456433e-05, 9036.0)
#tt_wtDiff[(0)],tt_wtDiff[(1)]

tt_prgLDiff = sm.stats.ttest_ind(firstBorn['prglngth'], NOTfirstBorn['prglngth'], alternative='two-sided', usevar='pooled')
#tstat | pval | df : # (1.3279213634203044, 0.18423762856820036, 9036.0)
#tt_prgLDiff[(0)], tt_prgLDiff[(1)]


## #################################################################################################
#==============================================================================
# ## RESPONSE in md
#==============================================================================
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
> > [Variables Ref] (http://greenteapress.com/thinkstats2/html/thinkstats2002.html)
[Effect Sizes from Wikipedia] (https://en.wikipedia.org/wiki/Effect_size_)

> > ####Task: Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. Compute `Cohen’s d` to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

> >
First borns (mean weight = `7.20` lbs) generally weigh less than non-first borns (mean weight = `7.33` lbs). The effect size of this difference is `-0.089` standard deviations, which is small (Cohen's d: `d <= 0.2` small; `0.2< d <=0.5`: moderate; `d => 0.8`: large). Nonetheless, t-test of mean difference yielded significant differences (`t=-4.212, p=2.5506e-05, df=9036`).
> >
The pregnancy length of first borns (mean = `38.61` lbs) do not differ much from that of non-first borns (mean = `38.53` lbs). The effect size of this difference is `0.028` standard deviations, which is  small ((Cohen's d: `d <= 0.2` small; `0.2< d <=0.5`: moderate; `d => 0.8`: large). Additionally, t-test of mean difference yielded no significant difference (`t=1.328, p=0.184238, df=9036`).

--

```{python}

#==============================================================================
# ## LOAD FILEs
#==============================================================================
import nsfg
df = nsfg.ReadFemPreg()

#==============================================================================
# ## TIDY DF
#==============================================================================
DFtmp = df[['caseid','outcome','birthord','prglngth', 'totalwgt_lb']]

#==============================================================================
# ## Exclude those where brithord == NaN --> likely early pregnancy termination...
#==============================================================================
DF = DFtmp.dropna()

#==============================================================================
# ## Retrieve Relevant variables
#==============================================================================
livebirths = DF[DF.outcome == 1]
firstBorn = livebirths[livebirths.birthord == 1]
NOTfirstBorn = livebirths[livebirths.birthord != 1]

#==============================================================================
# ## Summary Stats
#==============================================================================
firstBWt_mstd = [firstBorn['totalwgt_lb'].mean(), firstBorn['totalwgt_lb'].std()]
NOTfirstBWt_mstd = [NOTfirstBorn['totalwgt_lb'].mean(), NOTfirstBorn['totalwgt_lb'].std()]

firstBprgL_mstd = [firstBorn['prglngth'].mean(), firstBorn['prglngth'].std()]
NOTfirstBprgL_mstd = [NOTfirstBorn['prglngth'].mean(), NOTfirstBorn['prglngth'].std()]

#==============================================================================
# ## Define Cohen's D
#==============================================================================
import math

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

#==============================================================================
# ## Assess Size Effects for Differences
#==============================================================================
cD_weight = CohenEffectSize(firstBorn['totalwgt_lb'], NOTfirstBorn['totalwgt_lb'])
cD_prgL = CohenEffectSize(firstBorn['prglngth'], NOTfirstBorn['prglngth'])


#==============================================================================
# ## ttest -- assessment:
#==============================================================================
import statsmodels.api as sm

tt_wtDiff = sm.stats.ttest_ind(firstBorn['totalwgt_lb'], NOTfirstBorn['totalwgt_lb'], alternative='two-sided', usevar='pooled')
#tstat | pval | df : # (-4.2124577723189471, 2.5505957270456433e-05, 9036.0)

tt_prgLDiff = sm.stats.ttest_ind(firstBorn['prglngth'], NOTfirstBorn['prglngth'], alternative='two-sided', usevar='pooled')
#tstat | pval | df : # (1.3279213634203044, 0.18423762856820036, 9036.0)


#==============================================================================
# # RESPONSE
#==============================================================================
print ('First borns (mean weight = {0:.2f} lbs) generally weigh less than non-first borns (mean weight = {1:.2f} lbs). The effect size of this difference is {2:.3f} standard deviations, which is small (Cohen\'s d: d <= 0.2 small; 0.2< d <=0.5: moderate; d => 0.8: large). Nonetheless, t-test of mean difference yielded significant differences (t={3:.3f}, p={4:g}, df={5:.0f}).' .format(firstBWt_mstd[0], NOTfirstBWt_mstd[0], cD_weight, tt_wtDiff[0], tt_wtDiff[1], tt_wtDiff[2]) )


print ('The pregnancy length of first borns (mean = {0:.2f} lbs) do not differ much from that of non-first borns (mean = {1:.2f} lbs). The effect size of this difference is {2:.3f} standard deviations, which is  small (Cohen\'s d: d <= 0.2 small; 0.2< d <=0.5: moderate; d => 0.8: large). Additionally, t-test of mean difference yielded no significant difference (t={3:.3f}, p={4:g}, df={5:.0f}).' .format(firstBprgL_mstd[0], NOTfirstBprgL_mstd[0], cD_prgL, tt_prgLDiff[0], tt_prgLDiff[1], tt_prgLDiff[2]) )


```