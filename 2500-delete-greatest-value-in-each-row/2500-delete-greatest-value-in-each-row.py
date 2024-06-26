class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        ans = 0        
        for i in range(len(grid[0])):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j].pop()) 
            ans += max(tmp)  
        
        return ans

            