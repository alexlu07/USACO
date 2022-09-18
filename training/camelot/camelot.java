/*
  ID: alexlu.1
  LANG: JAVA
  TASK: camelot
*/
import java.io.*;
import java.util.*;
import java.lang.Math;

public class camelot {
    public static final int bigNumber = 1000000;

    public static int r;
    public static int c;

    public static final int[][] directions = new int[][] { {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}, {0, 0} };

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("camelot.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(fin.readLine());

        int[] king = new int[2];
        king[1] = st.nextToken().charAt(0) - 'A';
        king[0] = Integer.parseInt(st.nextToken()) - 1;

        int numKnights = 0;
        int[][] knights = new int[r*c][2];
        
        String line;
        while ((line = fin.readLine()) != null) { 
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int i = st.nextToken().charAt(0) - 'A';
                int j = Integer.parseInt(st.nextToken())-1;

                knights[numKnights++] = new int[] {j, i};
            }
        }

        fin.close();

        int[][][][] dist = new int[r][c][r][c];
        for (int[][][] i : dist) {
            for (int[][] j : i) {
                for(int[] k : j) {
                    Arrays.fill(k, bigNumber);
                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                LinkedList<int[]> queue = new LinkedList<int[]>();
                queue.add(new int[]{ i, j});

                dist[i][j][i][j] = 0;

                while (queue.size() > 0) {
                    int[] node = queue.poll();

                    for (int[] d : directions) {
                        int x = node[0] + d[0];
                        int y = node[1] + d[1];
                                
                        if (x < 0 || y < 0 || x >= r || y >= c || dist[i][j][x][y] != bigNumber) {
                            continue;  
                        }
                        
                        dist[i][j][x][y] = dist[i][j][node[0]][node[1]] + 1;
                        queue.add(new int[] { x, y });
                    }                    
                }
            }
        }

        int kIStart = Math.max(0, king[0] - 2);
        int kJStart = Math.max(0, king[1] - 2);
        int kIEnd = Math.min(r, king[0] + 2);
        int kJEnd = Math.min(c, king[1] + 2);

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int totalCost = 0;
                int extraCost = kingDist(i, j, king);

                for (int x = 0; x < numKnights; x++) {
                    totalCost += dist[knights[x][0]][knights[x][1]][i][j];
                    for (int kI = kIStart; kI < kIEnd; kI++) {
                        for (int kJ = kJStart; kJ < kJEnd; kJ++) {
                            int kingCost = kingDist(kI, kJ, king)
                                         + dist[knights[x][0]][knights[x][1]][kI][kJ]
                                         + dist[kI][kJ][i][j]
                                         - dist[knights[x][0]][knights[x][1]][i][j];
                            
                            if (kingCost < extraCost) extraCost = kingCost;
                        }
                    }
                }

                if (totalCost + extraCost < answer) answer = totalCost + extraCost;
            }
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("camelot.out")));
        fout.println(answer);
        fout.close();
    }

    public static int kingDist(int i, int j, int[] king) {
        return Math.max(Math.abs(king[0] - i), Math.abs(king[1] - j));
    }

}
