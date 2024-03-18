from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


# List of test cases
test_cases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

# Instance of the solution
solution = Solution()

# Loop through each test case
for nums, target in test_cases:
    response = solution.twoSum(nums, target)
    print(f"nums: {nums}, target: {target} => {response}")
