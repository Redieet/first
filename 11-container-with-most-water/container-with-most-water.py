class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1  # Initialize two pointers
        max_area = 0  # Variable to store the maximum area

        while left < right:
            # Calculate the current area
            current_area = (right - left) * min(height[left], height[right])
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        