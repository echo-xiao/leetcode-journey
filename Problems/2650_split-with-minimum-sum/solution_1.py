class Solution:
    def splitNum(self, num: int) -> int:
        
        num = list(str(num))
        num.sort()

        num1 = []
        num2 = []
        for i in num:
            if len(num2) > len(num1):
                num1.append(i)
            else:
                num2.append(i)
        
        return int("".join(num1)) + int("".join(num2))
