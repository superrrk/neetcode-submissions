class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must have 1 - 9 without repetition 
        # each column must contain the digits 1 - 9 
        # each 3x3 subboxes need 1-9 

        # i want to return if the board is valid, without any 
        # contradictions 

        # hashset for each row, hashset for each column
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True



        