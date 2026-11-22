class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n

        start = 1

        for ele in range(2, n):
            if nums[start-1] != nums[ele]:
                start += 1
                nums[start] = nums[ele] 
        
        return start+1
