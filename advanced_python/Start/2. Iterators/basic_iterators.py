# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
for d in days:
    print(d)

# use iter() to create an iterator over a collection
# the next() function retrieves the next value from an iterator


# iterate using a function and a sentinel
