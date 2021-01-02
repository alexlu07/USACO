import java.io.*;
import java.util.*;
public class pump {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("pump.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][][] neighbors = new int[n][n][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(fin.readLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;
            int c = Integer.parseInt(st.nextToken());
            int f = Integer.parseInt(st.nextToken());
            neighbors[a][b] = new int[]{c, f};
            neighbors[b][a] = new int[]{c, f};
        }

        int[] efficiency = new int[n];
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        int[] visited = new int[n];
        int[] speed = new int[n];
        Arrays.fill(speed, Integer.MAX_VALUE);
        distance[0] = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((x, y) -> Integer.compare(efficiency[y], efficiency[x]));
        heap.add(0);
        while (heap.size() > 0) {
            int i = heap.poll();
            // System.out.println(i);
            // System.out.println(heap);
            visited[i] = 1;
            for (int j = 0; j < n; j++) {
                // System.out.println(Arrays.toString(neighbors[i][j]));
                if (neighbors[i][j][0] > 0 && visited[j] == 0) {

                    if ((Math.min(speed[i], neighbors[i][j][1]) * 1000000)/ (distance[i] + neighbors[i][j][0]) > efficiency[j]) {
                        if (efficiency[j] == 0) {
                            heap.add(j);
                        }
                        speed[j] = Math.min(speed[i], neighbors[i][j][1]);
                        distance[j] = distance[i] + neighbors[i][j][0];
                        efficiency[j] = (speed[j] * 1000000) / distance[j];
                    }
                }
            }
        }
        // System.out.println(Arrays.toString(efficiency));

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("pump.out")));
        fout.print("" + efficiency[n-1]);
        fout.close();
    }
}

