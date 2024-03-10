
class Solution:

    def reverse(self, x: int) -> int:
        _one = 1
        if x < 0:
            x *= -1
            _one = -1
        result = 0
        n = self.get_len(x)
        while x > 0:
            result += x % 10 * 10 ** (n - 1)
            x //= 10
            n -= 1
        if _one * result >= 2 * 10 ** 31 - 1 or _one * result <= -1 * (2 * 10 ** 31):
            return 0
        return _one * result

    def get_len(self, x: int) -> int:
        n = 0
        while x > 0:
            x //= 10
            n += 1
        return n


