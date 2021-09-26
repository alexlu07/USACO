import java.io.*;
import java.math.BigInteger;
import java.util.*;
public class reststops {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("reststops.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int l = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int f = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int[][] stops = new int[n][2];
        TreeSet<int[]> tastiest = new TreeSet<int[]>(new Taste());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            tastiest.add(new int[]{c, x});
            stops[i][0] = x;
            stops[i][1] = c;
        }

        int dif = f-b;
        int stop = 0;
        BigInteger result = BigInteger.ZERO;
        for (int[] i:tastiest) {
            if (i[1] <= stop) {
                continue;
            }
            int t = (i[1] - stop) * dif;
            BigInteger increase = BigInteger.valueOf(i[0]);
            increase = increase.multiply(BigInteger.valueOf(t));
            result = result.add(increase);
            // if (result < 0) {
                // System.out.println("what");
            // }
            stop = i[1];
        }
        System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("reststops.out")));
        fout.print(result);
        fout.close();
    }
}

class Taste implements Comparator<int[]>{
    public int compare(int[] a, int[] b) {
        if (a[0] < b[0]) {
            return 1;
        } if (a[0] > b[0]) {
            return -1;
        }

        if (a[1] < b[1]) {
            return 1;
        } if (a[1] > b[1]) {
            return -1;
        }

        return 0;
    }
}
