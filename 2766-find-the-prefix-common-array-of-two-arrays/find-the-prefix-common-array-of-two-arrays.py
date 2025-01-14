from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = set()  # Set to track seen elements
        common_count = 0  # Counter for common elements
        result = []

        for i in range(n):
            # Add current elements from A and B to the seen set
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
            
            # Append the current count to the result
            result.append(common_count)
        
        return result

        