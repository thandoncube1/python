# Exponential Complexity Problem
def genSubsets(L):
    res = [] # Not really important for now
    if len(L) == 0:
        return [[]] # List of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # Create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
        return smaller + new # Combine those with last element and those without