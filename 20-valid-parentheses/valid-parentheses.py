class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []  # Stack to keep track of opening brackets

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Check if the top of the stack matches the corresponding opening bracket
                top_element = stack.pop() if stack else '#'  # Use '#' as a dummy character for empty stack
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack

        