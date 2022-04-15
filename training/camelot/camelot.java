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
    public static int[][] directions = new int[8][2];

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("camelot.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(fin.readLine());
        int[] king = new int[2];
        king[0] = st.nextToken().charAt(0) - 'A';
        king[1] = Integer.parseInt(st.nextToken()) - 1;


        int n = 0;
        ArrayList<int[]> knights = new ArrayList<int[]>();
        String line;
        while ((line = fin.readLine()) != null) {
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int i = st.nextToken().charAt(0) - 'A';
                int j = Integer.parseInt(st.nextToken())-1;

                knights.add(new int[]{ i, j });
                n++;
            }

        }

        for (int ind = 0; ind < 8; ind++) {
            int i = ind / 4;
            int j = (ind % 4) / 2;
            int k = ind % 2;

            int a = 1;
            int b = 2;

            if (i == 1) { a = -1; }
            if (j == 1) { b = -2; }
            if (k == 1) {
                int x = a;
                a = b;
                b = x;
            }

            directions[ind][0] = a;
            directions[ind][1] = b;
        }

        HashMap<int[], int[][]> distance = new HashMap<int[], int[][]>();
        for (int[] knight : knights) {
            bfs(distance, knight, directions);
        }

        // for (int[] name: distance.keySet()) {
        //     String key = Arrays.toString(name);
        //     System.out.println(key);
        //     int[][] value = distance.get(name);
        //     for (int[] row : value) {
        //         System.out.println(Arrays.toString(row));
        //     }
        //     System.out.println("--------------");
        // }



        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("camelot.out")));
        fout.println();
        fout.close();
    }

    public static void bfs(HashMap<int[], int[][]> distance, int[] source, int[][] directions) {
        int[][] dist = new int[r][c];

        HashSet<Integer> visited = new HashSet<Integer>();
        visited.add(source[0] * 100 + source[1]);

        LinkedList<int[]> queue = new LinkedList<int[]>();
        queue.add(new int[]{ source[0], source[1], 0 });

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
