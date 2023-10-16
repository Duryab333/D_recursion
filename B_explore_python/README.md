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
Review Python's basic
[data structures](https://www.dataquest.io/blog/data-structures-in-python).

```py
# Python is known for advanced list processing.
>>> fruits = ['apple', 'pear', 'orange', 'banana', 'apple']
>>> print(fruits)
>>> fruits
['apple', 'pear', 'orange', 'banana', 'apple']

>>> print(len(fruits))
5

>>> print(f"the third fruit is: {fruits[2]}")
the third fruit is: orange

>>> print(f"the second and third fruits are: {fruits[1:3]}")
the second and third fruits are: ['pear', 'orange']

>>> print(f"the last fruit is: {fruits[-1]}")
the last fruit is: apple

>>> print(f"the second-last fruit is: {fruits[-2]}")
the second-last fruit is: banana

>>> print(f"the last three fruits are: {fruits[-3:]}")
the last three fruits are: ['orange', 'banana', 'apple']
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
    >>> fruits = ['apple', 'pear', 'orange', 'banana', 'apple']
    >>> fruitbag = {'apple', 'pear', 'orange', 'banana', 'apple'}
    >>> fruitbox = ('apple', 'pear', 'orange', 'banana', 'apple')

    >>> print(fruits)
    ['apple', 'pear', 'orange', 'banana']

    >>> print(fruitbox)
    ('apple', 'pear', 'orange', 'banana', 'apple')

    >>> print(fruitbag)
    {'banana', 'apple', 'pear', 'orange'}

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

1. Some people say that Arrays in other languages are Lists
in Python. Other people argue that Tuples are closer to Arrays.
    - a) Which statement is (more) correct?
    - b) Name two differences between Arrays and Lists?
        (1 Pt)
    - c) What are differences between a Python 2-dimensional List
        (List with Lists) and a *NumPy* Array *ndarray* (read the first
        [three paragraphs](https://numpy.org/doc/stable/user/whatisnumpy.html))?
        (1 Pt)

1. Draw sketches to visualize Python data structures:
*List*, *Set*, *Tuple*, *Dictionary* and *NumPy Array*. (1 Pt)


&nbsp;
### 3.) Challenge 3: Sorting Fruits

```py
>>> fruits = ['apple', 'pear', 'orange', 'banana', 'apple']

>>> f1 = sorted(fruits)
>>> print(f"{f1},\n{fruits}")
['apple', 'apple', 'banana', 'orange', 'pear'],
['apple', 'pear', 'orange', 'banana', 'apple']


>>> f2 = fruits.sort()
>>> print(f"{f2},\n{fruits}")
None,
['apple', 'apple', 'banana', 'orange', 'pear']
```

What is the difference between List-function *sort()* and built-in
function *sorted()*, see
[link](https://www.python-engineer.com/posts/sort-vs-sorted) (2 Pts)?


&nbsp;
### 4.) Challenge 4: Income Analysis
The US tax Income Revenue Service (IRS) annually 
publishes income statistics by ZIP codes (postal codes)
([reports](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi)).

For example, California ZIP Code
[93636](https://simplemaps.com/us-zips/93636)
is for *Madera* county, an agricultural region north of
Fresno in the Central Valley.
The income distribution in this county was for the tax year 2020:
```
income bracket:         number of tax returns
                        filed in bracket
[$1 to under $25,000]            1,800
[$25,000 to under $50,000]       1,380
[$50,000 to under $75,000]         980
[$75,000 to under $100,000]        830
[$100,000 to under $200,000]     1,660
[$200,000 or more, up to $10M]     550
```
In the bracket [$50,000 to under $75,000] of taxable income (exact to 74,999),
a total of 980 tax returns were filed, which means 980 tax payers reported
taxable income in this band.

We assume $10 million ($10M) as upper limit in the highest bracket.

A common statistical analysis is to compute:

- the *mean (average) income* and the

- the *median income* across all tax payers in *Madera* county.

For calculating the *mean income*, average the income within
each bracket.

For calculating the *median income*, consider a linear rising
income from the lower bound to the upper bound in the bracket
holding the *median income*.

Answer questions:

1. What is the difference between *mean (average)* and
*median* calculations?
    - Why are both indicators relevant?
    - When should one over the other be preferred?

1. Calculate manually the *mean* or *average* income for *Madera* county
(result: *$453,073* ).

1. Calculate manually the *median* income for *Madera* county
(result: *$60,714* ).

(3 Pts)


&nbsp;
### 5.) Challenge 5: Code Income Analysis

Write Python code to perform this income analysis for arbitray
ZIP regions.

Use file
<b>[income_tax_analysis.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/B_explore_python/income_tax_analysis.py)</b>
as template.

<b>Use pure Python</b>, no libraries such as *Pandas* or *Numpy* or
built-in library functions.

Think about following steps:

1. Chose a suitable Python data structure to represent tax data for
    a ZIP code.
    - Which data is relevant for the analysis?
    - How can data be structured?
    - Use only use Python structures: *list*, *set*, *tuple*, *dictionary*.
    (1 Pt)

1. Implement that data structure for the *Madera* data
    (fill data in code, no need to read `.xlsx`-files). (1 Pt)

1. Define two functions `mean_income(...)` and `median_income(...)`
    that take a data structure for a ZIP code as input and return
    respective numbers as results.

1. Define a function `number_of_returns(...)` that returns what the
    name suggests.

1. Implement these functions and demonstrate they return correct values.

1. Demonstrate analysis for other ZIP codes using IRS tax
[reports](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi).
Select a state (CA: California, IA: Iowa, NY: New York City), download
the `.xlsx` and navigate to ZIP codes for:
    - [94040](https://simplemaps.com/us-zips/94040) (Mountain View, CA),
    - [94304](https://simplemaps.com/us-zips/94304) (Palo Alto, CA),
    - [94027](https://simplemaps.com/us-zips/94027) (Atherton, CA),
    - [50860](https://simplemaps.com/us-zips/50860) (Redding, IA) and
    - [10023](https://simplemaps.com/us-zips/10023) (New York City, NY Upper West side). (1 Pt)

Develop (test, debug) code in
[income_tax_analysis.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/B_explore_python/income_tax_analysis.py)
in your IDE (*VS Code*, *PyCharm*, *Jupyter*, etc.).

Run the final result in a terminal (*Jupyter*: export Python file):

```sh
$ python income_tax_analysis.py
```

Results:
```
mean_income in Madera County, CA          is:    453,073 - median_income is:   60,714
mean_income in Mountain View, CA          is:  1,740,371 - median_income is:  114,820
mean_income in Palo Alto, CA              is:  2,077,038 - median_income is:  153,658
mean_income in Atherton, CA               is:  2,623,881 - median_income is:  354,087
mean_income in Redding, IA                is:     33,333 - median_income is:   31,249
mean_income in New York City, NY U West   is:  1,544,990 - median_income is:  104,774
```
(4 Pts)


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
