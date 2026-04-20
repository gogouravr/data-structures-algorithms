class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        dp = {}
        def lcs(i: int = 0,j: int = 0) -> int:
            key = (i,j)
            if key in dp:
                return dp[key]

            if i == len(text1) or j == len(text2):
                return 0

            dp[key] = max(lcs(i+1,j) ,lcs(i,j+1), int(text1[i] == text2[j]) + lcs(i+1,j+1))
            return dp[key]

        
        return lcs()