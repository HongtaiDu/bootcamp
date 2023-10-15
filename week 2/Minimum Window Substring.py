class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size =  len(nums)
        minn  = -1 
        for i in range(0,size) :
            for j in range(i,size) :
                if nums[i] > nums[j] :
                    temp  = nums[i] 
                    nums[i] = nums[j]
                    nums[j] = temp 
                else :
                    continue 
        print(nums)