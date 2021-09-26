import java.io.*;
import java.util.*;
public class rental {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("rental.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        Integer[] cows = new Integer[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int c = Integer.parseInt(st.nextToken());
            cows[i] = c;
        }
        Arrays.sort(cows, Collections.reverseOrder());

        int[][] stores = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(fin.readLine());
            int q = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            stores[i][0] = q;
            stores[i][1] = p;
        }
        Arrays.sort(stores, new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b) {
                    return b[1] - a[1];
                }
            });

        Integer[] rentals = new Integer[r];
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            rentals[i] = x;
        }
        Arrays.sort(rentals, Collections.reverseOrder());

        int si = 0;
        int ri = 0;
        int c1 = 0;
        int c2 = n;

        long result = 0;
        while (c1 < c2) {
            int sp = 0;
            int x = cows[c1];
            int stores_used = 0;
            for (int i = si; i < m; i++) {
                if (stores[i][0] > x) {
                    sp += stores[i][1] * x;
                    break;
                } else if (stores[i][0] == x) {
                    stores_used++;
                    sp += stores[i][1] * x;
                    break;
                } else if (stores[i][0] < x) {
                    x -= stores[i][0];
                    sp += stores[i][1] * stores[i][0];
                    stores_used++;
                }
            }
            int rp = 0;
            if (ri < r) {
                rp = rentals[ri];
            }

            if (sp > rp) {
                si += stores_used;
                stores[si][0] -= x;
                c1++;
                result += sp;
            } else if (rp > 0) {
                ri++;
                c2--;
                result += rp;
            }

        }
        // System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("rental.out")));
        fout.print(result);
        fout.close();
        // System.out.println(Arrays.deepToString(stores));
        // System.out.println(Arrays.toString(cows));
        // System.out.println(cows1);

    }
}
