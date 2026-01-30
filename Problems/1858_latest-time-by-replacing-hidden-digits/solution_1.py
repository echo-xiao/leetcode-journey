class Solution:
    def maximumTime(self, time: str) -> str:
        hh = list(time[0:2])
        mm = list(time[3:])

        if hh[0] == '?' and hh[1] == '?':
            hh = '23'

        if mm[0] == '?':
            mm[0] = '5'

        if mm[1] == '?':
            mm[1] = '9'

        if hh[0] == '0' and hh[1] == '?':
            hh[1] = '9'

        if hh[0] == '1' and hh[1] == '?':
            hh[1] = '9'

        if hh[0] == '2' and hh[1] == '?':    
            hh[1] = '3'

        if hh[0] == '?' and int(hh[1]) <= 3:
            hh[0] = '2'
        
        if hh[0] == '?' and int(hh[1]) <= 9:
            hh[0] = '1'
        


        shh = "".join(hh)
        smm = "".join(mm)
        return shh + ":" + smm