import java.util.*;

public class Hi {

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
        
        int lo = 0, hi = 2 * n, res = 0;


        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (isPossible(dist, mid, n)) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }

        }
        return res;
    }

    boolean isPossible(int[][] dist, int query, int n) {
        Queue <int []>  q = new ArrayDeque<>();
        q.add(new int[]{0,0});
        while (!q.isEmpty()) {
            int[] elem = q.poll();
            int r = elem[0], c = elem[1];
            if (r == n -1 && c == n - 1) return true;
            for (int i = 0; i < 4; i++) {
                int nr = r + directions[i][0];
                int nc = c + directions[i][1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && dist[r][c] >= query) {
                    q.add(new int[]{nr, nc});
                    
                }
            }
        }
        return false;
    }

    public int[] asteroidCollision(int[] asteroids) {
        int n = asteroids.length;
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (asteroids[i] > 0 || s.isEmpty()) {
                s.push(asteroids[i]);
            } else {
                while (!s.isEmpty() && s.peek() > 0 && s.peek() < Math.abs(asteroids[i])) {
                    s.pop();
                }
                if (!s.isEmpty() && s.peek() == Math.abs(asteroids[i])) {
                    s.pop();
                } else {
                    if (s.isEmpty() || s.peek() < 0) {
                        s.push(asteroids[i]);
                    }
                }
            }
        }
        int[] res = new int[s.size()];
        for (int i = s.size() - 1; i >= 0; i--) {
            res[i] = s.pop();
        }
        return res;
    } 

    


    // public static void main(String[] args) {
    //     List<List<Integer>> grid = new ArrayList<>();
    //     grid.add(new ArrayList<>())
    //     System.out.println(Hi.maximumSafenessFactor([[0,1,1],[0,1,1],[1,1,0]]));
    // }

    // [[0,1,1],
//      [0,0,0],
//      [0,0,0]]


    // [[1, 0, 0], 
    // [2, 1, 1], 
    // [3, 2, 2]]
}
