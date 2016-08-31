[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

> > [Variables Ref] (http://greenteapress.com/thinkstats2/html/thinkstats2002.html)  
[Effect Sizes from Wikipedia] (https://en.wikipedia.org/wiki/Effect_size_)  

> > ####Task: Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. Compute `Cohen’s d` to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

> >
First borns (mean weight = `7.20` lbs) generally weigh less than non-first borns (mean weight = `7.33` lbs). The effect size of this difference is `-0.089` standard deviations, which is small (Cohen's d: `d <= 0.2` small; `0.2< d <=0.5`: moderate; `d => 0.8`: large). Nonetheless, t-test of mean difference yielded significant differences (`t=-4.212, p=2.5506e-05, df=9036`).
> >
The pregnancy length of first borns (mean = `38.61` lbs) do not differ much from that of non-first borns (mean = `38.53` lbs). The effect size of this difference is `0.028` standard deviations, which is  small (Cohen's d: `d <= 0.2` small; `0.2< d <=0.5`: moderate; `d => 0.8`: large). Additionally, t-test of mean difference yielded no significant difference (`t=1.328, p=0.184238, df=9036`).

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
