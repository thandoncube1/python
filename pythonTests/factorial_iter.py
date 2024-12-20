def factorial_iter(number: int, storage: list[int]):
    if number < 1:
        return number

    result: int = 1
    while number > 0:
        result *= number
        storage.append(result)
        number -= 1
    return result, storage


[total, getlist] = factorial_iter(5, [])

print(getlist)