class Solution:
    def addDigits(self, num: int) -> int:
        Total = 0
        new_Total = 0
        number = num
        next_Total = 0
        while number:
            ToAdd = number % 10
            Total += ToAdd
            number //= 10
        while  Total:
            Toadd = Total % 10
            new_Total += Toadd
            Total //= 10
        
        while new_Total:
            Toadd = new_Total % 10
            next_Total += Toadd
            new_Total //= 10
        return next_Total


