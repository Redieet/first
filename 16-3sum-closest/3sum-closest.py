from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to enable the two-pointer technique
        nums.sort()
        closest_sum = float('inf')  # Initialize with a large value

        for i in range(len(nums) - 2):
            # Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum only if necessary
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Early exit if the target sum is found
                if current_sum == target:
                    return target

                # Move pointers based on comparison with the target
                if current_sum < target:
                    left += 1
                    # Skip duplicate elements on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Skip duplicate elements on the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return closest_sum


