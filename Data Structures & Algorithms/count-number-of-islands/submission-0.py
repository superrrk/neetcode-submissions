class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input validation 
        if not grid: 
            return 0 

        # get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            q = collections.deque()
            visit.add((r,c)) # add as a tuple
            q.append((r,c))

            while q: # while q is not empty, expand island
                row, col = q.popleft()
                directions = [[1, 0], [-1,0], [0, 1], [0, -1]] #l r u d

                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    # check if pos is in bounds
                    if ((r) in range(rows) and
                    (c) in range(cols) and 
                    grid[r][c] == "1" and 
                    (r, c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        # visit every position in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # action: visiting a 1
                # - traverse and mark visited
                if grid[r][c] == "1" and (r, c) not in visit: # strings not integer values
                    dfs(r, c)
                    islands += 1

        return islands