class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        for s_char in s:
            s_dic[s_char] = s_dic.get(s_char,0) + 1
        for t_char in t:
            t_dic[t_char] = t_dic.get(t_char, 0) + 1
        print(s_dic)
        print(t_dic)
        if s_dic == t_dic:
            return True
        else:
            return False