class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        Unique_set = set(s)
        for char in Unique_set:
            if s.count(char) != t.count(char):
                return False
        
        return True