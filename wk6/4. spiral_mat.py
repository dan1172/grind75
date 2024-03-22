class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) 
        res = []
        move = {
            'r' : (0, 1, 'd'),
            'd' : (1, 0, 'l'),
            'l' : (0, -1, 'u'),
            'u' : (-1, 0, 'r')
        }
        i, j, direction, num_added = 0, 0, 'r', 0
        while num_added < n * m:
            res.append(matrix[i][j])
            num_added += 1
            matrix[i][j] = None
            
            add_i, add_j, new_dir = move[direction]
            new_i = i + add_i
            new_j = j + add_j
            if not (0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] is not None):
                direction = new_dir
                add_i, add_j, _ = move[direction]
                new_i = i + add_i
                new_j = j + add_j
            i = new_i
            j = new_j
        return res
    
s = Solution()
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

        
        