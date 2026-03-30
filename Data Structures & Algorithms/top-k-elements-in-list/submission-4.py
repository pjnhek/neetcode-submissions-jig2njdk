class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_count = dict()
        for n in nums:
            dic_count[n] = dic_count.get(n, 0) + 1
        
        dic_count = sorted(dic_count.items(), key = lambda x: x[1])
        select = dic_count[-k:]
        x = []
        for i in select:
            x.append(i[0])
        return x
        
        
        
        