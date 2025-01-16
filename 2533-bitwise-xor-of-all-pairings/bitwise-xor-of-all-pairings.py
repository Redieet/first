class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculate the bitwise XOR of all pairings between elements of nums1 and nums2.
        
        Args:
        nums1: List[int] - First list of non-negative integers.
        nums2: List[int] - Second list of non-negative integers.
        
        Returns:
        int - The XOR of all pairings between nums1 and nums2.
        """
        # Initialize XOR values for nums1 and nums2
        xor_nums1 = 0
        xor_nums2 = 0

        # Calculate the XOR of all elements in nums1
        for num in nums1:
            xor_nums1 ^= num

        # Calculate the XOR of all elements in nums2
        for num in nums2:
            xor_nums2 ^= num

        # Determine the size of nums1 and nums2
        len1, len2 = len(nums1), len(nums2)

        # The total XOR will depend on the parity (odd/even) of the lengths of nums1 and nums2
        result = 0

        # If nums2 contributes odd times to the result, include xor_nums1
        if len2 % 2 == 1:
            result ^= xor_nums1

        # If nums1 contributes odd times to the result, include xor_nums2
        if len1 % 2 == 1:
            result ^= xor_nums2

        return result

        