class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
       
        for i in range(n):
            my_set = set()
            
            for j in range(i, n):

                if s[j] in my_set:
                    break
                
                my_set.add(s[j])
                max_len = max(max_len, len(my_set))
        return max_len