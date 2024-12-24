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



# Merge sort - 1. Merge
def merge(left: list, right: list):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print('Merge: ' + str(left) + ' & ' + str(right))
    return result

"""
    Divide the list successively into halves
    Depth first such that conquer smallest pieces down one branch
    first before moving to larger pieces.
"""
def merge_sort(L: list):
    print('Merge Sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


arrayList = [3,6,8,9,3,1,4,5,12,7,2]
# bubble_sort(arrayList)
# selection_sort(arrayList)
result = merge_sort(arrayList)
# print(arrayList)
print(result)