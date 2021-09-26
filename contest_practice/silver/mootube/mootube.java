import java.io.*;
import java.util.*;
public class mootube {
    static ArrayList<HashMap<Integer, Integer>> neighbors = new ArrayList<HashMap<Integer, Integer>>();

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("mootube.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            neighbors.add(new HashMap<Integer, Integer>());
        }
        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(fin.readLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;
            int c = Integer.parseInt(st.nextToken());
            neighbors.get(a).put(b, c);
            neighbors.get(b).put(a, c);
        }

        // System.out.println(neighbors);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("mootube.out")));
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(fin.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken())-1;
            if (i > 0) {
                fout.println();
            }
            fout.print(solve(k, v));
        }
        fout.close();
    }

    public static int solve(int k, int v) {
        int result = 0;
        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(v);
        HashSet<Integer> visited = new HashSet<Integer>();
        visited.add(v);
        while (queue.size() > 0) {
            // System.out.println(queue);
            int i = queue.pop();
            result++;
            
            for (int j: neighbors.get(i).keySet()) {
                if (neighbors.get(i).get(j) >= k && visited.contains(j) == false) {
                    // System.out.println("" + i + " " + j + " " + k);
                    queue.add(j);
                    visited.add(j);
                }
            }
        }
        return result-1;
    }
}
