class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        heap = []
        for num in dic.keys():
            heapq.heappush(heap, (dic[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        
        
        
        