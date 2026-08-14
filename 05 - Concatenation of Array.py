from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums



solution = Solution()

result = solution.getConcatenation([1,2,1])

print(result)