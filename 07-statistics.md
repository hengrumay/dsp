# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

### Instructions for cloning the repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/metisgh/prework  
(Windows):  C:/ds/metis/metisgh/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/metisgh/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/metisgh/prework/ThinkStats2/code
```

---

###Required Exercises

*Include your Python code, results and explanation (where applicable).*

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 



###Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>>  
> > To solve for the conditional probability that Elvis was an identical twin given that his twin was a boy, we need to figure out the likelihood of twins (identical and fraternal) being both boys.    
> >  We presume that in general the probability of a baby being born boy or girl is respectively 0.5 .     

> >  Identical twins  are  both of the same sex . Therefore the conditional probability of a set of identical twins being  either boys or girls is 0.5.   
> >  Expressing this in probability 'notation': 

```{python}
#==============================================================================
# # IDENTICAL TWINS : itwins: bb OR gg
#  P(bb_itwin) = 1/2       #P(b|id)
#  P(gg_itwin) = 1/2      #P(~b|id)
#==============================================================================
'''#P(b|id)'''
Pbb_itwin = 0.5
'''#P(~b|id)'''
Pxbb_itwin = 0.5
```

> > As for fraternal twins, gender combinations can manifest where both fraternal twins are boys, or both are girls, or the first born twin is a boy and his twin a girl, or vice versa.    
> > Therefore, the oonditional probability of  fraternal twins being both boys is 0.25. This is expressed in probability 'notation' below:

```{python}
#==============================================================================
# # FRATERNAL TWINS: ftwins : b-b OR b-g OR g-b OR g-g
# P(bb_ftwin) | P(gg_ftwin) | P(bg_ftwin) | P(gb_ftwin) == 1/4
# P(b|~id)     #================ #P(~b|~id) ==================#
#==============================================================================
'''#P(b|~id)'''
Pbb_ftwin = 1/4
'''#P(~b|~id)'''
Pxbb_ftwin = 3/4
```

> >  We were provided with the observation  the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.   
> > This is expressed in probability 'notation' as follows:   
```{python}
#==============================================================================
# # P(itwin)
'''# p(id)'''
Pitwin= 1/300       # p(id)
#
# # P(ftwin)
'''# P(~id)'''
Pftwin = 1/125      # P(~id)
#==============================================================================
```

> >  The law of conditional probability allows us to infer the likelihood of events :   
```{python}
#==============================================================================
# ## Law of Prob
# P(B) = [P(A)*P(B|A)] + [P(~A) * P(B|~A)]
#==============================================================================
```

> >  We can infer the probability of twins being both boys as follows:   
```{python}
#==============================================================================
# # P(twin_bb)
# P(itwin & twin_brother) = 1/300 * 1/2   # P(id n b)
# P(ftwin & twin_brother) = 1/125 * 1/4   # P(~id n b)
#==============================================================================
'''#P(b) == P(b|id) * P(id) + P(b|~id) * P(~id)'''
Pbb = Pbb_itwin * Pitwin + Pbb_ftwin * Pftwin
#Pbb = (1/2 * 1/300) + (1/4 * 1/125) == 0.003666666666666667 == 11/3000
```

> > Finally, Bayes Theorem  helps with deriving the conditional probability of interest:   
```{python}
#==============================================================================
# ## Bayes Theorem
# P(A|B) =  P(A)*P(B|A) / ( [P(A)*P(B|A)] + [P(~A) * P(B|~A)] )
#==============================================================================
```

> >  By dividing the probability of identical twins being both boys  by the probability of twins who are boys, we  arrive at the conditional probability of  a set of twins being identical given that the twins are boys :   
```{python}
#==============================================================================
# # P(itwin | b)
#==============================================================================
'''#P(id|b) = P(b|id) * P(id) / P(b)'''
Pitwin_bb = (Pbb_itwin * Pitwin) / Pbb
#Pitwin_bb = (1/2 * 1/300 ) / (11/3000) == 0.45454545454545453 == 5/11
```

> >  Therefore the probability that Elvis was an identical twin is 5/11 .
> >  Actually this was [a question posted by Andrew Gelman in 2005](http://andrewgelman.com/2005/01/03/what_is_the_pro/).



---

###Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q7. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

###Q8. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

---

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.







