# class Solution:
#     def maxWidthOfVerticalArea(self, points) -> int:
#         points = sorted(points, key = lambda p : p[0])
#         dist = [0] * len(points)
#         for i in range(1, len(points)):
#             dist[i] = points[i] - points[i - 1]
#         return min(dist)

class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        points = sorted(points, key = lambda p : p[0])
        dist = [points[i][0] - points[i - 1][0] for i in range(1, len(points))]
        return max(dist)