
[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Task: Something like the class size paradox appears if you survey children and ask how many children are in their family.   
Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.

>> Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household

```{python}
#==============================================================================
# # LOAD FILEs
#==============================================================================

#%matplotlib inline
import chap01soln
respdr = chap01soln.ReadFemResp()

# Make a PMF of numkdhh, the number of children under 18 in the respondent's household.
import thinkstats2
actual_pmf = thinkstats2.Pmf(respdr.numkdhh, label='actual')

```{python}

>> Next compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

```{python}

## ThinkStats2 defined Un/BiasPmf
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.
    If pmf is the distribution of true values, the result is the distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students how big their classes are, large classes are oversampled in
    proportion to their size.
    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.
     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

#Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.
biased_pmf = BiasPmf(actual_pmf, label='biased')


```

>> Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

```{python}
import matplotlib.pyplot as plot
import thinkplot

#Display the actual Pmf and the biased Pmf on the same axes.
plot.figure(figsize=(6,6))
thinkplot.Pmfs([actual_pmf, biased_pmf])
plot.xlabel('Number of Children under 18 yrs')
plot.ylabel('Probability Mass Function (PMF)')
plot.legend()
plot.title('Actual vs. Observed Number of Children in Household')
plot.savefig(fpath+'figs/ch3ex1.png', dpi=100, format='png')
plot.show()


print( 'Actual Mean Number of Children = {0:.3f}' . format(actual_pmf.Mean()) )
#1.024
print( 'Observed Mean Number of Children = {0:.3f}' . format(biased_pmf.Mean()) )
#2.404


```

<img src="../img/ch3ex1.png"/>

> > As expected the actual mean number of children is `1.024` and less than the observed mean number `2.404` if children themselves are surveyed, since you won't be getting representative information about household without children from non-existing children!


> > Additional explorations ---   

```{python}

#==============================================================================
# #Given a Hist, we can make a dictionary that maps from each value to its probability:
#==============================================================================

import numpy as np
#respdr.numkdhh.hist() || plot.hist()
#respdr.numkdhh.hist(bins=np.arange(0,7,1), align='left', normed = True, histtype='step')

# creat Histogram Dict
respdr_NumKFreq = respdr.numkdhh.value_counts()
histDict = {i:respdr_NumKFreq[i] for i in range(len(respdr_NumKFreq))}

n = respdr.numkdhh.notnull().sum() #respdr.numkdhh.sum() # hist.Total()
pmf_man = {}
for numC, freq in histDict.items():
    pmf_man[numC] = freq / n


#import numpy as np
pmf_mat = np.array(list(pmf_man.items()))
numC, pmfnumC = pmf_mat[:,0], pmf_mat[:,1]
mean_man = sum(numC*pmfnumC)
#np.dot(pmfnumC, numC[:,None]) == 1.0


#==============================================================================
# ### Recreate biased Distributions from probmassfunction (pmf) for recreating plots without thinkstats functions -- because it is like a black box and not helpful
#==============================================================================

import pandas as pd

biased_pmfDict= np.array(list(biased_pmf.Items()))
biased_pmfDF = pd.DataFrame(biased_pmfDict, columns=['NumC','pmf'])

#actual_pmfDF = pd.DataFrame(pmf_mat, columns=['NumC','pmf'])

##########################################################
from scipy import stats
x = list(np.arange(len(biased_pmfDF['NumC'])))
p = list(biased_pmfDF['pmf'])
custm = stats.rv_discrete(name='custm', values=(x, p))


n = respdr.numkdhh.notnull().sum()  #respdr.numkdhh.sum()
# custm.rvs(size=n)
pmfDist = pd.DataFrame(custm.rvs(size=n), columns=['biased'])#, dtype='int64')
##########################################################


import matplotlib.pyplot as plot
# actualNbiased = pd.concat([respdr.numkdhh[respdr.numkdhh.notnull()], pmfDist.biased], axis=1)
#actualNbiased.hist(bins=np.arange(0,7,1), align='left', normed = True, histtype='step')

plot.subplot(111)
plot.hist(respdr.numkdhh, bins=np.arange(0,7,1), align='left', normed = True, histtype='step', alpha=0.5, label='actual')
plot.hist(pmfDist.biased, bins=np.arange(0,7,1), align='left', normed = True, histtype='step', alpha=0.5, label='biased', edgecolor = 'c')

```