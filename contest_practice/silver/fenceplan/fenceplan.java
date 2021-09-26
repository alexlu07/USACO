import java.io.*;
import java.util.*;
public class fenceplan {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("fenceplan.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] coords = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            coords[i] = new int[]{x, y};
        }
        ArrayList<ArrayList<Integer> > neighbors = new ArrayList<ArrayList<Integer> >(n);
        for (int i = 0; i < n; i++) {
            neighbors.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            neighbors.get(x).add(y);
            neighbors.get(y).add(x);
        }

        int result = Integer.MAX_VALUE;
        int[] visited = new int[n];
        for (int x = 0; x < n; x++) {
            if (visited[x] == 1) {
                continue;
            }
            LinkedList<Integer> queue = new LinkedList<Integer>();
            queue.add(x);
            visited[x] = 1;
            int l = coords[x][0];
            int r = coords[x][0];
            int t = coords[x][1];
            int d = coords[x][1];
            while (queue.size() > 0) {
                int i = queue.poll();
                if (coords[i][0] < l) {
                    l = coords[i][0];
                } else if (coords[i][0] > r) {
                    r = coords[i][0];
                } if (coords[i][1] > t) {
                    t = coords[i][1];
                } else if (coords[i][1] < d) {
                    d = coords[i][1];
                }

                for (int j: neighbors.get(i)) {
                    if (visited[j] == 0) {
                        visited[j] = 1;
                        queue.add(j);
                    }
                }
            }
            if (2 * (t-d + r-l) < result) {
                result = 2 * (t-d + r-l);
            }
        }
        // System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("fenceplan.out")));
        fout.print(result);
        fout.close();
    }
}
