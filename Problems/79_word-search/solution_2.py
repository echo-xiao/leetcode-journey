class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.backtrack(board, word, i, j, 0):
                        return True
        return False

    def backtrack(self, board, word, r, c, idx):

        if idx == len(word):
            return True

        if (r < 0 or r >= len(board) or 
            c < 0 or c >= len(board[0]) or
            board[r][c] != word[idx]):
            return False

        tmp = board[r][c]
        board[r][c] = '#'

        found = (self.backtrack(board, word, r+1, c, idx+1) or 
                 self.backtrack(board, word, r-1, c, idx+1) or
                 self.backtrack(board, word, r, c+1, idx+1) or
                 self.backtrack(board, word, r, c-1, idx+1))

        board[r][c] = tmp
        return found