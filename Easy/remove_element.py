from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        left_index = 0
        right_index = len(nums) - 1
        while left_index < len(nums):

            if right_index < left_index:
                break

            if nums[left_index] == val:
                if nums[right_index] != val:
                    a = nums[left_index] + nums[right_index]
                    nums[right_index] = a - nums[right_index]
                    nums[left_index] = a - nums[right_index]
                    result += 1
                else:
                    left_index -= 1
                right_index -= 1
            left_index += 1

        print(nums)
        return left_index


sol = Solution().removeElement([0,1,2,2,3,0,4,2], 2)
print(sol)
