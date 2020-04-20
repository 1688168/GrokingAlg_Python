from collections import namedtuple
from timeit import default_timer as timer
from pprint import pprint as pp

class Solution:
    def numIslands(self, grid):

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        pp(visited)
        pp(grid)

        cnt = 0
        for xx in range(len(grid)):
            for yy in range(len(grid[0])):
                if grid[xx][yy] == '1' and visited[xx][yy] is not True:
                    cnt += 1
                    self.exploring(grid, visited, xx, yy)

        print("cnt: ", cnt)
        return cnt

    def exploring(self, grid, visited, xx, yy):
        # is in scope
        if xx < 0 or xx >= len(grid) or yy < 0 or yy >= len(grid[0]):
            return

        # is visited
        if visited[xx][yy] == True or grid[xx][yy] != '1':
            return

        Direction = namedtuple('Direction', 'up down left right')

        direction = Direction(up=(1, 0), down=(-1, 0), left=(0, -1), right=(0, 1))

        #mark visited
        visited[xx][yy] = True

        #print("===========")


        for x, y in direction:
            pp(visited)
            print(f"x={x}, y={y}, xx={xx}, yy={yy}")
            self.exploring(grid, visited, xx + x, yy + y)

s=Solution()
start = timer()
#o=s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])

o=s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

#o=s.numIslands([["1"],["1"]])


#o=s.checkValidString("(*)")



end = timer()
print(end - start)
print(o)