class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ans.append([strs[0]])
        appended = False
        for x in range(1, len(strs)):
            for y in range(len(ans)):
                if(self.isAnagram(strs[x], ans[y][0])):
                    ans[y].append(strs[x])
                    appended = True
            if(not appended):
                ans.append([strs[x]])
            appended = False
        return ans



    def isAnagram(self, s: str, t: str) -> bool:
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        return False