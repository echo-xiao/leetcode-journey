class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        target = ''

        for char in s:
            if char != '9':
                target = char 
                break

        if target:
            maxS = s.replace(target, '9')
        else:
            maxS = s

        
        target = ''
        for char in s:
            if char != '0':
                target = char
                break
            
        if target:
            minS = s.replace(target, '0')
        else:
            minS = s

        return int(maxS) - int(minS)