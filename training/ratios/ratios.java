/*
ID: alexlu.1
LANG: JAVA
TASK: ratios
*/
import java.io.*;
import java.util.*;

public class ratios {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("ratios.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        double a = Integer.parseInt(st.nextToken());
        double b = Integer.parseInt(st.nextToken());
        double c = Integer.parseInt(st.nextToken());
        double s = a + b + c;

        // a = (a > 0) ? a:-1;
        // b = (b > 0) ? b:-1;
        // c = (c > 0) ? c:-1;

        int[][] mixtures = new int[3][3];
        for (int mixture = 0; mixture < 3; mixture++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            mixtures[mixture][0] = x;
            mixtures[mixture][1] = y;
            mixtures[mixture][2] = z;

        }

        int resultSum = 301;
        int[] result = new int[3];
        double m = 0;
        for (int p = 0; p < 100; p++) {
            for (int q = 0; q < 100; q++) {
                for (int r = 0; r < 100; r++) {

                    if (p + q + r > resultSum) {
                        break;
                    }

                    double totalA = p * mixtures[0][0] + q * mixtures[1][0] + r * mixtures[2][0];
                    double totalB = p * mixtures[0][1] + q * mixtures[1][1] + r * mixtures[2][1];
                    double totalC = p * mixtures[0][2] + q * mixtures[1][2] + r * mixtures[2][2];

                    // totalA = (totalA > 0) ? totalA:-1;
                    // totalB = (totalB > 0) ? totalB:-1;
                    // totalC = (totalC > 0) ? totalC:-1;

                    double multiplier = (totalA + totalB + totalC) / s;

                    if (multiplier >= 1 &&
                        totalA == multiplier * a &&
                        totalB == multiplier * b &&
                        totalC == multiplier * c) {

                        resultSum = p + q + r;
                        result[0] = p;
                        result[1] = q;
                        result[2] = r;

                        m = multiplier;


                    }

                }
            }
        }

        for (int x: result) {
            System.out.println(x);
        }

        int x = (int) m;
        System.out.println(x);

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("ratios.out")));
        if (resultSum < 301) {
            fout.printf("%s %s %s %s\n", result[0], result[1], result[2], x);
        } else {
            fout.println("NONE");
        }

        fout.close();

    }
}
