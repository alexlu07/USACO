import java.io.*;
import java.util.*;
public class perimeter {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("perimeter.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());

        char[][] icecream = new char[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            icecream[i] = st.nextToken().toCharArray();

        }

        // System.out.println(Arrays.deepToString(icecream));
        // System.out.println(Arrays.toString(floodfill(icecream, 1, 4, n)));
        int[] result = new int[]{0, 0};
        int[][] visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0 && icecream[i][j] == '#') {
                    int[] ap = floodfill(icecream, visited, i, j, n);
                    if (ap[0] > result[0]) {
                        result = ap;
                    } else if (ap[0] == result[0] && ap[1] < result[1]) {
                        result = ap;
                    }
                }
            }
        }
        System.out.println(Arrays.toString(result));

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("perimeter.out")));
        fout.printf("%d %d", result[0], result[1]);
        fout.close();

    }

    public static int[] floodfill(char[][] icecream, int[][] visited, int x, int y, int n) {
        int[] ichange = new int[]{1, -1, 0, 0};
        int[] jchange = new int[]{0, 0, 1, -1};
        visited[x][y] = 1;
        int area = 0;
        int perimeter = 0;
        LinkedList<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        // System.out.println(Arrays.toString(queue.poll()));
        while (queue.size() > 0) {
            int[] coords = queue.poll();
            int i = coords[0];
            int j = coords[1];
            // System.out.println("" + i + " " + j);
            area++;
            for (int c = 0; c < 4; c++) {
                int a = i+ichange[c];
                int b = j+jchange[c];
                if (a < 0 || a >= n || b < 0 || b >= n || icecream[a][b] == '.') {
                    perimeter++;
                    continue;
                }

                if (visited[a][b] == 1) {
                    continue;
                }

                queue.add(new int[]{a, b});
                visited[a][b]++;
            }

        }
        // System.out.println(Arrays.deepToString(visited));
        return new int[]{area, perimeter};
    }
}
