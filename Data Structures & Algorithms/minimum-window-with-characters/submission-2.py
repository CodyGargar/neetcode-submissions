class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count1 = {}
        for c in t:
            count1[c] = 1 + count1.get(c, 0)
        need = len(t)
        smallest = 1000
        ans = ""
        
        for i in range(len(s)):
            count2, cur = {}, 0
            for j in range(i, len(s)):
                count2[s[j]] = 1 + count2.get(s[j], 0)
                if count1.get(s[j], 0) == count2[s[j]]:
                    cur += count2[s[j]]
                if cur == need:
                    if j-i+1 < smallest:
                        smallest = j - i + 1
                        ans = s[i: j+1]
                        break
        return ans
