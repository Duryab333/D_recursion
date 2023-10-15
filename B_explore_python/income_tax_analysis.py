'''
Code for Assignment B: Explore Python
 - Challenge 4: Income Analysis
 - Challenge 5: Code Income Analysis

Based on 2020 tax returns, income distribution in Madera County, CA, ZIP 93636 was:
#
income brackets:        number of tax returns
                        filed in brackets:
[$1 to under $25,000]             1,800
[$25,000 to under $50,000]        1,380
[$50,000 to under $75,000]          980
[$75,000 to under $100,000]         830
[$100,000 to under $200,000]      1,660
[$200,000 or more, up to $10M>]     550

Find more income distributions:
[93636](https://simplemaps.com/us-zips/93636) (Madera County, CA),
[94040](https://simplemaps.com/us-zips/94040) (Mountain View, CA),
[94304](https://simplemaps.com/us-zips/94304) (Palo Alto, CA),
[94027](https://simplemaps.com/us-zips/94027) (Atherton, CA),
[50860](https://simplemaps.com/us-zips/50860) (Redding, IA) and
[10023](https://simplemaps.com/us-zips/10023) (New York City, NY U West). (1 Pt)
'''

# design a data structure that stores information about a ZIP area
# that is relevant for mean/median tax analysis
zip_93636 = None
zip_94040 = None
zip_94304 = None
zip_94027 = None
zip_50860 = None
zip_10023 = None


# implement a function that calculates the mean income for a ZIP area
def mean_income(_zip) -> int:
    return 25000    # mock result, replace with correct result


# implement a function that calculates the median income for a ZIP area
def median_income(_zip) -> int:
    return 18500    # mock result, replace with correct result


# use function that prints analysis results for a ZIP area
def print_analysis(_zip):
    _county = 'Madera, CA'
    # -> "mean_income in Redding, IA is: 33,333 - median_income is: 31,249"
    print(
        f'mean_income in {_county:26} is: {mean_income(_zip):10,} - ' +
        f'median_income is: {median_income(_zip):8,}'
    )


# attempt to load solution module (ignore)
try:
    solution_module = 'income_tax_analysis_sol'
    mod = __import__(solution_module, globals(), locals(), [], 0)
    mean_income, median_income, print_analysis = mod.mean_income, mod.median_income, mod.print_analysis
    zip_93636, zip_94040, zip_94304, zip_94027, zip_50860, zip_10023 = \
        mod.zip_93636, mod.zip_94040, mod.zip_94304, mod.zip_94027, mod.zip_50860, mod.zip_10023
    print(f'solution module found: {solution_module}.py')
#
except ImportError:
    pass


if __name__ == '__main__':
    '''
    driver code that runs when this file is directly executed
    '''
    print_analysis(zip_93636)
    print_analysis(zip_94040)
    print_analysis(zip_94304)
    print_analysis(zip_94027)
    print_analysis(zip_50860)
    print_analysis(zip_10023)
