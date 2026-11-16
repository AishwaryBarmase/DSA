class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice, bob = 0, 0
        for ele in nums:
            if ele > 9:
                alice += ele
            else:
                bob += ele
        return alice != bob