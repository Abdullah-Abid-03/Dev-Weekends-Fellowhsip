from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        for x in range(k):
            last = nums[len(nums) - 1]

            # Move elements one position to the right
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]

            # Put last element at index 0
            nums[0] = last


solution = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]

solution.rotate(nums, 3)

print(nums)