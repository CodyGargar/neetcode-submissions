class Solution:
    
    ans = set()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = set() 
        self.helper([], nums)
        return [list(item) for item in self.ans]

    def helper(self, temp, nums):
        if not nums:
            self.ans.add(tuple(sorted(temp)))
            return
            
        temporary = nums[0]
        remaining_nums = nums[1:]
        
        self.helper(temp + [temporary], remaining_nums)
        self.helper(temp, remaining_nums)