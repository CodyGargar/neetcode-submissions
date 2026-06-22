class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in range(len(numbers) - 1):
            for y in range(x + 1, len(numbers)):
                if( y > x and numbers[x] + numbers[y] == target):
                    return [x+1,y +1]