class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sud_dic = {}
        for i, n in enumerate(board):
            inner_dic = {}
            for cell_idx, cell in enumerate(n):
                inner_dic[cell_idx] = cell
            sud_dic[i] = inner_dic
        # first check - iterate thru each row to find dups
        for k, v in sud_dic.items():
            val_list = []
            for val in v.values():
                try:
                    val_list.append(int(val))
                except:
                    continue
            if len(set(val_list)) == len(val_list):
                print(set(val_list))
                print(val_list)
                continue
            else:
                return False
        # second check - iterate thru each val in col to find dup
        for k in sud_dic.keys():
            val_list = []
            for v1 in sud_dic.values():
                try:
                    val_list.append(int(v1[k]))
                except:
                    continue
            if len(set(val_list)) == len(val_list):
                continue
            else:
                return False
        # third check - iterate thru each box to find dups
        for k in sud_dic.keys():
            val_list = []
            for i in range(3):
                for j in range(3):
                    row = (k//3) * 3 + i
                    col = (k%3) * 3 + j
                    try:
                        val_list.append(int(sud_dic[row][col]))
                    except:
                        continue
            if len(val_list) == len(set(val_list)):
                continue
            else:
                return False
        return True


