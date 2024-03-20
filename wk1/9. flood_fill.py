# def bfs(image, r, c, orig, visited, new):
#     max_r = len(image)
#     max_c = len(image)
#     image[r][c] = new
#     visited[r][c] = new
#     if r + 1 < max_r and image[r + 1][c] == orig and visited[r + 1][c] == -1:
#         bfs(image, r + 1, c, orig, visited, new)
#     if r - 1 >= 0 and image[r - 1][c] == orig and visited[r - 1][c] == -1:
#         bfs(image, r - 1, c, orig, visited, new)
#     if c + 1 < max_c and image[r][c + 1] == orig and visited[r][c + 1] == -1:
#         bfs(image, r, c + 1, orig, visited, new)
#     if c - 1 >= 0 and image[r][c - 1] == orig and visited[r][c - 1] == -1:
#         bfs(image, r, c -1, orig, visited, new)
        
# class Solution:
#     def floodFill(self, image, sr: int, sc: int, color: int):
#         max_r = len(image)
#         max_c = len(image)
#         visited = x = [[-1 for i in range(max_r)] for j in range(max_c)]
#         bfs(image, sr, sc, image[sr][sc], visited, color)
#         return image
    
    
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        if image[sr][sc] == color:
            return image
        
        orig = image[sr][sc]
        stack = [(sr, sc)]
        max_r = len(image)
        max_c = len(image[0])
        while stack:
            r,c = stack.pop()
            if 0 <= r < max_r and 0 <= c < max_c and image[r][c] == orig:
                image[r][c] = color
                stack.extend(((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
        return image
