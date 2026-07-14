class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count1 = {}
        for c in t:
            count1[c] = 1 + count1.get(c, 0)
        need = len(t)
        smallest = len(s) + 1
        ans = ""
        
        for i in range(len(s)):
            if smallest == len(t):  # can't beat this, stop entirely
                break
            count2, cur = {}, 0
            for j in range(i, len(s)):
                c = s[j]
                if c not in count1:
                    continue  # skip chars that can't matter
                count2[c] = 1 + count2.get(c, 0)
                if count1[c] >= count2[c]:
                    cur += 1
                if cur == need:
                    if j - i + 1 < smallest:
                        smallest = j - i + 1
                        ans = s[i:j+1]
                    break
        return ans
