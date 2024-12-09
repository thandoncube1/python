from random import shuffle


def bubble_sort(array: list, n: int) -> None:
    for _ in range(0, n):
        for i in range(0, n-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array


def main():
    numbers = [num for num in range(0, 20)]
    shuffle(numbers)
    print("Shuffled: ", numbers)
    bubble_sort(numbers, len(numbers))
    print("Sorted: ", numbers)


if __name__ == "__main__":
    main()