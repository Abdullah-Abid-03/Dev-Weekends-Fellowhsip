from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for i in gain:
            altitude += i
            highest = max(highest, altitude)

        return highest


solution = Solution()

result = solution.largestAltitude([-5, 1, 5, 0, -7])

print(result)