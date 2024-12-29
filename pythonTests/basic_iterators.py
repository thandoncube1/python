# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
for d in days:
    print(d)

print("=="*10)
# use iter() to create an iterator over a collection
# the next() function retrieves the next value from an iterator
i  = iter(days)
print(next(i))
print(next(i))
print(next(i))
"""You have control over what is iterated over and values you need."""

# iterate using a function and a sentinel
with open("testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)