import java.io.*;
import java.util.*;
public class vacationgold {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("vacationgold.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[][] dist = new int[n][n];
        Arrays.stream(dist).forEach(a -> Arrays.fill(a, Integer.MAX_VALUE));
        for (int i = 0; i < n; i++) {
            dist[i][i] = 0;
        }
        // System.out.println(Arrays.deepToString(dist));
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(fin.readLine());
            int u = Integer.parseInt(st.nextToken())-1;
            int v = Integer.parseInt(st.nextToken())-1;
            int d = Integer.parseInt(st.nextToken());

            dist[u][v] = d;
        }
        // System.out.println(Arrays.deepToString(dist));
        int[] hubs = new int[k];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(fin.readLine());
            int h = Integer.parseInt(st.nextToken())-1;
            hubs[i] = h;
        }
        // System.out.println(Arrays.toString(hubs));
        for (int x: hubs) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][x] == Integer.MAX_VALUE || dist[x][j] == Integer.MAX_VALUE) {
                        continue;
                    }
                    if (dist[i][x] + dist[x][j] < dist[i][j]) {
                        dist[i][j] = dist[i][x] + dist[x][j];
                    }
                }
            }
        }

        int tickets = 0;
        long cost = 0;
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(fin.readLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;
            // System.out.println(dist[a][b]);
            if (dist[a][b] < Integer.MAX_VALUE) {
                tickets++;
                cost += dist[a][b];
            }
        }

        // System.out.println(Arrays.deepToString(dist));
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("vacationgold.out")));
        fout.println(tickets);
        fout.print(cost);
        fout.close();
    }
}
