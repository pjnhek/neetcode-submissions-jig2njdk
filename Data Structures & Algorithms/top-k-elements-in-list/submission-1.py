class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dic = dict()
        for num in nums:
            num_dic[num] = num_dic.get(num, 0) + 1
        
        list_dic = list()
        for num, count in num_dic.items():
            list_dic.append([count, num])
        list_dic.sort()

        count = list()
        while len(count) < k:
            count.append(list_dic.pop()[1])
        return count
            
            
