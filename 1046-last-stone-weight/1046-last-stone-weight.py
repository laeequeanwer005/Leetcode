import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)
        while len(heap)>1:
            y= -heapq.heappop(heap)
            x= -heapq.heappop(heap)
            difference = y-x
            if difference >0:
                heapq.heappush(heap,-difference)
        if heap:
            return -heap[0]
        return 0