import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            mid = (l + r) // 2
            temph = 0
            for p in piles:
                temph += (p + mid - 1) // mid
            if temph <= h:
                res = mid
                r = mid - 1
            elif temph > h:
                l = mid + 1
        return res
