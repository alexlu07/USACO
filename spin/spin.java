/*
ID: alexlu.1
LANG: JAVA
TASK: spin
*/
import java.io.*;
import java.util.*;

class Wheel {
    int speed;
    int[][] cuts = new int[5][2];
    int nCuts;
    int pos = 0;

    public Wheel(int s, int n) {
        speed = s;
        nCuts = n;
    }

    public int[] getHoles(int[] holes) {
        for (int i = 0; i < nCuts; i++) {
            int degree = (pos + cuts[i][0]) % 360;
            for (int j = 0; j <= cuts[i][1]; j++) {
                holes[degree]++;
                degree = (degree + 1) % 360;
            }
        }
        return holes;
    }
}

public class spin {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("spin.in"));

        Wheel[] wheels = new Wheel[5];
        for (int wheel = 0; wheel < 5; wheel++) {
            StringTokenizer st = new StringTokenizer(fin.readLine());
            int speed = Integer.parseInt(st.nextToken());
            int wedges = Integer.parseInt(st.nextToken());
            Wheel w = new Wheel(speed, wedges);
            for (int wedge = 0; wedge < wedges; wedge++) {
                int start = Integer.parseInt(st.nextToken());
                int extent = Integer.parseInt(st.nextToken());

                w.cuts[wedge][0] = start;
                w.cuts[wedge][1] = extent;

            }

            wheels[wheel] = w;
        }

        int t = 0;
        time:
        for (; t < 360; t++) {
            int[] holes = new int[360];

            for (Wheel wheel: wheels) {
                holes = wheel.getHoles(holes);
                wheel.pos = (wheel.pos + wheel.speed) % 360;
            }

            for (int degree: holes) {
                if (degree == 5) {
                    break time;
                }
            }
        }

        System.out.println(t);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("spin.out")));
        fout.println((t < 360) ? t : "none");
        fout.close();
    }
}
