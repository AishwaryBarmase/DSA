class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0

        for i in range(len(s)-1):
            char1 = str(s[i]).lower()
            char2 = str(s[i+1]).lower()

            if char1 != char2:
                count += 1
        
        return count