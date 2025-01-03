class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= total_sum - left_sum:
                count += 1
        
        return count

        