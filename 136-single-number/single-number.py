class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap = Counter(nums)

        for x in hashmap:
            if hashmap[x] == 1:
                return x