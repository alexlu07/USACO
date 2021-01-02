/*
ID: alexlu.1
LANG: JAVA
TASK: fact4
*/
import java.io.*;
import java.util.*;

class fact4 {
    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("fact4.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        System.out.println(n);

        int twos = 0;
        int fives = 0;
        int result = 1;
        for (int i = 2; i <= n; i++) {
            int j = i;

            while (j % 2 == 0) {
                twos++;
                j /= 2;
            }

            while (j % 5 == 0) {
                fives++;
                j /= 5;
            }

            result = (result * j) % 10;

        }

        for (int i = 0; i < twos-fives; i++) {
            result = (result * 2) % 10;
        }

        System.out.println(result);

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("fact4.out")));
        fout.printf("%d\n", result);
        fout.close();

    }
}
