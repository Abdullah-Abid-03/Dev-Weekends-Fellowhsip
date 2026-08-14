from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_list = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count_list.append(count)
                count = 0
            count_list.append(count)

        count = max(count_list)
        return count




        

solution = Solution()

result = solution.findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1])

print(result)