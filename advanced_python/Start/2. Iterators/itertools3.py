# Example file for Advanced Python by Joe Marini
# Itertools: dropwhile, takewhile, filterfalse

import itertools
import pprint
from dataclasses import dataclass


vals = [10, 20, 30, 40, 50, 40, 30, 25, 55, 45, 40, 30]

# dropwhile and takewhile will return values until
# a certain condition is met that stops them
def testFunction(x):
    return x < 40

# dropwhile() drops values until the predicate expression is True
print(list(itertools.dropwhile(testFunction, vals)))


# takewhile() is the opposite of dropwhile() - it returns values from
# the iterable while the predicate is True, then stops
print(list(itertools.takewhile(lambda x: x < 40, vals)))
print('#'*20, end="\n")


# filterfalse() returns elements from the iterable for which the predicate
# function returns False.
result = list(itertools.filterfalse(lambda x: x % 2 == 0, vals))
print(result)

# These functions can work on complex objects
@dataclass
class wcdata:
    game: str
    attendance: int
    team1: str
    team2: str
    score: str

worldcupdata = [
    wcdata("Final", 88966, "Argentina" , "France" , "3 (4) -- 3 (2)" ),
    wcdata("3rd Place", 44137, "Croatia" , "Morocco" , "2 -- 1" ),
    wcdata("Semifinal", 68294, "France" , "Morocco" , "2 -- 0" ),
    wcdata("Semifinal", 88966, "Argentina" , "Croatia" , "3 -- 0" ),
]


result = list(itertools.filterfalse(lambda x: x.attendance < 80_000, worldcupdata))
print(result)