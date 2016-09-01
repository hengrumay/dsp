
[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

> > ##### In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

> > Task: In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). 

> > What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.


```{python}
#==============================================================================
# # LOAD FILEs
#==============================================================================
#import numpy as np

#import pandas as pd
#import random


import scipy.stats
scipy.stats.norm.cdf(0)

```
> > We create the population distributions for men and women based on the given mean and standard deviations (sigma) information:

```{python}
### Men
Mmu = 178
Msigma = 7.7
Mdist = scipy.stats.norm(loc=Mmu, scale=Msigma)
#type(dist)  #scipy.stats._distn_infrastructure.rv_frozen

# Check:
Mdist.mean(), Mdist.std()
# (178.0, 7.7000000000000002)


## Women
Wmu = 163
Wsigma = 7.3
Wdist = scipy.stats.norm(loc=Wmu, scale=Wsigma)

# Check:
Wdist.mean(), Wdist.std()
#(163.0, 7.2999999999999998)
```

> > We can assess its CDF. e.g. How many people are more than one standard deviation below the mean? -- It is about 16% for both men and women.

```{python}
Mdist.cdf(Mmu-Msigma)
#0.15865525393145741

Wdist.cdf(Wmu-Wsigma)
#0.15865525393145663
```

> > Determin how many people are between 5'10" and 6'1". First converting the imperial height measure to metric (more sensible!), and then using the CDF distribution to find the percentile rank(s). 

```{python}

def feetNinch_to_cm(feet, inches):
    #http://www.calculatorsoup.com/calculators/conversions/heightftcm.php
    inches2cm = 2.54
    ft2inches = 12
    #ft2cm = 30.48

    cm = (feet*ft2inches + inches) *inches2cm
    return cm
```

```{python}
## Men
mCumPct_lowEnd = Mdist.cdf(feetNinch_to_cm(5,10))   # 5'10" == 177.8cm
mCumPct_highEnd = Mdist.cdf(feetNinch_to_cm(6,1))   # 6'1" == 185.4vm
mDiff=mCumPct_highEnd- mCumPct_lowEnd

np.array([mCumPct_lowEnd, mCumPct_highEnd, mDiff])*100
#array([ 48.96390279,  83.23858655,  34.27468376])
#(0.48963902786483265, 0.83173371081078573, 0.34209468294595308)
``` 
> > About 34.3% men are within the 5'10" and 6'1" height range.

```{python}
wCumPct_lowEnd = Wdist.cdf(feetNinch_to_cm(5,10))   # 5'10" == 177.8cm
wCumPct_highEnd = Wdist.cdf(feetNinch_to_cm(6,1))   # 6'1" == 185.4vm
wDiff=wCumPct_highEnd- wCumPct_lowEnd

np.array([wCumPct_lowEnd, wCumPct_highEnd, wDiff])*100
#array([ 97.8689099 ,  99.89341159,   2.02450169])
```
> > For the height range requirment, only about 2 % of females will likely qualify. See also the [interview] ('http://www.atlasobscura.com/articles/the-ao-exit-interview-12-years-in-the-blue-man-group') that mentioned the rarity of female performers.
