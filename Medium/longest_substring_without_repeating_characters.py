
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        highlest = ""
        for k in range(len(s)):
            letters = s[k]
            for item in range(k + 1, len(s)):
                if s[item] not in letters:
                    letters += s[item]
                else:
                    break
            if len(highlest) == 0:
                highlest = letters
            elif len(highlest) < len(letters):
                highlest = letters

        return len(highlest)


    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_len = 0

        for k in range(len(s)):
            letters = ''
            current_len = 0
            for item in range(k, len(s)):
                if s[item] not in letters:
                    letters += s[item]
                    current_len += 1
                    if max_len < current_len:
                        max_len = current_len
                else:
                    if max_len == 0:
                        max_len = current_len
                    else:
                        if max_len < current_len:
                            max_len = current_len
                    break

        return max_len


s = Solution().lengthOfLongestSubstring("1@1 @#1")
print(s)


