class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = [nums[0]]

        for indx in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[indx])

        return running_sum 