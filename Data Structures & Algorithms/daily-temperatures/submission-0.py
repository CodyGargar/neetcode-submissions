class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for x in range(len(temperatures)):
            size = 0
            for y in range(x+1, len(temperatures)):
                
                if(temperatures[y] > temperatures[x]):
                    size+=1
                    break
                elif(y == len(temperatures) - 1):
                    size = 0
                else:
                    size+= 1
            
            ans.append(size)

        return ans
            