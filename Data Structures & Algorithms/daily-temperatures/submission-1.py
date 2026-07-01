class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = [] # idx of days which we have not found a warmer temp for

        for i in range(n):
            curr_temp = temperatures[i]
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)

        return res

        
        