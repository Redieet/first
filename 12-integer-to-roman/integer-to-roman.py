class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the Roman numeral mappings
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        result = []
        
        # Iterate through each value-symbol pair
        for value, symbol in value_symbols:
            if num == 0:
                break
            count, num = divmod(num, value)  # Determine how many of the current value fit into num
            result.append(symbol * count)  # Append the corresponding Roman symbols
        
        return ''.join(result)

        