class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = dict()
        for word in strs:
            word_sort = "".join(sorted(word))
            if word_sort not in word_dic:
                word_dic[word_sort] = []
            word_dic[word_sort].append(word)
        return list(word_dic.values()) 