class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single, double = 0, 0
        for ele in nums:
            if ele > 9:
                single += ele
            else:
                double += ele
        return single != double