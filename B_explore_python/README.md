# Assignment B: Explore Python &nbsp; (<span style="color:red">20 Pts</span>)

This assignment demonstrates Python's basic data structures.

### Challenges
1. [Challenge 1:](#1-challenge-1-indexing-fruits) Indexing Fruits
2. [Challenge 2:](#2-challenge-2-packaging-fruits) Packaging Fruits
3. [Challenge 3:](#3-challenge-3-sorting-fruits) Sorting Fruits
4. [Challenge 4:](#4-challenge-4-income-analysis) Income Analysis
5. [Challenge 5:](#5-challenge-5-code-income-analysis) Code Income Analysis
6. [Challenge 6:](#6-challenge-6-explore-python-built-in-functions)
    Explore Python built-in functions

&nbsp;
### 1.) Challenge 1: Indexing Fruits
Explore Python. Review Python's basic
[data structures](https://www.dataquest.io/blog/data-structures-in-python).

```py
# Python is known for advanced list processing.
>>> fruits = ['apple', 'pear', 'orange', 'banana']
>>> print(fruits)
>>> fruits
['apple', 'pear', 'orange', 'banana']

>>> len(fruits)
4

>>> print(f"the third fruit is: {fruits[2]}")
the third fruit is: orange

>>> print(f"the second and third fruits are: {fruits[1:3]}")
the second and third fruits are: ['pear', 'orange']

>>> print(f"the last fruit is: {fruits[-1]}")
the last fruit is: banana

>>> print(f"the last two fruits are: {fruits[-2:]}")
the last two fruits are: ['orange', 'banana']
```
Perform examples on your laptop. (1 Pt)


&nbsp;
### 2.) Challenge 2: Packaging Fruits

Review Python's built-in
[data structures](https://www.dataquest.io/blog/data-structures-in-python).
Perform examples and answer questions on a piece of paper.

1. What are data types for `fruits`, `fruitbag` and `fruitbox` called? (1 Pt)

1. Name three properties that characterize each data type. (1 Pts)

1. Why does output for `fruitbag` differ from input? (1 Pt)

    ```py
    >>> fruits = ['apple', 'pear', 'orange', 'banana']
    >>> fruitbag = {'apple', 'pear', 'orange', 'banana'}
    >>> fruitbox = ('apple', 'pear', 'orange', 'banana')

    >>> print(fruits)
    ['apple', 'pear', 'orange', 'banana']

    >>> print(fruitbox)
    ('apple', 'pear', 'orange', 'banana')

    >>> print(fruitbag)
    {'orange', 'banana', 'apple', 'pear'}

    >>> print(fruits[1])
    pear
    >>> print(fruitbox[1])
    pear
    >>> print(fruitbag[1])
    TypeError: object is not subscriptable
    >>>
    ```


1. How is the structure for Eric called? (1 Pt)

    ```py
    eric = {"name": "Eric", "salary": 5000, "birthday": "Sep 25 2001"}

    >>> print(eric)
    {'name': 'Eric', 'salary': 5000, 'birthday': 'Sep 25 2001'}
    >>> print(eric["salary"])
    5000
    ```


&nbsp;
### 3.) Challenge 3: Sorting Fruits

1. What is the difference between *sort()* and built-in function *sorted()*,
[link](https://www.python-engineer.com/posts/sort-vs-sorted) (2 Pts)?

    ```py
    >>> fruits = ['apple', 'pear', 'orange', 'banana']

    >>> f1 = sorted(fruits)
    >>> print(f"{f1},\n{fruits}")
    ['apple', 'banana', 'orange', 'pear'],
    ['apple', 'pear', 'orange', 'banana']

    >>> f2 = fruits.sort()
    >>> print(f"{f2},\n{fruits}")
    None,
    ['apple', 'banana', 'orange', 'pear']
    ```

1. Some people say that Arrays in other languages are
Lists in Python. Other people argue that Tuples are Arrays.
   - a) Which statement is (more) correct? (1 Pt)
   - b) Name two differences between Arrays and Lists?
        (1 Pt)

1. Draw sketches to visualize Python data structures:
*List*, *Set*, *Tuple*, *Dictionary* and *Array* (from other
languages like C, C++). (1 Pt)


&nbsp;
### 4.) Challenge 4: Income Analysis
The US tax Income Revenue Service (IRS) annually 
publishes income statistics by ZIP codes
([reports](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi)).

For example, California ZIP Code
[93636](https://simplemaps.com/us-zips/93636)
is a rural agricultural county of Madera, north of
Fresno in the Central Valley.
Income distribution for the tax year 2020 was:
```
income bracket:         number of tax returns
                        filed in bracket
[$1 to under $25,000]             1,800
[$25,000 to under $50,000]        1,380
[$50,000 to under $75,000]          980
[$75,000 to under $100,000]         830
[$100,000 to under $200,000]      1,660
[$200,000 or more < $50M>]          550
```
Numbers mean that 980 tax returns were filed in the
bracket [$50,000 to under $75,000] taxable income.

A common statistical analysis is to compute:

- the *mean (average) income* per tax filer and the

- the *median income* per tax filer.

Assume $50 million as upper limit for *"more"* in the
highest bracket.

Answer questions:

1. What is the difference between *mean (average)* and
*median* calculations? (1 Pt)
    - Why are both indicators relevant?

1. Calculate manually the *average* income for Madera
    county. (1 Pt)

1. Calculate manually the *median* income for Madera
    county. (1 Pt)


&nbsp;
### 5.) Challenge 5: Code Income Analysis

Write Python code to perform this income analysis.

<b>Use pure Python</b> (no *Pandas* nor *Numpy*) for this simple example.

Think about following steps:

1. Chose a suitable Python structure to represent tax data for a ZIP code. (1 Pt)
    - Which data is relevant for the analysis?
    - How can data be structured?
    - Use only use Python structures: *list*, *set*, *tuple*, *dictionary*. 

1. Code data for one ZIP code into your structure
    (no need to read `.xlsx`-files). (1 Pt)

1. Define two functions `mean_income(...)` and `median_income(...)` that take
    data for one ZIP code as input and return respective numbers.

1. Define function `number_of_returns(...)`.

1. Implement functions and demonstrate they return correct values. (4 Pts)

1. Demonstrate analysis for other ZIP codes:
    - [94040](https://simplemaps.com/us-zips/94040) (Mountain View, CA),
    - [94304](https://simplemaps.com/us-zips/94304) (Palo Alto, CA),
    - [94027](https://simplemaps.com/us-zips/94027) (Atherton, CA),
    - [50860](https://simplemaps.com/us-zips/93636) (Redding, IA) and
    - [10023](https://simplemaps.com/us-zips/10023) (New York City, NY Upper West side). (1 Pt)


&nbsp;
### 6.) Challenge 6: Explore Python built-in functions
Learn about Python's
[built-in functions](https://docs.python.org/3/library/functions.html).
Test the
[*globals()*](https://docs.python.org/3/library/functions.html#globals)
function.
```py
  >>> globals()
  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_
  importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module
  'builtins' (built-in)>, 'fruits': ['apple', 'pear', 'orange', 'banana']}
```
Test the [*input()*](https://docs.python.org/3/library/functions.html#input) function.
```py
  >>> s = input('--> ')
  --> Monty Python's Flying Circus
  >>> s
  "Monty Python's Flying Circus"
  exit()
```
(1 Pt)
