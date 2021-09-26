import java.io.*;
import java.util.*;
public class snowboots {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("snowboots.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(fin.readLine());
        int[] tiles = new int[n];
        for (int i = 0; i < n; i++) {
            tiles[i] = Integer.parseInt(st.nextToken());
        }
        int[][] boots = new int[b][2];
        for (int i = 0; i < b; i++) {
            st = new StringTokenizer(fin.readLine());
            boots[i][0] = Integer.parseInt(st.nextToken());
            boots[i][1] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        int i = 0;
        for (int boot = 0; boot < b; boot++) {
            if (i == n-1) {
                result = boot;
                break;
            }
            for (int j = i + boots[boot][1]; j > i; j--) {
                if (j >= n) {
                    continue;
                }
                if (tiles[j] > boots[boot][0]) {
                    continue;
                }
                i = j;
                break;
            }
        }

        System.out.println(result);
    }
}
