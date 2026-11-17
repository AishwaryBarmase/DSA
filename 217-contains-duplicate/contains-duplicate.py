class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
        # set_val = set()
        # for val in nums:
        #     if val not in set_val:
        #         set_val.add(val)
        #     else:
        #         return True
        # return False