/*
ID: alexlu.1
LANG: JAVA
TASK: shopping
*/
import java.io.*;
import java.util.*;

public class shopping {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("shopping.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int s = Integer.parseInt(st.nextToken());
        int[][] offers_raw = new int[s][12];
        for (int i = 0; i < s; i++) {
            st = new StringTokenizer(fin.readLine());
            int n = Integer.parseInt(st.nextToken());
            offers_raw[i][10] = n;
            for (int j = 0; j < n*2; j+=2) {
                int c = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                offers_raw[i][j] = c;
                offers_raw[i][j+1] = k;
            }
            int p = Integer.parseInt(st.nextToken());
            offers_raw[i][11] = p;
        }

        st = new StringTokenizer(fin.readLine());
        int b = Integer.parseInt(st.nextToken());
        int[][] products = new int[b][3];
        int[][] offers = new int[s][b+1];
        int size = 1;
        int[] dimensions = new int[b];
        for (int i = 0; i < b; i++) {
            st = new StringTokenizer(fin.readLine());
            int c = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            size *= k+1;
            dimensions[i] = k;

            products[i][0] = c;
            products[i][1] = k;
            products[i][2] = p;

            for (int j = 0; j < s; j++) {
                for (int x = 0; x < offers_raw[j][10] * 2; x+=2) {
                    if (offers_raw[j][x] == c) {
                        offers[j][i] = offers_raw[j][x+1];
                    }
                }
                offers[j][b] = offers_raw[j][11];
            }
        }

        fin.close();

        // System.out.println(Arrays.deepToString(products));
        int[] multiplier = new int[b];
        Arrays.fill(multiplier, 1);
        for (int i = b-2; i >= 0; i--) {
            multiplier[i] = multiplier[i+1] * (products[i+1][1]+1);
        }
        int[] prices = new int[size];
        for (int i = 0; i < size; i++) {
            int r = i;
            for (int j = 0; j < b; j++) {
                // if (i == size-1) {
                //     System.out.println("" + r + " " + r / multiplier[j]);
                // }
                prices[i] += (r / multiplier[j]) * products[j][2];
                // System.out.println(prices[i]);
                r %= multiplier[j];
            }
        }
        // System.out.println(Arrays.deepToString(offers));
        // System.out.println(prices[size-1]);
        for (int i = 0; i < size; i++) {
            int[] d = new int[b];
            int r = i;
            for (int j = 0; j < b; j++) {
                d[j] += r / multiplier[j];
                r %= multiplier[j];
            }
            for (int j = 0; j < s; j++) {
                // System.out.println(Arrays.toString(dimensions));
                int ind = addIndex(dimensions, d, offers[j], multiplier);
                // if (i == 0) {
                //     System.out.println(Arrays.toString(offers[j]));
                //     System.out.println("" + prices[i] + offers[j][b] + " " + prices[ind]);
                // }
                if (ind == -1) {
                    // System.out.println("no");
                    continue;
                }
                if (prices[i] + offers[j][b] < prices[ind]) {
                    // System.out.println("yes");
                    prices[ind] = prices[i] + offers[j][b];
                }
            }
        }
        // System.out.println(prices[1*1296 + 0*216 + 0*36 + 0*6 + 0*1]);
        // System.out.println(prices[1296]);
        // System.out.println(Arrays.toString(multiplier));
        // System.out.println(Arrays.deepToString(offers));
        // System.out.println(Arrays.deepToString(products));

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("shopping.out")));
        fout.println(prices[size-1]);
        fout.close();
    }

    public static int addIndex(int[] dimensions, int[] values, int[] offer, int[] multiplier) {
        // System.out.println(Arrays.toString(dimensions));
        // System.out.println(Arrays.toString(values));
        // System.out.println(Arrays.toString(offer));
        // System.out.println(Arrays.toString(multiplier));
        int result = 0;
        for (int i = 0; i < dimensions.length; i++) {
            int x = values[i] + offer[i];
            if (x > dimensions[i]) {
                return -1;
            }
            result += x * multiplier[i];
        }
        return result;
    }

}
