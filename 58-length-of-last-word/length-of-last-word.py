class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        strip_s = s.strip()

        list_s = s.split()

        return len(list_s[-1])