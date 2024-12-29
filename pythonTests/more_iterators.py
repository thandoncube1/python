# Example file for Advanced Python by Joe Marini

import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

for d in range(len(days)):
    pass
    # print(d+1, days[d])

# the enumerate function
for i, d in enumerate(days, start=1):
    print(i, d)

# use zip to combine sequences
for d in zip(days, daysFr):
    print(d)

print("="*20)
# use enumerate and zip together
for i, d in enumerate(zip(days, daysFr), start=1):
    print(i, d[0], "=", d[1], "in French")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"

result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result: ")
[print(item, end="\n") for item in result]