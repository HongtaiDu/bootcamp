class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        def minimumSum(row, col):
            if(row < 0 or col < 0): 
                return float('inf')
            if (row, col) == (0, 0): 
                return grid[0][0]
            if (row, col) in cache: 
                return cache[(row, col)]
            else:
                cache[(row, col)] = grid[row][col] + min(minimumSum(row - 1, col), minimumSum(row, col - 1))
                return cache[(row, col)]
        return minimumSum(len(grid) - 1, len(grid[0]) - 1)