/*
  ID: alexlu.1
  LANG: JAVA
  TASK: camelot
*/
import java.io.*;
import java.util.*;

public class camelot {
    public static int r;
    public static int c;
    public static int[][] directions = new int[][] { {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2} };

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("camelot.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(fin.readLine());
        int[] king = new int[2];
        king[0] = st.nextToken().charAt(0) - 'A';
        king[1] = Integer.parseInt(st.nextToken()) - 1;

        int[][] totalCost = new int[r][c];
        int[][] extraCost = new int[r][c];

        String line;
        while ((line = fin.readLine()) != null) {
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int i = st.nextToken().charAt(0) - 'A';
                int j = Integer.parseInt(st.nextToken())-1;

                search(i, j, totalCost, extraCost);
            }
        }


        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("camelot.out")));
        fout.println();
        fout.close();
    }

    public static void search(int kI, int kJ, int[][] totalCost, int[][] extraCost) {

        int[][][] visited = new int[r][c][2];

        PriorityQueue<int[]> queue = new PriorityQueue<int[]>  ();
        queue.add(new int[]{ kI , kJ, 0 });

        while (queue.size() > 0) {
            int[] i = queue.poll();
            dist[i[0]][i[1]] = i[2];

            for (int[] d : directions) {
                int[] j = new int[]{ i[0] + d[0], i[1] + d[1], i[2] + 1 };

                // System.out.println(visited.add(j));
                if (visited.add(j[0] * 100 + j[1]) == false) {
                    continue;
                } else if (j[0] < 0 || j[1] < 0) {
                    continue;
                } else if (j[0] >= r || j[1] >= c) {
                    continue;
                }

                // System.out.println(Arrays.toString(j));
                queue.add(j);

            }
        }
        // for (int[] row : dist) {
        //     System.out.println(Arrays.toString(row));
        // }
        distance.put(source, dist);

    }
}
