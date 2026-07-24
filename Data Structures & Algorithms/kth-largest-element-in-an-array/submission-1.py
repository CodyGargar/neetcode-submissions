class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        count = 0
        for i in reversed(nums):
            count+=1
            print(i)
            if count == k:
                return i