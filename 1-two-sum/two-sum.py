class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for indx in range(len(nums)-1):
            for indx2 in range(indx+1, len(nums)):
                if nums[indx] + nums[indx2] == target:
                    return [indx, indx2]