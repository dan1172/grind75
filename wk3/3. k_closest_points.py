import math

class Solution:
    def kClosest(self, points, k):
        return (sorted(points, key= lambda x : math.sqrt(x[0] ** 2 + x[1] ** 2)))[0:k]