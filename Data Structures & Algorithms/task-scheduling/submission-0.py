class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mo = Counter(tasks)
        my_heap = []

        for obj, count in mo.items():
            heapq.heappush(my_heap, (-count, obj))
        cycles = 0

        while(my_heap):
            temp = []
            for i in range(n+1):
                if(my_heap):
                    count, obj = heapq.heappop(my_heap)
                    count += 1 
                    print(i, obj)
                    if(count < 0):
                        temp.append([count, obj])
                    cycles += 1
                elif temp:
                    cycles += (n-i + 1)
                    for _ in range(n-i + 1):
                        print("idle")
                    break
            
            for count, obj in temp:
                heapq.heappush(my_heap, (count, obj))

            
        return cycles

                

                