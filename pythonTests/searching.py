# Bubble sort
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                swap = False
                L[j], L[j - 1] = L[j - 1], L[j]


# Selection sort
""" select the smallest in the list and put it at thhe front of the list """
def selection_sort(L):
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[i], L[suffixStart] = L[suffixStart], L[i]
        suffixStart += 1



arrayList = [3,6,8,9,3,1,4,5,12,7,2]
# bubble_sort(arrayList)
selection_sort(arrayList)
print(arrayList)