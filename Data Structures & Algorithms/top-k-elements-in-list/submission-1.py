class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numlist = []
        numlist.append([nums[0]])
        appended = False
        for x in range(1,len(nums)):
            for y in range(len(numlist)):
                if(nums[x] == numlist[y][0]):
                    numlist[y].append(nums[x])
                    appended = True
            if(not appended):
                numlist.append([nums[x]])
            appended = False
        ans = []
        for x in range(k):
            largest = -1
            count = -99
            index = -1
            for y in range(len(numlist)):
                if(len(numlist[y]) > count):
                    count = len(numlist[y])
                    largest = numlist[y][0]
                    index = y
            numlist.pop(index)
            ans.append(largest)
        
        return ans
