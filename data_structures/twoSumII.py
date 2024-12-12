class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        n = len(numbers)
        right = n - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return [left, right]


if __name__ == "__main__":
    solution = Solution()
    case1 = { "target": 9, "collection": [2, 7, 11, 15]}
    case2 = { "target": 6, "collection": [2, 3, 4]}
    case3 = { "target": -1, "collection": [-1, 0]}

    print("Case 1: {}".format(solution.twoSum(case1["collection"], case1["target"])))
    print("Case 2: {}".format(solution.twoSum(case2["collection"], case2["target"])))
    print("Case 3: {}".format(solution.twoSum(case3["collection"], case3["target"])))