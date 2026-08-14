from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            if len(ans) == 0:
                ans.append(i)
            else:
                ans.append(ans[-1] + i)

        return ans


solution = Solution()
result = solution.runningSum([1, 2, 3, 4])

print(result)