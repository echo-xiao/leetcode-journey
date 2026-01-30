class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        res = []
        for i in range(0, len(number)):
            if number[i] == digit:
                res.append(number[0:i]+number[i+1:])
        return max(res)
                
