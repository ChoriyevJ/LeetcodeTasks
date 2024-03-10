from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        result = []
        for i in range(len(index)):
            ind = index[i]
            value = nums[i]
            self.insert(result, ind, value)
        return result

    def insert(self, array: list, index: int, value: int):
        n = len(array)
        array.append(value)
        i = 0
        while index + i != n:
            array.append(array[index])
            del array[index]
            i += 1


print(Solution().createTargetArray(nums = [4, 1, 2, 4, 3, 2, 4, 0, 4, 1], index = [0, 1, 2, 0, 1, 2, 0, 1, 2, 3]))



