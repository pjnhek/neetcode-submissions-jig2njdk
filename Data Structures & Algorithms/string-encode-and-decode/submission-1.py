class Solution:

    def encode(self, strs: List[str]) -> str:
        size, res = [], ""
        for s in strs:
            size.append(len(s))
        for sz in size:
            res = res+str(sz)
            res = res+","
        res = res+"#"
        for ss in strs:
            res = res+ss
        return res

    def decode(self, s: str) -> List[str]:
        word, size, count = [], [], 0
        while s[count] != "#":
            curr = ""
            while s[count] != ",":
                curr = curr+s[count]
                count += 1
            size.append(int(curr))    
            count += 1
        count += 1
        for sz in size:
            word.append(s[count: count + sz])
            count += sz
        return word

