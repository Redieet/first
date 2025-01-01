class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area and update max_area in a single step
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1

        return max_area


        