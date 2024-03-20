import java.util.*;

public class MaxSafeness {
        int[][] directions = {{0,1}, {1,0},{0,-1}, {-1, 0}};
    
        public int maximumSafenessFactor(List<List<Integer>> grid) {
    
            int n = grid.size();
            int[][] dist = new int[n][n];
            boolean[][] visited = new boolean[n][n];
            Queue<int[]> q = new ArrayDeque<>();
    
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j ++) {
                    if (grid.get(i).get(j) == 1) {
                        q.add(new int[]{i, j, 0});
                        visited[i][j] = true;
                        dist[i][j] = 0;
                    }
                }
            }
    
            if (grid.get(0).get(0) == 1 || grid.get(n - 1).get(n - 1) == 1) return 0;
    
            while (!q.isEmpty()) {
                int[] elem = q.poll();
                int r = elem[0], c = elem[1], d = elem[2];
                dist[r][c] = d;
                for (int i = 0; i < 4; i++) {
                    int nr = r + directions[i][0];
                    int nc = c + directions[i][1];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && !visited[nr][nc]) {
                        q.add(new int[]{nr, nc, d + 1});
                        dist[nr][nc] = d + 1;
                        visited[nr][nc] = true;
                    }
                }
            }
    
            System.out.println(Arrays.deepToString(dist));
    
            
            int lo = 0, hi = 2 * n, res = 0;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                System.out.println("hi let's query" + mid);
                if (isPossible(dist, mid, n)) {
                    res = mid;
                    lo = mid + 1;
                    System.out.println("query" + mid + " was possible");
                } else {
                    hi = mid - 1;
                    System.out.println("query" + mid + " was not possible");
                }
    
            }
            return res;
        }
    
        public boolean isPossible(int[][] dist, int query, int n) {
            // System.out.println("hi");
            Queue <int []>  q = new ArrayDeque<>();
            boolean[][] visited = new boolean[n][n];
    
            if (dist[0][0] < query) {
                return false;
            }
            q.add(new int[]{0,0});
            while (!q.isEmpty()) {
                int[] elem = q.poll();
                int r = elem[0], c = elem[1];
                for (int i = 0; i < 4; i++) {
                    int nr = r + directions[i][0];
                    int nc = c + directions[i][1];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && dist[nr][nc] >= query && !visited[nr][nc]) {
                        q.add(new int[]{nr, nc});
                        visited[nr][nc] = true;
                        if (nr == n -1 && nc == n - 1) return true;
                    }
                }
            }
            return false;
        }
}
