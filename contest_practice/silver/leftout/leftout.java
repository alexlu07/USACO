import java.io.*;
import java.util.*;
public class leftout {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("leftout.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        Boolean[][] cows = new Boolean[n][n];
        int[][] n_cows = new int[n][2];
        for (int i = 0; i < n; i++) {
            String l = fin.readLine();
            for (int j = 0; j < n; j++) {
                if (l.charAt(j) == 'L') {
                    cows[i][j] = false;
                    n_cows[i][0] ++;
                } else {
                    cows[i][j] = true;
                    n_cows[i][1] ++;
                }
            }
        }

        boolean flip = false;
        if (n_cows[0][0] < n_cows[0][1]) {
            flip = true;
        }

        for (int i = 0; i < n; i++) {
            cows[0][i] ^= flip;
            if (cows[0][i]) {
                for (int j = 0; j < n; j++) {
                    cows[j][i] ^= true;
                    if (cows[j][i] == false) {
                        n_cows[j][0]++;
                        n_cows[j][1]--;
                    } else {
                        n_cows[j][0]--;
                        n_cows[j][1]++;
                    }
                }
            }
        }

        int found = 0;
        for (int i = 1; i < n; i++) {
            if (n_cows[i][0] == 1 || n_cows[i][1] == 1) {
                found = i;
                break;
            }
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("leftout.out")));
        // System.out.println(found);
        if (found > 0) {
            if (n > 2) {
                int i = found;
                int j = -1;
                if (found < n-1) {
                    if (n_cows[found+1][0] == 1 || n_cows[found+1][0] == 1) {
                        i = 0;
                    }
                }
                for (int x = 0; x < n; x++) {
                    if (n_cows[found][0] < n_cows[found][1]) {
                        if (cows[found][x] == false) {
                            j = x;
                            break;
                        }
                    } else {
                        if (cows[found][x] == true) {
                            j = x;
                            break;
                        }
                    }
                }
                fout.print("" + (i+1) + " " + (j+1));
            } else {
                fout.print("1 1");
            }
        } else {
            fout.print(-1);
        }
        fout.close();
        // System.out.println(Arrays.deepToString(cows));

    }
}
