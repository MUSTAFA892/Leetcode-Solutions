class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m , n = len(nums1) , len(nums2)
        max_ = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_ = max(max_, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_
        