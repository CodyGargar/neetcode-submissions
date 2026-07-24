import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            temp1 = -heapq.heappop(max_heap)
            temp2 = -heapq.heappop(max_heap)
            
            if temp1 > temp2:
                heapq.heappush(max_heap, -(temp1 - temp2))
            elif temp1 < temp2:
                heapq.heappush(max_heap, -(temp2 - temp1))
                
        return -max_heap[0] if max_heap else 0
