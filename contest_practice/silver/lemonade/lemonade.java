import java.io.*;
import java.util.*;
public class lemonade {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("lemonade.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(fin.readLine());
        Integer[] nums = new Integer[n];
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            nums[i] = x;
        }
        Arrays.sort(nums, Collections.reverseOrder());
        // System.out.println(Arrays.toString(nums));
        int i1 = 0;
        int i2 = n;
        int c = 0;
        while (i1 < i2) {
            // System.out.println("" + i1 + " " + i2);
            i1++;
            c++;
            for (;nums[i2-1] < c; i2--);


        }
        System.out.println(c);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("lemonade.out")));
        fout.print(c);
        fout.close();
    }
}
