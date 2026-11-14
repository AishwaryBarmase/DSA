class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digit_sum = 0
        for digit in nums:
            if digit > 9:
                while digit:
                    number = digit % 10
                    digit_sum += number
                    digit //= 10
            else:
                digit_sum += digit
        return sum(nums) - digit_sum