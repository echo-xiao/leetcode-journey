class Solution:
    results: List[str]
    leds: List[tuple]
    target_count: int

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.results = []
        self.leds = [
            (1, "H"), (2, "H"), (4, "H"), (8, "H"),
            (1, "M"), (2, "M"), (4, "M"), (8, "M"), (16, "M"), (32, "M")
        ]
        self.target_count = turnedOn
        self._backtrack(0, 0, 0, 0)
        return self.results

    def _backtrack(self, start_index: int, count: int, hour: int, minute: int):

        if hour > 11 or minute > 59:
            return

        if count == self.target_count:
            self.results.append(format_time(hour, minute))
            return 

        for i in range(start_index, 10):
            val, type = self.leds[i]
            
            if type == "H":
                self._backtrack(i + 1, count + 1, hour + val, minute)
            else:
                self._backtrack(i + 1, count + 1, hour, minute + val)
            


from typing import List

def format_time(hour: int, minute: int) -> str:
    return f"{hour}:{minute:02d}"