import java.io.*;
import java.util.*;

public class pairedup {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("pairedup.in"));
        // BufferedReader fin = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        
        int[] numbers = new int[n];
        int[] key = new int[n+1];
        st = new StringTokenizer(fin.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            numbers[i] = x;
            key[x] = i;
        }

        fin.close();

        int[][] hilos = new int[n][4];
        LinkedList<int[]> curr_hilos = new LinkedList<int[]>();

        for (int i = 1; i < n; i++) {
            
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("structure.out")));
        fout.println();
        fout.close();
    }
}
