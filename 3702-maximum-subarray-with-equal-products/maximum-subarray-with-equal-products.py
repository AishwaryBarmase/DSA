class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0

        for i in range(n):
            product  = 1
            gcd = 0
            lcm = 1

            for j in range(i, n):
                product *= nums[j]
                
                gcd = self.findgcd(gcd, nums[j])

                lcm = self.findlcm(lcm, nums[j])

                if product == gcd * lcm:
                    ans = max(ans, j-i + 1)

        return ans

    def findgcd(self, a,b):
        if b == 0:
            return a
            
        return gcd(b, a%b)

    def findlcm(self, a,b):
        return a*b // gcd(a,b)