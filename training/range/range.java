/*
ID: alexlu.1
LANG: JAVA
TASK: range
*/

import java.io.*;
import java.util.*;

public class range {

    public static final int[] dI = new int[] { -1,  0, -1};
    public static final int[] dJ = new int[] {  0, -1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("range.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[][] field = new int[n][n];
        int[][] maxSize = new int[n][n];
        int[] maxSizeCounter = new int[n+1];

        for (int i = 0; i < n; i++) {
            String line = fin.readLine();
            for (int j = 0; j < n; j++) {
                field[i][j] = line.charAt(j) - '0';

                if (field[i][j] == 0) {
                    maxSize[i][j] = 0;
                    maxSizeCounter[0]++;
                    continue;
                }

                int min = Integer.MAX_VALUE;

                for (int d = 0; d < 3; d++) {
                    int x = i + dI[d];
                    int y = j + dJ[d];
                    
                    if (x < 0 || y < 0) {
                        min = 0;
                        break;
                    }

                    if (maxSize[x][y] < min) min = maxSize[x][y];
                }

                maxSize[i][j] = min + 1;
                maxSizeCounter[min+1]++;
            }
        }

        fin.close();

        int[] results = new int[n+1];
        int squares = n * n;

        squares -= maxSizeCounter[0] + maxSizeCounter[1];
        for (int i = 2; i <=n; i++) {
            results[i] = squares;
            squares -= maxSizeCounter[i];
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("range.out")));
        for (int i = 0; i <= n; i++) {
            if (results[i] > 0) {
                fout.println("" + i + " " + results[i]);
            }
        }
        fout.close();
    }
}
