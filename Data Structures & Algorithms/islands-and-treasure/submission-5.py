class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row=len(grid)
        col=len(grid[0])

        def check():

            q=[]
            flag=[[False]*col for _ in range(row)]
            for i in range(row):
                for j in range(col):

                    if grid[i][j]==0:
                        q.append((i,j))
                        flag[i][j]=True


            
            count=0
            while q:
                n=len(q)
                # print(q)
                count+=1
                

                for k in range(n):
                    r,c=q.pop(0)
                    # print(r,c)
                    if r+1 <row and flag[r+1][c]==False and grid[r+1][c]!=-1:
                        if grid[r+1][c]>count:
                            grid[r+1][c]=count
                        flag[r+1][c]=True
                        q.append((r+1,c))

                    if r-1 >=0 and flag[r-1][c]==False and grid[r-1][c]!=-1:
                        if grid[r-1][c]>count:
                            grid[r-1][c] = count
                        flag[r-1][c]=True
                        q.append((r-1,c))

                    if c+1 <col and flag[r][c+1]==False and grid[r][c+1]!=-1:
                        if grid[r][c+1]>count:
                            grid[r][c+1] = count
                        flag[r][c+1]=True
                        q.append((r,c+1))


                    if c-1 >=0 and flag[r][c-1]==False and grid[r][c-1]!=-1:
                        if grid[r][c-1]>count:
                            grid[r][c-1] = count
                        flag[r][c-1]=True
                        q.append((r,c-1))
                # print(grid)

            return 2147483647


        

        check()
                    # print(grid)




            