class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we want to find the target within the matrix
        # we can use binary search because the matrices are sorted
        # start at the top right corner
        # if the curr value is greater than the target, move left
        # if the curr value is less than the target, move down 
        
        # for each row m, we check the values n (columns) 
        
        # double binary search

        # check if matrix[0] is empty or not to avoid access issues 
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])

        # bst 1: find the target row
        top, bot = 0, ROWS - 1
        while top <= bot: 
            row = (top + bot) // 2
            # is the target value greater than the largest value in this row? 
            if target > matrix[row][-1]:
                top = row + 1
            # is the target value less than the least value in this row? 
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break
            
        # none of the rows have the target value
        if not (top <= bot): 
            return False

        # bst: find the target within this row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r: 
            m = (l + r) // 2
            if target > matrix[row][m]: 
                l = m + 1
            elif target < matrix[row][m]: 
                r = m - 1
            else:
                return True
        return False


        
        
        
        
        
        
        
        
        
        
        
        
        
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // COLS, mid % COLS
            if target < matrix[row][col]: 
                r = mid - 1
            elif target > matrix[row][col]: 
                l = mid + 1
            else: 
                return True
        return False
            