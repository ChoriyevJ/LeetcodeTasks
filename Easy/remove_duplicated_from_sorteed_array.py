from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        discount = 0
        i = 1

        while i < len(nums) - discount:

            if nums[i - 1] == nums[i]:
                nums.append(nums[i])
                discount += 1
                del nums[i]

            else:
                i += 1

        return i

print(Solution().removeDuplicates(nums=[1,]))