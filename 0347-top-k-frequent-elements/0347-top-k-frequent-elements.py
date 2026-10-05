class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            frequency[num]=frequency.get(num,0)+1
        heap = []
        for num,count in frequency.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count , num in heap]