from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target <= nums[len(nums) - 1 - i]:
                continue
            else:
                return len(nums) - i
        return 0


print(Solution().searchInsert([1, 3, 5, 6], target=5))
