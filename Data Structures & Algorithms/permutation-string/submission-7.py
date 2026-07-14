class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = "".join(sorted(s1))
        for x in range(len(s2) - len(s1)+1):
            if s1 == "".join(sorted(s2[x: x + len(s1)])):
                return True

        return False