class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row=len(grid)
        col=len(grid[0])

        c=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    c+=1

        if c==0:
            return 0
            
                 
        flag=[[False]*col for _ in range(row)]
        q=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j))
                    flag[i][j]=True
        
        

        

        pos=[(0,1),(0,-1),(1,0),(-1,0)]
        count=0
        while len(q)>0:
            count+=1
            n=len(q)
            for l in range(n):
                r,c=q.pop(0)
                for k in pos:
                    if k[0]+r>=row or k[0]+r<0:
                        continue
                    if k[1]+c>=col or k[1]+c<0:
                        continue
                    if grid[k[0]+r][k[1]+c]==0:
                        continue
                    if flag[k[0]+r][k[1]+c]==True:
                        continue
                    flag[k[0]+r][k[1]+c]=True
                    q.append((k[0]+r,k[1]+c))
        
        for i in range(row):
            for j in range(col):
                if flag[i][j]==False and grid[i][j]==1:
                    return -1
        return count-1
        