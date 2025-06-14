class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ans=nums1[:m]+nums2[:n]
        ans.sort()
        for i in range(m+n):
            nums1[i]=ans[i]
            