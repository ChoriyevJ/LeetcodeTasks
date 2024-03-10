from typing import List, Optional

from Medium.medium import ListNode


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
        for i in range(n // 2):
            if numbers[i] != numbers[n - 1 - i]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        dx = x
        length = 0
        numbers = []
        palindrome_number = 0
        while dx > 0:
            l = dx % 10
            length += 1
            dx //= 10
            numbers.append(l)
        print(length)
        print(numbers)
        for number in numbers:
            palindrome_number += number * 10 ** (length - 1)
            length -= 1
        print(palindrome_number)
        if palindrome_number == x:
            return True
        return False

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




