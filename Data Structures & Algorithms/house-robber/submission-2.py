class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        arr=[]

        arr.append(0)
        arr.append(nums[0])
        arr.append(nums[1])

        for i in range(2,len(nums)):
            print(i-2)
            arr.append(max(arr[i-1]+nums[i],arr[i-2]+nums[i]))
        return max(arr[len(arr)-1],arr[len(arr)-2])
