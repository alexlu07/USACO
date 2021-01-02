/*
ID: alexlu.1
LANG: JAVA
TASK: stamps
*/

import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.io.FileWriter;
import java.io.IOException;

public class stamps {

    public static void main(String[] args) {
        try {
            File fin = new File("stamps.in");
            Scanner sc = new Scanner(fin);

            int k = sc.nextInt();
            int n = sc.nextInt();
            int[] stamps = new int[n];
            int biggest = -1;

            for (int i = 0; i < n; i++) {
                int stamp = sc.nextInt();
                stamps[i] = stamp;
                if (biggest < stamp) {
                    biggest = stamp;
                }
            }

            sc.close();

            System.out.printf("%s %s\n", k, n);
            System.out.println(Arrays.toString(stamps));
            int[] values = new int[biggest * (k+1) + 2];
            Arrays.fill(values, Integer.MAX_VALUE);
            values[0] = 0;

            int i = 0;
            while (values[i] <= k) {
                for (int stamp:stamps) {
                    if (values[i] + 1 < values[i+stamp]) {
                        values[i+stamp] = values[i] + 1;
                    }
                }

                i ++;
            }

            i--;
            System.out.println(i);

            FileWriter fout = new FileWriter("stamps.out");
            fout.write(String.valueOf(i));
            fout.write('\n');
            fout.close();
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
