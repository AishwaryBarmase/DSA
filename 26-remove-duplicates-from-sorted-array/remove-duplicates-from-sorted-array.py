class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        n = len(nums)

        start = 0

        for ele in range(1, n):
            if nums[ele] != nums[start]:
                start += 1
                nums[start] = nums[ele]
        
        return start + 1

        
            