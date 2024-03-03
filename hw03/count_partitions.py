from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = int((n * (n + 1)) / 2)
        given_sum = sum([x for x in nums])
        return actual_sum - given_sum


assert Solution().missingNumber([3, 0, 1]) == 2
assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert Solution().missingNumber([0, 1]) == 2
