
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = self.binary_to_ten(a) + self.binary_to_ten(b)
        return self.ten_to_binary(result)

    def reverse(self, string):
        new_string = ""
        i = 0
        while i < len(string):
            new_string += string[len(string) - 1 - i]
            i += 1
        return new_string

    def binary_to_ten(self, binary):
        result = 0
        i = 0
        for item in binary:
            if int(item) > 0:
                result += 2 ** (len(binary) - 1 - i)
            i += 1
        return result

    def ten_to_binary(self, number):
        result = ""
        while number >= 1:
            x = number % 2
            number //= 2
            result += str(x)
        return self.reverse(result)


print(Solution().addBinary("0", "0"))

