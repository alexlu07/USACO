import java.io.*;
import java.util.*;
public class milkvisits {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("milkvisits.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] type = new int[n];
        st = new StringTokenizer(fin.readLine());
        for (int i = 0; i < n; i++) {
            type[i] = Integer.parseInt(st.nextToken());
        }

        int[][] neighbors = new int[n][n];
        int[] n_neighbors = new int[n];
        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            neighbors[x][n_neighbors[x]] = y;
            neighbors[y][n_neighbors[y]] = x;
            n_neighbors[x]++;
            n_neighbors[y]++;
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(0);
        int[] parent = new int[n];
        int[] visited = new int[n];
        ArrayList<HashMap<Integer, Integer>> types = new ArrayList<HashMap<Integer, Integer>>(Collections.nCopies(n, new HashMap<Integer,Integer>()));
        while (queue.size() > 0) {
            int i = queue.poll();
            visited[i] = 1;
            HashMap<Integer, Integer> hm = null;
            if (i != 0) {
                // System.out.println(types.get(parent[i]));
                hm = (HashMap<Integer, Integer>) types.get(parent[i]).clone();
            } else {
                hm = types.get(i);
            }
            hm.put(type[i], hm.getOrDefault(type[i], 0) + 1);
            types.set(i, hm);
            for (int j = 0; j < n_neighbors[i]; j++) {
                if (visited[neighbors[i][j]] == 0) {
                    queue.add(neighbors[i][j]);
                }
            }
        }

        System.out.println(types);
        // PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("milkvisits.out")));
        // fout.print("" + efficiency[n-1]);
        // fout.close();
    }
}
