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

> > **An object is hashable if it has an associative hash value (i.e. a __hash__() method) that does not change and it can be compared to other objects (i.e. it has an __eq__() method). Hashable objects which compare equal must have the same hash value.  

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

> >   ###
- Order is kept in Lists but not in (Dictionaries and) Sets. If order is required, use Lists.
- Unlke Lists, Sets do not allow duplicates and are therefore commonly used to build sequence of unique items or identifiers.  

```
### --- Examples of List(s) ---
>>> stack = ['a', 'b', 'c']

>>> stack.append(['d', 'e', 'f'])
>>> stack
['a', 'b', 'c', ['d', 'e', 'f']]


>>> stack.extend(['d', 'e','f'])
>>> stack
['a', 'b', 'c', 'd', 'e', 'f']

>>> a_list = ['a','b','c','b', 'a']
>>> a_list.index('b')
1
>>> a_list.index('b', 2)
3

>>> b_list = ['b','c','b']
>>> b_list.insert(2, 'a')
>>> b_list
['b', 'c', 'a', 'b']

>>> c_list = ['a','b','c','b', 'a']
>>> c_list.remove('a')
>>> c_list
['b', 'c', 'b', 'a']

>>> c_list.pop()
'a'
>>> c_list
['b', 'c', 'b']

>>> b_list.sort()
>>> b_list
['a', 'b', 'b', 'c']

>>> b_list.sort(reverse=True)
>>> b_list
['c', 'b', 'b', 'a']

>>> stack.reverse()   #stack = ['a', 'b', 'c', 'd', 'e', 'f']
>>> stack
['f', 'e', 'd', 'c', 'b', 'a']

```

```
### --- Examples of Set(s) ---

>>> a = set([1, 2, 3, 4])
>>> b = set([3, 4, 5, 6])

# Union:    a.union(b)
>>> a | b 
set([1, 2, 3, 4, 5, 6])

# Intersection:   a.intersection(b)
>>> a & b 
set([3, 4])

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
set([1, 20])

# Symmetric Difference:   a.symmetric_difference(b)
>>> a ^ b 
set([1, 2, 5, 6])

```
> >  
- Checking for membership of a value in a set (or dict, for keys) is often faster compared to finding an element in a list due to the time taken being roughly proportional to the list's length.  

```
>>> setL=set(range(1000))
>>> setL.issuperset([888])
True

>>> listL = range(1000)
>>> [n for n in listL if n==888 ]
[888]

```

> > Some useful references :   
  - http://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set  
  - http://www.thomas-cokelaer.info/tutorials/python/sets.html
> >   


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> >   Anonymous inline functions can be created with the lambda keyword. A function invoked by the keyword "lambda" is a single expression that is evaluated when it is called. Similar to nested function definitions, lambda functions can reference variables from the containing environment. Unlike regular functions, lamda functions do not require using the "return" statement; they always return the outcome of their expression. 

```
>>> def add2number (n): return lambda x: x + n
>>> 
>>> f = add2number(2)
>>> g = add2number(6)
>>> 
>>> print f(42), g(42)
44 48
>>> 
>>> print add2number(22)(33)
55


>>> colors = ["blue", "lavender", "red", "yellow"]
# Sort colors by length, in reverse (descending) order.
>>> for color in sorted(colors, key=lambda color: len(color), reverse=True):
>>>     print(color)

lavender
yellow
blue
red

>>> sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())
['differently', 'Some', 'sort', 'words']

```


> >  
ref http://www.secnetix.de/olli/Python/lambda_functions.hawk  
ref https://docs.python.org/3/tutorial/controlflow.html  
ref http://www.python-course.eu/lambda.php  
ref http://www.dotnetperls.com/sort-python  
ref https://wiki.python.org/moin/HowTo/Sorting

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.  

> > #### List Comprehensions  
- List comprehension:   a method for transforming one iterable list (i.e. an object capable of returning elements individually at a time) into another list. During this transformation, elements can be conditionally included in the new list and each element can also be transformed where needed.

```
>>> x = range(0,6) #[0, 1, 2, 3, 4, 5]

## for-loop
>>> doubled_x = []
>>> for n in x:
>>>     if n % 2 == 1:
>>>         doubled_x.append(n * 2)

## list-comprehended
>>> doubled_x = [n * 2 for n in x if n % 2 == 1]
>>> doubled_x
[2, 6, 10]

```
> >  
- Map:       A special function for cases when you need to do a specific action on every element of a list. It enables you to accomplish this without having to write the loop; much like the use of list-comprehension. It is often used with the lambda function. 

```
## map(func, seq)
>>> result = map(lambda x: "The word %s is %s letters long" % (x, len(x)), [ 'home', 'hello'] )
>>> print result
['The word home is 4 letters long', 'The word hello is 5 letters long']

## example with defined function and data-seq
>>> def fahrenheit(tempC):
    return ((float(9)/5)*tempC + 32)
    
>>> def celsius(tempF):
    return (float(5)/9)*(tempF-32)

>>> temp = (36.5, 37, 37.5,39)

>>> F = map(fahrenheit, temp)
[97.7, 98.60000000000001, 99.5, 102.2]
>>> C = map(celsius, F)
[36.5, 37.00000000000001, 37.5, 39.0]
```
> >  
- Filter:   The filter() function is also often used with the lambda function. It is used in conjunction with a function and an iterable object. It returns the items of the sequence for which function(item) is true.

```
## filter(func, seq)
## [x for x in seq if func(x)]
>>> filter(lambda x: x%2 == 0, [0,3,6,9])
[0, 6]

```

> > #### Set Comprehensions  

```
>>> newSet = {x for x in 'abracadabra' if x not in 'abc'}
>>> newSet
set(['r', 'd'])

```

> > #### Dictionary Comprehensions  

```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

```

> > Useful Refs:     
- https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps  
- http://www.python-course.eu/lambda.php  
- http://www.python-course.eu/list_comprehension.php  
- http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
- http://www.thomas-cokelaer.info/tutorials/python/basics.html  




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





