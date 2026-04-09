class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0

        t = ""

        for c in s:
            if (c >= 'a' and c <= 'z') or (c>='A' and c < 'Z') or (c >= '0' and c <= '9'):
                t += c.capitalize()

        s = t
        j = len(s) - 1
        print(s)
        while i < j:    
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
        