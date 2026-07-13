class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        longest = 0
        char_set = set()
        while r < len(s):
            while(s[r:r + 1] in char_set and l < r):
                char_set.remove(s[l])
                l+=1
                
            temp = r - l +1
            char_set.add(s[r])
            longest = max(longest, temp)
            r+=1
        return longest