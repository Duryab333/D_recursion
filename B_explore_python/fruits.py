'''
Code for Assignment B: Explore Python
 - Challenge 1: Indexing Fruits
 - Challenge 2: Packaging Fruits
 - Challenge 3: Sorting Fruits
'''

fruits = ['apple', 'pear', 'orange', 'banana', 'apple']
fruitbag = {'apple', 'pear', 'orange', 'banana', 'apple'}
fruitbox = ('apple', 'pear', 'orange', 'banana', 'apple')


def index_fruits():
    # fruits = ['apple', 'pear', 'orange', 'banana']
    print(fruits)
    print(len(fruits))
    print(f"the third fruit is: {fruits[2]}")
    print(f"the second and third fruits are: {fruits[1:3]}")
    print(f"the last fruit is: {fruits[-1]}")
    print(f"the last two fruits are: {fruits[-2:]}")


def package_fruits():
    print(f'fruits:   {fruits}')
    print(f'fruitbox: {fruitbox}')
    print(f'fruitbag: {fruitbag}')
    print(fruits[1])
    print(fruitbox[1])
    # print(fruitbag[1])
    # 
    eric = {"name": "Eric", "salary": 5000, "birthday": "Sep 25 2001"}
    print(eric)
    print(eric["salary"])


def sort_fruits():
    f1 = sorted(fruits)
    print(f"{f1},\n{fruits}")
    f2 = fruits.sort()
    print(f"{f2},\n{fruits}")


if __name__ == '__main__':
    '''
    Main driver that runs when this file is executed by the Python interpreter.
    '''
    index_fruits()
    package_fruits()
    sort_fruits()
    # 
    # print(globals())
