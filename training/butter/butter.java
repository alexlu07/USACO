/*
ID: alexlu.1
LANG: JAVA
TASK: butter
*/
import java.io.*;
import java.util.*;

class DistanceComparator implements Comparator<Integer> {
    private int cow;
    private int[][] distance;

    public DistanceComparator(int c, int[][] d) {
        cow = c;
        distance = d;
    }

    @Override
    public int compare(Integer x, Integer y) {
        return distance[cow][x] - distance[cow][y];
    }

}

public class butter {
    public static void main(String args[]) throws IOException {
        long start = System.nanoTime();
        BufferedReader fin = new BufferedReader(new FileReader("butter.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] cows = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            cows[i] = Integer.parseInt(st.nextToken()) - 1;
        }

        int[] nNeighbors = new int[p];
        int[][] neighbors = new int[p][p];
        int[][] paths = new int[p][p];
        for (int i = 0; i < c; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int distance = Integer.parseInt(st.nextToken());
            neighbors[x][nNeighbors[x]] = y;
            neighbors[y][nNeighbors[y]] = x;
            nNeighbors[x] += 1;
            nNeighbors[y] += 1;
            paths[x][y] = distance;
            paths[y][x] = distance;

        }

        int[][] distance = new int[n][p];

        for (int cow = 0; cow < n; cow++) {
            int[] visited = new int[p];
            for (int i = 0; i < p; i++) {
                distance[cow][i] = Integer.MAX_VALUE;
            }

            PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(new DistanceComparator(cow, distance));
            minHeap.add(cows[cow]);
            distance[cow][cows[cow]] = 0;
            // System.out.println(minHeap);
            while (minHeap.size() > 0) {
                int i = minHeap.poll();
                visited[i] = 1;

                // System.out.println(distance[cow][i]);

                for (int j = 0; j < nNeighbors[i]; j++) {
                   if (visited[neighbors[i][j]] == 0) {
                       if (distance[cow][i] + paths[i][neighbors[i][j]] < distance[cow][neighbors[i][j]]) {
                           // System.out.println("dis:" + i + ", " + distance[cow][neighbors[i][j]] + " " + distance[cow][i] + " " + paths[i][neighbors[i][j]] + ", " + neighbors[i][j]);

                           distance[cow][neighbors[i][j]] = distance[cow][i] + paths[i][neighbors[i][j]];
                           minHeap.remove(neighbors[i][j]);
                           minHeap.add(neighbors[i][j]);

                        }
                    }
                }
            }

        }

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < p; i++) {
            int counter = 0;
            for (int j = 0; j < n; j++) {
                counter += distance[j][i];
            }

            if (counter < result) {
                result = counter;
            }
            // System.out.println(counter);
        }

        // System.out.println(Arrays.deepToString(distance));
        // System.out.println("Cow number 9  at pasture " + cows[9] + Arrays.toString(distance[9]));
        // System.out.println("Cow number 10 at pasture " + cows[10] + Arrays.toString(distance[10]));
        System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("butter.out")));
        fout.println(result);
        fout.close();
        long end = System.nanoTime();
        System.out.println("Time: " + (end - start));
    }
}
