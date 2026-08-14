from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(n):
            for j in range(i, i + 1):
                ans.append(nums[j])
                ans.append(nums[n + j])

        return ans


solution = Solution()

result = solution.shuffle([2, 5, 1, 3, 4, 7], 3)

print(result)