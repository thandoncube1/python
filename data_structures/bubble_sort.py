from random import shuffle


def bubble_sort(array: list, n: int) -> None:
    for _ in range(0, n):
        # initial loop just to iterate over all elements
        for i in range(0, n-1):
            # Loop for comparing until the second of last element in the array
            # This way is doesn't go out of range.
            if array[i] > array[i+1]:
                # Compare the current element with the next element in the list
                array[i], array[i+1] = array[i+1], array[i]
                # Swap the elements using the pattern matching operation.



def main():
    numbers = [num for num in range(0, 20)]
    shuffle(numbers)
    print("Shuffled: ", numbers)
    bubble_sort(numbers, len(numbers))
    print("Sorted: ", numbers)


if __name__ == "__main__":
    main()