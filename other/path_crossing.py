class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        x, y = 0, 0
        points.add((x,y))
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            if (x,y) in points:
                return True
            else:
                points.add((x,y))
        return False