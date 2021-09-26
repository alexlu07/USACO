/*
  ID: alexlu.1
  LANG: JAVA
  TASK: camelot
*/
import java.io.*;
import java.util.*;

public class camelot {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("camelot.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(fin.readLine());
        int[] king = new int[2];
        king[0] = Integer.parseInt(st.nextToken());
        king[1] = Integer.parseInt(st.nextToken());


        String line;
        while ((line = f.readLine()) != null) {
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int j = Integer.parseInt(st.nextToken());
                int i = Integer.parseInt(st.nextToken());
            }


        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("camelot.out")));
        fout.println();
        fout.close();
    }
}
