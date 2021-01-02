import java.io.*;
import java.util.*;
public class mountains {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("mountains.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        TreeSet<int[]> mountains = new TreeSet<>(new comp());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            mountains.add(new int[]{ x-y, x+y});
        }

        int result = 0;
        int max_end = 0;
        for (int[] l:mountains) {
            if (l[1] > max_end) {
                result++;
                max_end = l[1];
            }
        }

        System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("mountains.out")));
        fout.print(result);
        fout.close();

    }
}

class comp implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
        if (a[0] < b[0]) {
            return -1;
        }
        if (a[0] > b[0]) {
            return 1;
        }
        if (a[1] < b[1]) {
            return 1;
        }
        if (a[1] > b[1]) {
            return -1;
        }

        return 0;
    }
}
