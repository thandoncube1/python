def bisection(L, target):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == target
    else:
        half = len(L) // 2
        if L[half] > target:
            return bisection(L[:half], target)
        else:
            return bisection(L[half:], target)


if __name__ == "__main__":
    result = bisection([2,3,4,5,6,7,8,9,23,54,64,123,543,2345,3451,4335,5423,12323], 64)
    print(result)