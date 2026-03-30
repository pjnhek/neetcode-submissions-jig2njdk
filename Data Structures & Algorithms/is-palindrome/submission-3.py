class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().split(' ')
        s = ''.join(s)
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[end].isalnum():
                end -= 1
            elif not s[start].isalnum():
                start += 1
            elif s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True         