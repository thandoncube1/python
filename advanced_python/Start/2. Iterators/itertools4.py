# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits)) # Instead of using a nested for loop
# print(len(deck))
# print(deck)

# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
# print(list(result))

# combinations() will create combinations of a given length with no repeats
result = itertools.combinations("ABCD", 2)
# print(list(result))
# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement("ABCD", 2)
print(list(result))

numbers = [[43, 2, 77, 48, 24, 9, 3, 65, 41, 42, 10, 75, 14, 69, 61], [20, 47, 69, 38, 2, 49, 76, 42, 81, 34, 10, 47, 76, 85, 81, 72], [92, 46, 25, 61, 75, 40, 87, 9, 52, 77, 0, 11, 25], [48, 74, 81, 71, 32, 82, 39, 74, 37, 72, 15], [8, 26, 12, 71, 5, 83, 75, 30, 34, 77]]

print("Maximum: ", max(itertools.chain.from_iterable(numbers)))
