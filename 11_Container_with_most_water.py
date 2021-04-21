import math
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        a_point = 0
        b_point = n-1
        max_vol = 0
        while a_point<b_point:
            if min(height[a_point],height[b_point]) == height[a_point]:
                vol = height[a_point]*abs(b_point-a_point)
                a_point+=1
            elif min(height[a_point],height[b_point]) == height[b_point]:
                vol = height[b_point]*abs(b_point-a_point)
                b_point-=1
            if vol>max_vol:
                max_vol = vol
        return max_vol
