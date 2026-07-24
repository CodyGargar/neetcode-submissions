
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Invert weights to simulate a Max-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop the two largest stones (remember they are negative)
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # If they are not equal, push the difference back
            if stone1 != stone2:
                # e.g., -8 - (-7) = -1
                heapq.heappush(max_heap, stone1 - stone2)

        # If 1 stone remains, turn it back to positive. Otherwise, return 0.
        return -max_heap[0] if max_heap else 0
