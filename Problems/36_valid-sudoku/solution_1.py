class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = []
        cols = []
        boxes = []
        
        for i in range(0, n):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for r in range(0, n):
            for c in range(0, n):
                val = board[r][c]
                if val == ".":
                    continue
                box = (r//3)*3 + c//3

                if val not in rows[r]: 
                    rows[r].add(val)
                else:
                    return False

                if val not in cols[c]: 
                    cols[c].add(val)
                else:
                    return False

                if val not in boxes[box]: 
                    boxes[box].add(val)
                else:
                    return False

        return True

