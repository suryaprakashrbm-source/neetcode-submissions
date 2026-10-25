class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.length=0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.length+=1
        self.arr.sort()
        # print(self.arr)

    def findMedian(self) -> float:
        
        if self.length%2 == 0 :
            return (self.arr[self.length//2]+self.arr[(self.length//2)-1])/2
        else:
            # print(math.ceil(self.length/2)-1)
            return self.arr[self.length//2]
        
        