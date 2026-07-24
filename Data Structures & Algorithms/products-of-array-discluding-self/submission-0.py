class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6] example array
        n = len(nums) 
        leftpass, rightpass = [0] * n, [0] * n 

        # leftpass finds the product of all of everything to left of the element itself
        leftpass[0] = 1 
        for i in range(1, n):
            leftpass[i] = leftpass[i-1] * nums[i-1]
        #leftpass == [1, 1, 2, 8]
        
        rightpass[n-1] = 1
        for j in range(n-2, -1, -1):
            rightpass[j] = nums[j+1] * rightpass[j+1]
        #rightpass == [48, 24, 6, 1]
        
        return[leftpass[i] * rightpass[i] for i in range(n)]


