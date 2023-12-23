import java.io.*;
import java.util.*;

public class united {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("united.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[] nums = new int[n];
        int[] used = new int[n];
        StringTokenizer st = new StringTokenizer(fin.readLine());
        nums[0] = Integer.parseInt(st.nextToken())-1;;
        int first = 0;
        for (int i = 1; i < n; i++) {
            int x = Integer.parseInt(st.nextToken())-1;
            used[x]++;
            nums[i] = x;

            if (nums[first] == x) {
                used[x]--;
                while (used[nums[first]] > 0) {
                    first++;
                }
            }



        }

    }
}
