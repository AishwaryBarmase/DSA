class Solution(object):
    def countDigits(self, num):
        count = 0
        len_ = num
        while len_:
            val = len_ % 10
            if num % val == 0:
                count += 1
            len_ /= 10
        return count
        