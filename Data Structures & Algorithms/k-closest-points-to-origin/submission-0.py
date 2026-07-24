class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_heap = []
        
        for i in points:
            heapq.heappush(my_heap, (math.sqrt(i[0]**2 + i[1]**2) , i))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(my_heap)[1])
        return ans