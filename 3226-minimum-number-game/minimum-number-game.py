class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            first_ele = min(nums)
            nums.remove(first_ele)
            second_ele = min(nums)
            arr.append(second_ele)
            nums.remove(second_ele)
            arr.append(first_ele)
        return arr
