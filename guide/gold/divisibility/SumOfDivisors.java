import java.io.*;
import java.util.*;

public class SumOfDivisors {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        fin.close();

        long sum = 0;
        for (int i = 1; i * i < n; i++) {
            int terms = n / i;
            sum += (terms-i+1) * i;
            if (terms > i) {
                sum += (terms-i) * (i+1 + terms) / 2;
            }
        }

        System.out.println(sum);
    }
}