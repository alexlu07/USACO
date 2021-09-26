import java.io.*;
import java.util.*;
public class lifeguards {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("lifeguards.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        TreeSet<int[]> timeline = new TreeSet<int[]>(new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b) {
                    return a[0] - b[0];
                }
            });
        int[][] guards = new int[n][2];
        int[] time = new int[n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            guards[i][0] = s;
            guards[i][1] = e;

            timeline.add(new int[]{s, i, 0});
            timeline.add(new int[]{e, i, 1});
        }

        int alone = -1;
        int working = -1;
        HashSet<Integer> active = new HashSet<Integer>();
        for (int[] p: timeline) {
            // System.out.println(alone);
            if (p[2] == 0) {
                // for (int a: active) {
                //     int overlap = Math.min(guards[p[1]][1], guards[a][1]) - Math.max(guards[p[1]][0], guards[a][0]);
                //     if (overlap > 0) {
                //         total -= overlap;
                //         time[a] -= overlap;
                //         if (time[a] < result) {
                //             result = time[a];
                //         }
                //         time[p[1]] -= overlap;
                //         if (time[p[1]] < result) {
                //             result = time[p[1]];
                //         }
                //     }
                // }
                if (active.isEmpty()) {
                    alone = p[0];
                    working = p[0];
                } else if (active.size() == 1) {
                    int x = active.iterator().next();
                    time[x] += p[0] - alone;
                    // System.out.println(p[0]);
                    alone = -1;

                }
                active.add(p[1]);
            } else {
                active.remove(p[1]);
                if (active.size() == 1) {
                    alone = p[0];
                } else if (active.isEmpty()) {
                    time[p[1]] += p[0] - alone;
                    // System.out.println(p[0]);
                    total += p[0] - working;
                    working = -1;
                    alone = -1;
                }
            }
        }

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (time[i] < result) {
                result = time[i];
            }
        }
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("lifeguards.out")));
        fout.print(total - result);
        fout.close();
        // System.out.println(total - result);
        // System.out.println(Arrays.toString(time));
        // System.out.println(total);
        // System.out.println(result);
    }
}
