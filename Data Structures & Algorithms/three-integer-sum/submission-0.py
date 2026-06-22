class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num_map = {num: i for i, num in enumerate(nums)}
        for x in range(len(nums) -2):
            for y in range(x+1, len(nums)-1):
                s = -(nums[x] + nums[y])
                if s in num_map and num_map[s] > y :
                    ans.add(tuple(sorted([nums[x], nums[y], s])))

        return [list(a) for a in ans]