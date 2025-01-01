class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return [] 
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append("".join(current_combination))
                return
            possible_chars = digit_to_char[digits[index]]
            for char in possible_chars:
                current_combination.append(char)  # Choose
                backtrack(index + 1, current_combination)  # Explore
                current_combination.pop()  
        backtrack(0, [])
        return result
