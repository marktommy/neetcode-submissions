class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r, row in enumerate(board):
            for c, column in enumerate(row):
                v = board[r][c]
                if v == ".":
                    continue
                if v in rows[r] or v in cols[c] or v in squares[(r//3, c//3)]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                squares[(r//3, c//3)].add(v)
        return True        
        
        
