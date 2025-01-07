class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if any(word in other for other in words if word != other):
                result.append(word)
        return result

        