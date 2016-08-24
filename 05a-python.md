# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> >   
- List and Tuples are similar in that they are an (ordered) array of items (integers, strings etc.) and these items are indexed starting from 0.   
- They differ in that the items in Tuples, enclosed within "()", are 'immutable' i.e. non-changeable whereas the items enclosed within "[]" in a List are mutable. Tuples are considered 'faster' to manipulate because of their immutability.     
- Tuples are also comparable and hashable**, which allow one to use tuples as key values in dictionaries.  
- Hash methods in dictionaries require unique mappings between keys and their corresponding values. Given the mutability of lists, they are not considered to provide a valid hash_method and can lead to key-pairing errors.  

> > **An object is hashable if it has an associative hash value (i.e. a __hash__() method) that never changes during its lifetime and it can be compared to other objects (i.e. it has an __eq__() method). Hashable objects which compare equal must have the same hash value.  

> >Some useful references :   
  - http://sthurlow.com/python/lesson06/  
  - http://www.thomas-cokelaer.info/tutorials/python/data_structures.html  
  - https://wiki.python.org/moin/DictionaryKeys  
  - http://www.pythonlearn.com/html-008/cfbook011.html  
  - http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
  - https://docs.python.org/3/glossary.html


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> >   
- Order is kept in Lists but not in (Dictionaries and) Sets. If order is required, use Lists.
- Sets require items to be hashable**, lists do not. For non-hashable items, use List(s).
- Sets do not allow duplicates, Lists do. 

```
''' Examples of Set(s)'''
>>> a = set([1, 2, 3, 4])
>>> b = set([3, 4, 5, 6])

# Union:    a.union(b)
>>> a | b 
{1, 2, 3, 4, 5, 6}

# Intersection:   a.intersection(b)
>>> a & b 
{3, 4}

>>> c = a & b
>>> c
set([3, 4])
>>> c.issuperset(a)
False

# Subset:   b.issubset(a)
>>> a < b 
False

# Difference:   a.difference(b)
>>> a - b 
{1, 2}

# Symmetric Difference:   a.symmetric_difference(b)
>>> a ^ b 
{1, 2, 5, 6}
```

- Checking for membership of a value in a set (or dict, for keys) is swift compared to finding an element in a list due to the time taken being roughly proportional to the list's length.  

> > Some useful references :   
  - http://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set  
  - http://www.thomas-cokelaer.info/tutorials/python/sets.html
> >   


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





