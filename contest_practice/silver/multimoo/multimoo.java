import java.io.*;
import java.util.*;
public class multimoo {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("multimoo.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            for (int j = 0; j < n; j++) {
                int x = Integer.parseInt(st.nextToken());
                board[i][j] = x;
            }
        }

        int[][] c = new int[n][n];
        for (int[] r: c) {
            Arrays.fill(r, -1);
        }
        ArrayList<HashMap<Integer, Integer>> team_size = new ArrayList<HashMap<Integer, Integer>>();
        int component = 0;
        int[][] visited = new int[n][n];
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (c[i][j] == -1) {
                    System.out.println("" + i + " " + j);
                    int size = floodfill(board, n, c, team_size, component, visited, i, j);
                    component++;
                    if (size > result) {
                        result = size;
                    }
                }
            }
        }
        System.out.println(result);
        System.out.println(team_size);
    }

    public static int floodfill(int[][] board, int n, int[][] c, ArrayList<HashMap<Integer, Integer>> team_size, int component, int[][] visited, int i, int j) {
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int current = board[i][j];
        team_size.add(new HashMap<Integer, Integer>());
        team_size.get(component).put(-1, 1);
        visited[i][j] = 1;
        c[i][j] = component;
        LinkedList<int[]> queue = new LinkedList<int[]>();
        queue.add(new int[]{i, j});
        while (queue.size() > 0) {
            int[] coords = queue.poll();

            for (int d = 0; d < 4; d++) {
                int[] new_c = new int[]{coords[0] + directions[d][0], coords[1] + directions[d][1]};
                if (new_c[0] < 0 || new_c[0] >= n || new_c[1] < 0 || new_c[1] >= n) {
                    continue;
                }

                if (board[new_c[0]][new_c[1]] == current && visited[new_c[0]][new_c[1]] == 0) {
                    visited[new_c[0]][new_c[1]] = 1;
                    c[new_c[0]][new_c[1]] = component;
                    queue.add(new_c);
                    
                    team_size.get(component).compute(-1, (key, val) -> val+1);
                } else if (d == 0 || d == 2) {
                    int other = c[new_c[0]][new_c[1]];
                    if (team_size.get(component).containsKey(other) == false) {
                        team_size.get(component).put(other, team_size.get(other).getOrDefault(component, 0));
                    }
                }

            }
        }
        int largest = 0;
        for (int v: team_size.get(component).values()) {
            if (team_size.get(component).get(-1) + v > largest) {
                largest = team_size.get(component).get(-1) + v;
            }
        }
        return largest;

    }
}
