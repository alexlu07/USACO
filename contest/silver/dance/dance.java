import java.io.*;
import java.util.*;
public class dance {
    public static void main(String args[]) throws IOException {
        Scanner ip = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(ip.nextLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // ArrayList<HashSet<Integer>> places = new ArrayList<HashSet<Integer>>();
        ArrayList<HashSet<Integer>> visits = new ArrayList<HashSet<Integer>>();
        int[] locs = new int[n];
        for (int i = 0; i < n; i++) {
            HashSet<Integer> hs = new HashSet<Integer>();
            // hs.add(i);
            // places.add(hs);
            visits.add(new HashSet<Integer>());
            locs[i] = i;
        }

        for (int i = 0; i < k; i++) {
            // System.out.println(Arrays.toString(locs));
            st = new StringTokenizer(ip.nextLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;
            visits.get(locs[a]).add(b);
            visits.get(locs[b]).add(a);
            int x = locs[a];
            locs[a] = locs[b];
            locs[b] = x;
        }

        // System.out.println(Arrays.toString(locs));
        // System.out.println(visits);
        int[] new_locs = new int[n];
        for (int i = 0; i < n; i++) {
            new_locs[locs[i]] = i;
        }
        // System.out.println(Arrays.toString(new_locs));
        int[] cows = new int[n];

        for (int i = 0; i < n; i++) {
            if (cows[i] > 0) {
                continue;
            }
            HashSet<Integer> p = new HashSet<Integer>();
            p.add(i);
            int pos = i;
            int first = 1;
            ArrayList<Integer> neighbors = new ArrayList<Integer>();
            // System.out.println("-------" + i + "------------");
            while (first == 1 || pos != i) {
                first = 0;
                // System.out.println(pos);
                // System.out.println(places.get(i));
                // System.out.println(visits.get(pos));
                p.addAll(visits.get(pos));
                pos = new_locs[pos];
                neighbors.add(pos);
            }
            int s = p.size();
            cows[i] = s;
            for (int j: neighbors) {
                cows[j] = s;
            }
            // System.out.println(places.get(i).size());
        }

        for (int i = 0; i < n; i++) {
            System.out.println(cows[i]);
        }
        // System.out.println(places);



    }
}
