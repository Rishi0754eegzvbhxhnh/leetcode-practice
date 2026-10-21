class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # palindrome table
        is_pal = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2 or is_pal[start + 1][end - 1]
                ):
                    is_pal[start][end] = True

        dp = [0] * n

        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')

                for j in range(1, i + 1):
                    if is_pal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]