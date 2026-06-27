class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_dic = {}
        for n in nums:
            c_dic[n] = c_dic.get(n, 0) + 1
        
        print(c_dic)
        o_list = [[] for _ in range(len(nums)+1)]
        for num, count in c_dic.items():
            o_list[count].append(num)
            
        print(o_list)
        res = []
        for i in range(len(o_list)-1, 0, -1):
            for val in o_list[i]:
                if len(res) == k:
                    break
                res.append(val)
                
        return res
