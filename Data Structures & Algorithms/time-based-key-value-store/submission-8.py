class TimeMap:

    def __init__(self):
        self.time_dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dic:
            self.time_dic[key] = []
        self.time_dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dic:
            return ""
        val_list = self.time_dic[key]
        l, r = 0, len(val_list)-1
        ans = val_list[l][0]
        if ans > timestamp:
            return ""
        while l <= r:
            m = l + ((r-l)//2)
            if val_list[m][0] == timestamp:
                return val_list[m][1]
            elif val_list[m][0] < timestamp:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return val_list[ans][1]  

        
        