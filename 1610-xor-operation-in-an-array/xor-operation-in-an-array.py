class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            value = start + (2 * i)
            nums.append(value)

        result = 0
        for i in nums:
             result ^= i
        return result  