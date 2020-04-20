from collections import deque
import math
from timeit import default_timer as timer
from pprint import pprint as pp

class Solution:
    def minPathSum(self, grid):
        dp=[[None for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # initialize what you can do
        dp[0][0]=grid[0][0] # start point cost

        # first row
        for ii in range(1, len(grid[0])):
            #print("ii1: ", ii)
            dp[0][ii] = dp[0][ii-1] + grid[0][ii]

        # first col
        for ii in range(1, len(grid)):
            #print("ii2: ", ii)
            dp[ii][0] = dp[ii-1][0] + grid[ii][0]


        for ii in range(1, len(grid)):
            for jj in range(1, len(grid[0])):
                dp[ii][jj] = min(dp[ii-1][jj]+grid[ii][jj], dp[ii][jj-1]+grid[ii][jj])



        return dp[len(grid)-1][len(grid[0])-1]

s=Solution()
start = timer()

o=s.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]])



end = timer()
print(end - start)
print(o)
"""

 qq = deque()
        start = (0, 0, grid[0][0])
        visited = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        qq.append(start)

        min_dist = math.inf
        curr_dist = grid[0][0]


        end = (len(grid) - 1, len(grid[0]) - 1, grid[len(grid) - 1][len(grid[0]) - 1])
cnt = 0
while qq:
    cnt += 1
    if cnt >= 1000:
        break
    xx, yy, dd = qq.popleft()
    print(f"xx={xx}, yy={yy}, dd={dd}, qsize={len(qq)}")

    if xx < 0 or yy < 0 or xx >= len(grid) or yy >= len(grid[0]):
        continue

    if (xx, yy) == (end[0], end[1]):
        curr_dist += grid[xx][yy]
        min_dist = min(min_dist, dd)
        visited[xx][yy] = min_dist
        continue

        # add neighbors (only left and down)

    if visited[xx][yy] == -1:
        visited[xx][yy] = dd
    else:
        if dd > visited[xx][yy]:
            continue

    x_right = xx
    y_right = yy + 1

    x_down = xx + 1
    y_down = yy

    if x_right < len(grid) and y_right < len(grid[0]):
        right_dist = dd + grid[x_right][y_right]
        if visited[x_right][y_right] == -1 or (
                visited[x_right][y_right] != -1 and right_dist > visited[x_right][y_right]):
            qq.append((x_right, y_right, right_dist))

    if x_down < len(grid) and y_down < len(grid[0]):
        down_dist = dd + grid[x_down][y_down]
        if visited[x_down][y_down] == -1 or (visited[x_down][y_down] != -1 and down_dist > visited[x_down][y_down]):
            qq.append((x_down, y_down, down_dist))

"""