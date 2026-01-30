class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        
        n = len(code)
        next_win = sum(code[1: (k % n) + 1]) + sum(code[:]) * (k // n)
        befr_win = sum(code[n - (abs(k) % n): n]) + sum(code[:]) * (abs(k) // n)
        arr = [0] * n
        
        if k == 0:
            arr[0] = 0
        elif k > 0:
            arr[0] = next_win
        elif k < 0:
            arr[0] = befr_win
        

        for i in range(1, len(code)):
            if k == 0:
                arr[i] = 0
            elif k > 0:
                next_win = next_win + code[(i + k) % n] - code[i]
                arr[i] = next_win
            elif k < 0:
                befr_win = befr_win + code[i-1] - code[i - 1 - (abs(k) % n)]
                arr[i] = befr_win
        return arr