class Solution:
    found_nodes: List[str]  
    leds: List[tuple]
    target_depth: int

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.found_nodes = []
        self.leds = [
            (1, "H"), (2, "H"), (4, "H"), (8, "H"),
            (1, "M"), (2, "M"), (4, "M"), (8, "M"), (16, "M"), (32, "M")
        ]
        self.target_depth = turnedOn
        self._dfs(0, 0, 0, 0)
        return self.found_nodes

    def _dfs(self, current_node_index: int, depth: int, hour: int, minute: int):

        if hour > 11 or minute > 59:
            return

        if depth == self.target_depth:
            self.found_nodes.append(format_time(hour, minute))
            return

        for i in range(current_node_index, 10):
            val, type = self.leds[i]
            
            if type == "H":
                self._dfs(i + 1, depth + 1, hour + val, minute)
            else:
                self._dfs(i + 1, depth + 1, hour, minute + val)

from typing import List

def format_time(hour: int, minute: int) -> str:
    return f"{hour}:{minute:02d}"
