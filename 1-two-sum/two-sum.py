class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        dictionary = {}
        
        for i in range(n):
            remainder = target - nums[i]

            if remainder in dictionary:
                return [dictionary[remainder], i]
            dictionary[nums[i]] =  i

    