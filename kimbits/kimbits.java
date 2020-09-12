/*
ID: alexlu.1
LANG: JAVA
TASK: kimbits
*/
import java.io.*;
import java.util.*;

class kimbits {
    static long[][] sizeOfSet = new long[33][33];

    public static void initSizeOfSet() {
        for (int j = 0; j <= 32; j++) {
            sizeOfSet[0][j] = 1;

        }

        for (int i = 1; i <= 32; i++) {
            for (int j = 0; j <= 32; j++) {
                if (j == 0) {
                    sizeOfSet[i][j] = 1;

                } else {
                    sizeOfSet[i][j] = sizeOfSet[i-1][j-1] + sizeOfSet[i-1][j];

                }
            }
        }
    }

    public static void printbits(int nbits, int nones, double index, PrintWriter fout) {
        if (nbits == 0) {
            return;
        }

        long s = sizeOfSet[nbits-1][nones];
        if (s <= index) {
            fout.printf("1");
            printbits(nbits-1, nones-1, index-s, fout);

        } else {
            fout.printf("0");
            printbits(nbits-1, nones, index, fout);

        }
    }



    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("kimbits.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int nbits = Integer.parseInt(st.nextToken());
        int nones = Integer.parseInt(st.nextToken());
        long index = Long.parseLong(st.nextToken());

        initSizeOfSet();
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("kimbits.out")));
        printbits(nbits, nones, index-1, fout);
        fout.printf("\n");
        fout.close();

    }
}
