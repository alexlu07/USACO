/*
ID: Alex.1
LANG: JAVA
TASK: msquare
*/
import java.io.*;
import java.util.*;

class Square {
    private int[] numbers;
    private String transformations;

    public Square(String t, int[] n) {
        numbers = n;
        transformations = t;

    }

    public Square flip() {
        return new Square(transformations + "A", new int[]{ numbers[7], numbers[6], numbers[5], numbers[4], numbers[3], numbers[2], numbers[1], numbers[0] });
    }

    public Square shift() {
        return new Square(transformations + "B", new int[]{ numbers[3], numbers[0], numbers[1], numbers[2], numbers[5], numbers[6], numbers[7], numbers[4] });
    }

    public Square turn() {
        return new Square(transformations + "C", new int[]{ numbers[0], numbers[6], numbers[1], numbers[3], numbers[4], numbers[2], numbers[5], numbers[7] });
    }

    public String toString() {
        return "" + transformations;

    }

    public int toInt() {
        int result = 0;
        for (int n: numbers) {
            result *= 10;
            result += n;
        }

        return result;

    }

}

public class msquare {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("msquare.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int goal = 0;
        for (int i = 0; i < 8; i++) {
            goal *= 10;
            goal += Integer.parseInt(st.nextToken());
        }

        fin.close();

        String result;

        TreeSet<Integer> explored = new TreeSet<Integer>();
        explored.add(12348765);

        Queue<Square> queue = new LinkedList<>();
        queue.add(new Square("", new int[]{ 1, 2, 3, 4, 5, 6, 7, 8 }));
        while (true) {
            // if (queue.toString().length() < 100) {
            //     System.out.println(queue);
            // } else {
            //     System.out.println(queue.toString().substring(0, 100));
            // }

            Square arrangement = queue.remove();
            if (arrangement.toInt() == goal) {
                result = arrangement.toString();
                break;
            }

            // System.out.println(arrangement);

            // if (arrangement.toString().equals("BCABCCB")) {
            //     result = arrangement.toString();
            //     System.out.println("yay");
            //     System.out.println(arrangement.toInt());
            //     break;
            // }

            Square flipped = arrangement.flip();
            if (explored.add(flipped.toInt())) {
                queue.add(flipped);
            }

            Square shifted = arrangement.shift();
            if (explored.add(shifted.toInt())) {
                queue.add(shifted);
            }

            Square turned = arrangement.turn();
            if (explored.add(turned.toInt())) {
                queue.add(turned);
            }

        }

        // System.out.println(result);

        // Square s = new Square("", new int[]{ 1, 2, 3, 4, 5, 6, 7, 8 });
        // System.out.println(s.toInt());
        // System.out.println(s.shift().toInt());
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("msquare.out")));
        fout.println(result.length());
        fout.println(result);
        fout.close();
    }
}


/*
1 2 3 4
8 7 6 5
1 2 3 4 5 6 7 8

4 1 2 3
5 8 7 6
4 1 2 3 6 7 8 5

4 8 1 3
5 7 2 6
4 8 1 3 5 7 2 6

5 7 2 6
4 8 1 3
5 7 2 6 3 1 8 4

6 5 7 2
3 4 8 1

6 8 4 2
3 7 8 1

2 6 8 4
1 3 7 8


 */
