/*
ID: alexlu.1
LANG: JAVA
TASK: structure
*/
import java.io.*;
import java.util.*;

public class findandreplace {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("structure.in"));
        // BufferedReader fin = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        System.out.println(n);
        fin.close();

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("structure.out")));
        fout.println();
        fout.close();
    }
}
