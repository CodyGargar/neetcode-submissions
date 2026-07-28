class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        for i in (reversed(sorted(nums))):
            count+=1
            if count == k:
                return i