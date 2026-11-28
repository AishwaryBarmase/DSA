class Solution:
    def sortColors(self, nums: list[int]) -> None:
        
        n = len(nums)
        right = n-1
        left = 0
        i = 0
        while i<= right:

            if nums[i] == 1:
                i +=1
            elif nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            