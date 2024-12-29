# Example file for Advanced Python by Joe Marini


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


# use enumerate and zip together


# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
