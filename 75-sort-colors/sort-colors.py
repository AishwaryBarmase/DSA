class Solution:
    def sortColors(self, nums: list[int]) -> None:
        
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        