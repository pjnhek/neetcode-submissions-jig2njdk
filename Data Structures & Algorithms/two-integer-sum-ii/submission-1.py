class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_num = len(numbers)
        start = 0
        
        while start != len_num - 1:
            end = len_num - 1
            while start < end:
                if numbers[start] + numbers[end] == target:
                    return [start+1, end + 1]
                end -= 1
            start += 1
