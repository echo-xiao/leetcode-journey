class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        

        curr = int(current[0:2]) * 60 + int(current[3:5])
        corr = int(correct[0:2]) * 60 + int(correct[3:5])
        diff1 = corr - curr
        

        h = diff1 // 60 
        diff2 = diff1 - h * 60

        k = diff2 // 15
        diff3 = diff2 - k * 15

        m = diff3 // 5
        diff4 = diff3 - m * 5

        t = diff4 // 1

        res = h + k + m + t
        return res
