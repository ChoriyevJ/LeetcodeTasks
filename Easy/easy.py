from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def isPalindrome(self, x: int) -> bool:
        numbers = []
        if x < 0:
            return False
        while x > 0:
            dx = x % 10
            numbers.append(dx)
            x //= 10
        n = len(numbers)
        input(numbers)
        for i in range(n // 2):
            if numbers[i] != numbers[n - 1 - i]:
                return False
        return True

    def romanToInt(self, s: str) -> int:

        # XIIV

        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        last_letter = None
        same_letters = 1
        for letter in s.upper():

            result += romans[letter]
            if last_letter:
                if letter == last_letter:
                    same_letters += 1
                else:
                    if romans[letter] > romans[last_letter]:
                        result -= 2 * same_letters * romans[last_letter]
            last_letter = letter
        return result


