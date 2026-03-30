class Solution:

    def encode(self, strs: List[str]) -> str:
        word_len, string = [], ""
        for s in strs:
            word_len.append(len(s))
        for l in word_len:
            string = string + str(l) + ","
        string = string + "#"
        for s in strs:
            string = string + s
        return string
    def decode(self, s: str) -> List[str]:
        word_len, res, i = [], [], 0
        while s[i] != '#':
            str_len = ""
            while s[i] != ',':
                str_len += s[i]
                i += 1
            word_len.append(int(str_len))
            i += 1
        i += 1
        for x in word_len:
            res.append(s[i:i+x])
            i = i+x
        return res
