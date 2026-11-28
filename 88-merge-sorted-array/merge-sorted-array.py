class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        for i in range(len(nums2)):
            nums1[m] = nums2[i]
            m += 1
        
        nums1.sort()
        