class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_res = max(candies)
        for i in candies:
            val = i + extraCandies
            if val >= max_res:
                result.append(True)
            else:
                result.append(False)
        return result


