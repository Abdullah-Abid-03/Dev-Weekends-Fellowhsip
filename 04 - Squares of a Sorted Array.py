from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums



solution = Solution()

result = solution.sortedSquares([-4,-1,0,3,10])

print(result)

