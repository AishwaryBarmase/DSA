from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Count frequency of each lowercase letter 'a' to 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Lists are mutable and unhashable, so convert count to a tuple
            anagram_groups[tuple(count)].append(s)
            
        return list(anagram_groups.values())
