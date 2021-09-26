
import java.io.*;
import java.util.*;
public class sort {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("sort.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            a[i] = x;
            b[i] = x;
        }

        if (n > 10000) {
            Arrays.sort(b);
            HashMap<Integer, int[]> numbers = new HashMap<Integer, int[]>();
            int current = -1;
            int idx = -1;
            for (int i = 0; i < n; i++) {
                if (b[i] != current) {
                    numbers.put(current, new int[]{idx, i-1});
                    current = b[i];
                    idx = i;
                }
            }
            numbers.put(current, new int[]{idx, n-1});

            // System.out.println(numbers);
            // for (int k: numbers.keySet()) {
            //     System.out.println("" + k + ": " + Arrays.toString(numbers.get(k)));
            // }

            int result = 0;
            int ans = 0;
            int y = 0;
            for (int i = 0; i < n; i++) {
                int dist = 0;
                if (i > numbers.get(a[i])[1]) {
                    dist = i-numbers.get(a[i])[1];
                } else if (i < numbers.get(a[i])[0]) {
                    dist = numbers.get(a[i])[0] - i;
                }
                if (dist > result) {
                    result = dist;
                    ans = a[i];
                    y = i;
                }
            }

            result++;
            System.out.println(result);
            System.out.println("" + ans + ", " + y);
            System.out.println(Arrays.toString(numbers.get(996178)));
            PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("sort.out")));
            fout.print(result);
            fout.close();
        } else {
            int result = 0;
            boolean sorted = false;
            while (sorted == false) {
                sorted = true;
                result++;
                for (int i = 0; i < n-1; i++) {
                    // System.out.println("" + i + " " + a[i+1] + " " + a[i]);
                    if (a[i+1] < a[i]) {
                        int x = a[i+1];
                        a[i+1] = a[i];
                        a[i] = x;
                        // System.out.println(Arrays.toString(a));
                        sorted = false;
                    }
                }
            }
            PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("sort.out")));
            fout.print(result);
            fout.close();
        }
    }
}
