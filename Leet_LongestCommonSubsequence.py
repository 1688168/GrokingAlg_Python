from timer import *
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        dp=[[None for _ in range(n2)] for _ in range(n1)]
        return self.lcs(text1, text2, n1-1, n2-1, dp)

    def lcs(self, s1, s2, ii, jj, dp):
        if ii==0 and jj==0:
            dp[ii][jj] = 1 if s1[ii] == s2[jj] else 0
            return dp[ii][jj]

        if ii < 0 or jj < 0:
            return 0

        if dp[ii][jj] is not None:
            return dp[ii][jj]


        if s1[ii] == s2[jj]:
            dp[ii][jj] = 1+self.lcs(s1, s2, ii-1, jj-1, dp)
            return dp[ii][jj]
        else:
            dp[ii][jj] = max(self.lcs(s1, s2, ii-1, jj, dp), self.lcs(s1, s2, ii, jj-1, dp))
            return dp[ii][jj]


t=make_timer()


s=Solution()

t()
o=s.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")
#o=s.longestCommonSubsequence("ace", "ace")
#o=s.longestCommonSubsequence("abc", "def")
print(" cnt: ", o)
t()



