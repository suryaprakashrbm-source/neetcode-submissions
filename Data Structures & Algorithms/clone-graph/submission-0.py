"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.ans=[]
        self.count=1
        self.hashmap={}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        a=[node]
        temphash={}
        while a:
            t=a.pop()
            if t.val not in self.hashmap:
                self.hashmap[t.val]=Node(t.val,[])
                temphash[t.val]=t.neighbors 
                for i in t.neighbors:
                    a.append(i)

            
                
        # print(self.hashmap)
        # print(temphash)
        for i in range(1,len(self.hashmap)+1):
            mainnode=self.hashmap[i]
            temp=temphash[mainnode.val]
            for j in temp:
                newtemp=self.hashmap[j.val]
                mainnode.neighbors.append(newtemp)
            self.ans.append(mainnode)
        # print(self.ans)
        


        return self.ans[0]


        