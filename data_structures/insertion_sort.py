from random import shuffle


def insertion_sort(array: list, n: int):
    for i in range(1, n):
        key = array[i] # current element
        j = i - 1 # previous element
        while j >= 0 and key < array[j]:
            # move element to the left in relation to the next
            # element after the previous element.
            # Generally we are assigning element to the right with the
            # previous element.
            array[j + 1] = array[j]
            j -= 1
        # Then we assign the next element to be the (key) or current
        array[j + 1] = key


def main():
    numbers = [num for num in range(0, 20)]
    # shuffle the numbers
    shuffle(numbers)
    print("Shuffled: ", numbers)

    # Sort the numbers
    insertion_sort(numbers, len(numbers))

    # Print the numbers
    print("Sorted: ", numbers)


if __name__ == "__main__":
    main()