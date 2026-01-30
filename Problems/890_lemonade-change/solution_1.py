class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        
        rem5 = 0
        rem10 = 0
        
        for m in bills:

            if m == 5:
                rem5 += 1
                
            if m == 10:
                if rem5 <= 0:
                    return False
                rem5 -= 1
                rem10 += 1

            if m == 20:
                if rem5 > 0 and rem10 > 0:
                    rem5 -= 1
                    rem10 -= 1
                elif rem5 >= 3:
                    rem5 -= 3
                else:
                    return False      

        return True
