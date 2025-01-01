from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer technique
        nums.sort()
        closest_sum = float('inf')  # Initialize with a large value

        for i in range(len(nums) - 2):
            # Use two pointers to find the closest sum for nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the closest sum if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # If the current sum equals the target, return immediately
                if current_sum == target:
                    return current_sum

                # Adjust the pointers based on the sum comparison
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
