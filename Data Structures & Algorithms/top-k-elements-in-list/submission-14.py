class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = [[] for i in range(len(nums)+1)]
        
        count_dic = {}
        
        for n in nums:
            count_dic[n] = count_dic.get(n, 0) + 1
        
        for num, count in count_dic.items():
            freq_nums[count].append(num)
        
        # count_dic = {1:1, 2:2, 3:3}
        # freq_nums = [[], [1], [2], [3], [], [], []]
        print(freq_nums)
        res = []

        for i in range(len(freq_nums)-1, 0, -1):
            for val in freq_nums[i]:
                if len(res) == k:
                    break
                res.append(val)
                
        return res     
