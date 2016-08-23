# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>   
- List and Tuples are similar in that they are an (ordered) array of items (integers, strings etc.) and these items are indexed starting from 0.   
- They differ in that the items in Tuples, enclosed within "()", are 'immutable' i.e. non-changeable whereas the items enclosed within "[]" in a List are mutable. Tuples are considered 'faster' to manipulate because of their immutability.     
- Tuples are also comparable and hashable, which allow one to sort items in tuples and use tuples as key values in dictionaries.  
- Hash methods in dictionaries require unique mappings between keys and their corresponding values. Given the mutability of lists, they are not considered to provide a valid hash_method and can lead to key-pairing errors.  

>> Some useful references :   
  - http://sthurlow.com/python/lesson06/  
  - http://www.thomas-cokelaer.info/tutorials/python/data_structures.html  
  - https://wiki.python.org/moin/DictionaryKeys  
  - http://www.pythonlearn.com/html-008/cfbook011.html  
  - http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/  


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE  
- Order is kept in Lists but not in (Dictionaries and) Sets. -- if order is required, use Lists.  
- Sets require items to be hashable ##, list doesn't: ###### if you have non-hashable items, therefore, you cannot use set and must instead use list.

##### set forbids duplicates, list does not: also a crucial distinction. (A "multiset", which maps duplicates into a different count for items present more than once, can be found in collections.Counter -- you could build one as a dict, if for some weird reason you couldn't import collections, or, in pre-2.7 Python as a collections.defaultdict(int), using the items as keys and the associated value as the count).

##### Checking for membership of a value in a set (or dict, for keys) is blazingly fast (taking about a constant, short time), while in a list it takes time proportional to the list's length in the average and worst cases. So, if you have hashable items, don't care either way about order or duplicates, and want speedy membership checking, set is better than list.

>> Some useful references :   
  - http://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set  
  - http://www.thomas-cokelaer.info/tutorials/python/sets.html

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





