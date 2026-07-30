
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recursion(nums, [])
        return self.result

    def recursion(self, nums, res):
        if not nums:
            self.result.append(res[:])
            return

        nums_copy = nums[:]
        temp = nums_copy.pop()
        
        self.recursion(nums_copy, res)
        self.recursion(nums_copy, res + [temp])
