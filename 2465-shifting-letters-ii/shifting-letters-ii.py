class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
   
        s = list(s)
        n = len(s)

        net_shifts = [0] * (n + 1)
        

        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            net_shifts[start] += shift_value
            net_shifts[end + 1] -= shift_value
        

        for i in range(1, n):
            net_shifts[i] += net_shifts[i - 1]
    
        for i in range(n):
            shift = net_shifts[i]
            s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        
        return ''.join(s)
