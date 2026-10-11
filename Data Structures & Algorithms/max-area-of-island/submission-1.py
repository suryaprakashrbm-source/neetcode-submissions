class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        flag=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def check(i,j):
            nonlocal flag
            if i<0 or j<0:
                return 0
            if (i>=len(grid) or j>=len(grid[0])) :
                return 0
            if flag[i][j] or grid[i][j]==0:
                return 0
            flag[i][j]=True 


            return 1+check(i+1,j)+check(i,j+1)+check(i-1,j)+check(i,j-1)
         
        

        
        maxval=0
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==1 and flag[i][j]==False :
                    maxval=max(check(i,j),maxval)
        return maxval