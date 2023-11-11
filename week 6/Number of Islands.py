class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        def solve(i,j):
            if i < 0 or j < 0  or i >= r or j >= c:
                return 
            if grid[i][j] == "0" :
                return
            grid[i][j] = '0'

            solve(i-1, j)

            solve(i+1, j)

            solve(i, j+1)
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    solve(i,j)
                    count += 1
        
        return count