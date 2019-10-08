class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height) - 1
        max_area = 0

        # Leverage 2 pointers, and only increment l if the left height is smaller than the right height.
        # Otherwise, decrement r
        while l < r:
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
