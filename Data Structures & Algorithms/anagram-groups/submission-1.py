class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = dict()
        for string in strs:
            sorted_word = ''.join(sorted(string))
            if not word_dic.get(sorted_word):
                word_dic[sorted_word] = [string]
            else:
                word_dic[sorted_word] += [string]
        return list(word_dic.values())


