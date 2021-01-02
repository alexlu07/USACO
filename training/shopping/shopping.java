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
        int size = 0;
        for (int i = 0; i < b; i++) {
            st = new StringTokenizer(fin.readLine());
            int c = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            size += k;

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

        int[] multiplier = new int[b];
        Arrays.fill(multiplier, 1);
        for (int i = 0; i < multiplier.length; i++) {
            for (int j = i+1; j < products.length; j++) {
                multiplier[i] *= products[j][1];
            }
        }
        int[] prices = new int[size];
        for (int i = 0; i < size; i++) {
            
        }
        // System.out.println(Arrays.deepToString(offers));
        // System.out.println(Arrays.deepToString(products));
        // ArrayList<String> offersString = new ArrayList<String>();
        // for (int i = 0; i < s; i++) {
        //     offersString.add(fin.readLine());
        // }

        // StringTokenizer st = new StringTokenizer(fin.readline());
        // int b = Integer.parseInt(st.nextToken());
        // int[][] products = new int[b][3];
        // for (int i = 0; i < b; i++) {
        //     StringTokenizer st = new StringTokenizer(fin.readLine());
        //     for (int j = 0; j < 3; j++) {
        //         products[i][j] = Integer.parseInt(st.nextToken());
        //     }
        // }

        // int[][] offers = new int[s][];
        // for (int i = 0; i < s; i++) {
        //     StringTokenizer st = new StringTokenizer(offersString.get(i));
        //     int n = Integer.parseInt(st.nextToken());
        //     for (int j = 0; j++; j < n) {
        //         int c = Integer.parseInt(st.nextToken());
        //         int k = Integer.parseInt(st.nextToken());
        //         offers[i] = new int[] { c, k };
        //     }
        // }

        // PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("shopping.out")));
        // fout.close();
    }

    public int toIndex(int[] values, int[] multiplier) {
        int result = 0;
        for (int i = 0; i < values.length; i++) {
            result += values[i] * multiplier[i];
        }
        return result;
    }
}
