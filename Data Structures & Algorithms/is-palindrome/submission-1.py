class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        s = "".join(s.split(" "))
        print(s)
        if s == s[::-1]:
            return True
        return False