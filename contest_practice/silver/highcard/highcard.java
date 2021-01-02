import java.io.*;
import java.util.*;
public class highcard {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("highcard.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        TreeSet<Integer> elsie = new TreeSet<Integer>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int a = Integer.parseInt(st.nextToken());
            elsie.add(a);
        }

        Iterator<Integer> iterator = elsie.iterator();
        Iterator<Integer> elsie_cards = elsie.iterator();
        int bessie = -1;
        int elsie_pos = -1;
        int elsie_card = elsie_cards.next();
        int result = 0;

        while (bessie < n * 2+1) {
            if (bessie == elsie_pos) {
                if (iterator.hasNext()) {
                    elsie_pos = iterator.next();
                } else {
                    elsie_pos = Integer.MAX_VALUE;
                }
                bessie++;
                continue;
            }
            // System.out.println(bessie);
            if (bessie > elsie_card){
                result++;
                if (elsie_cards.hasNext()) {
                    elsie_card = elsie_cards.next();
                } else {
                    elsie_card = Integer.MAX_VALUE;
                }
            }
            bessie++;
        }

        System.out.println(result);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("highcard.out")));
        fout.print(result);
        fout.close();

    }
}
