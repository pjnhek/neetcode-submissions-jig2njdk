class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        dic1 = dict()
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        for char1 in s:
            dic1[char1] = dic1.get(char1, 0) + 1
        print(dic, dic1)
        if dic == dic1:
            return True
        return False