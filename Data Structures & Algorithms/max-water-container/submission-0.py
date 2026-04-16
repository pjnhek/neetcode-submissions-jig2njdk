class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # to get the area we need to take height x length
        # for the height, we want the min height between 
        # two h[i]s and for the length its just the diff
        # between the two h[i]s calc using the idx
        area = 0
        for i in range(len(heights)-1):
            right = i + 1
            while right <= len(heights)-1:
                height = min(heights[i], heights[right])
                length = right - i
                new_area = height * length
                if new_area > area:
                    area = new_area
                right += 1
        return area