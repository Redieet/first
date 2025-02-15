class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n

        # Pass from left to right
        count = 0
        operations = 0
        for i in range(n):
            answer[i] += operations
            count += int(boxes[i])
            operations += count

        # Pass from right to left
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            count += int(boxes[i])
            operations += count

        return answer

        