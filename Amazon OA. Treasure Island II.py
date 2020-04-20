"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
"""

import unittest
import collections
from typing import List

class Solution:
    def minSteps(self, grid: List[List[int]]) -> int: 
        """
        breadth first search
        time: O(MN)
        space: O(MN)
        """
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "S":
                    queue.append([(i, j)])
        visited = set()
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j]]:
                    if 0 <= r < m and 0 <= c < n:
                        if grid[r][c] == "X":
                            return steps
                        if grid[r][c] == "O" and (r, c) not in visited:
                            visited.add((r, c))
                            queue.append((r, c))


class TestSolution(unittest.TestCase):
    def test(self):
        grid = [['S', 'O', 'O', 'S', 'S'],
                ['D', 'O', 'D', 'O', 'D'],
                ['O', 'O', 'O', 'O', 'X'],
                ['X', 'D', 'D', 'O', 'O'],
                ['X', 'D', 'D', 'D', 'O']]
        output = 3
        self.assertEqual(grid, output, "Should be 3")
