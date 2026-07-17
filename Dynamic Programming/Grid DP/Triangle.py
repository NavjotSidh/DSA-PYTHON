def rec( i, j, tri, dp):
    if i == len(tri) - 1:
        dp[i][j] = tri[i][j]
        return dp[i][j]
    if dp[i][j] is not None:
        return dp[i][j]
    down = rec(i + 1, j, tri, dp)
    right_down = rec(i + 1, j + 1, tri, dp)

    dp[i][j] = tri[i][j] + min(down, right_down)
    return dp[i][j]


def minimumTotal(triangle):
    m = len(triangle)
    n = len(triangle[-1])
    dp = [[None] * len(row) for row in triangle]
    return rec(0, 0, triangle, dp)
