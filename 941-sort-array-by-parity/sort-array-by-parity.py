class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
        n = len(nums)

        if n <= 1:
            return nums
        
        new_array = []
        new_array2 = []

        for indx in range(n):
            if nums[indx] % 2 == 0:
                new_array.append(nums[indx])
            else:
                new_array2.append(nums[indx])

        return new_array + new_array2
