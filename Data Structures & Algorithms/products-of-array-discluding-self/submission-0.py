class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        containszero = False
        zerocount = 0
        mult = 1
        for x in nums:
            if x == 0:
                containszero = True
                zerocount += 1
                if(zerocount == 2):
                    break
            else:
                mult *= x
        ans = []
        if zerocount > 1:
            for x in nums:
                ans.append(0)
        else:
            for x in nums:
                if(x != 0 and containszero):
                    ans.append(0)
                elif x == 0:
                    ans.append(mult)
                else:
                    ans.append(int(mult/x))
        return ans