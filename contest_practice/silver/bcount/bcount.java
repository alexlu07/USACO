import java.io.*;
import java.util.*;
public class bcount {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("bcount.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[][] cows = new int[3][n];
        int[][] prefix = new int[3][n+1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int type = Integer.parseInt(st.nextToken());
            cows[type-1][i] = 1;

            prefix[0][i+1] = prefix[0][i];
            prefix[1][i+1] = prefix[1][i];
            prefix[2][i+1] = prefix[2][i];

            prefix[type-1][i+1] += 1;
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("bcount.out")));

        st = new StringTokenizer(fin.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        fout.printf("%d %d %d", prefix[0][b] - prefix[0][a-1], prefix[1][b] - prefix[1][a-1], prefix[2][b] - prefix[2][a-1]);

        for (int i = 1; i < q; i++ ) {
            st = new StringTokenizer(fin.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            fout.printf("%n%d %d %d", prefix[0][b] - prefix[0][a-1], prefix[1][b] - prefix[1][a-1], prefix[2][b] - prefix[2][a-1]);

        }
        fout.close();
    }
}
