class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        def merge_max_counts(words):
            max_counts = Counter()
            for word in words:
                word_count = Counter(word)
                for char in word_count:
                    max_counts[char] = max(max_counts[char], word_count[char])
            return max_counts

        max_counts2 = merge_max_counts(words2)
        result = []

        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_counts2[char] for char in max_counts2):
                result.append(word)

        return result
