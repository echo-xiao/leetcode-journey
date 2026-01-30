
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.arr = [(1, "H"), (2, "H"), (4, "H"), (8, "H"),
                    (1, "M"), (2, "M"), (4, "M"), (8, "M"), (16, "M"), (32, "M")]


        self.turnedOn = turnedOn
        self.res = []
        self.backtrack(0, 0, 0, 0)
        return self.res



    def backtrack(self, idx: int, lights: int, hours: int, minutes: int):

        if hours > 11 or minutes > 59:
            return 

        if lights == self.turnedOn:
            self.res.append(f"{hours}:{minutes:02d}")
            return

        for idx in range(idx, 10):
            
            val, tag = self.arr[idx]
            
            if tag == 'H':
                self.backtrack(idx+1, lights+1, hours+val, minutes)
            else:
                self.backtrack(idx+1, lights+1, hours, minutes+val)