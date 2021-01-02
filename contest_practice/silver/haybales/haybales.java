import java.io.*;
import java.util.*;
public class haybales {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("haybales.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] haybales = new int[n];

        st = new StringTokenizer(fin.readLine());
        for (int i = 0; i < n; i++) {
            haybales[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(haybales);

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("haybales.out")));
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(fin.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (i > 0) {
                fout.print("\n");
            }

            fout.print(search(haybales, b) - search(haybales, a-1));

        }

        fout.close();
    }

    public static int search(int[] list, int x) {
        if(list[0] > x) {
            return 0;
        }
        int min = 0;
        int max = list.length-1;
        while(min != max) {
            int mid = (min+max+1)/2;
            if(list[mid] <= x) {
                min = mid;
            }
            else {
                max = mid-1;
            }
        }
        return min + 1;
    }
}
