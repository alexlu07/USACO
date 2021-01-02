/*
ID: alexlu.1
LANG: JAVA
TASK: fence
*/
import java.io.*;
import java.util.*;

class NodeComparator implements Comparator {

    public int compare(Object a, Object b) {
        return ((Node) a).id - ((Node) b).id;
    }
}

class Node {
    public int id = -1;
    public PriorityQueue<Node> neighbors = new PriorityQueue<Node>(new NodeComparator());
    public int nNeighbors = 0;

    public Node(int i) {
        id = i;
    }

    public void addNeighbor(Node j) {
        neighbors.add(j);
        nNeighbors += 1;
    }

    public Node popNeighbor() {
        Node j = neighbors.poll();
        nNeighbors -= 1;

        j.neighbors.remove(this);
        j.nNeighbors -= 1;

        return j;
    }

    public String toString() {
        return "" + id;
    }

}

public class fence {
    public static ArrayList<Integer> circuit = new ArrayList<Integer>();
    // public static int[][] neighbors = new int[501][501];
    // public static int[] nNeighbors = new int[501];

    public static void findCircuit(Node i) {
        // System.out.println(circuit);
        // System.out.println(i.neighbors + " " + i.nNeighbors);
        if (i.nNeighbors == 0) {
            // System.out.println("Circuit added " + i.id);
            circuit.add(i.id);
        } else {
            while (i.nNeighbors > 0) {
                // System.out.println(Arrays.toString(Arrays.copyOfRange(nNeighbors, 0, 10)));
                // System.out.println(i.neighbors);
                Node j = i.popNeighbor();
                // System.out.println("" + i.id + " " + j.id);
                // System.out.println
                findCircuit(j);
                // System.out.println("finished one neightbo");
            }
            // System.out.println("Circuit Done added " + i.id);
            circuit.add(i.id);
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("fence.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int f = Integer.parseInt(st.nextToken());

        Node[] nodes = new Node[501];
        for (int i = 1; i < 501; i++) {
            nodes[i] = new Node(i);
        }

        int[] n = new int[501];

        for (int i = 0; i < f; i++) {
            st = new StringTokenizer(fin.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[x].addNeighbor(nodes[y]);
            nodes[y].addNeighbor(nodes[x]);

            n[x] += 1;
            n[y] += 1;
        }

        // System.out.println(Arrays.toString(neighbors[7]));
        Node start = null;
        for (int i = 1; i < 501; i++) {
            if (n[i] % 2 == 1) {
                start = nodes[i];
                break;
            }
        }
        if (start == null) {
            for (int i = 1; i < 501; i++) {
                if (n[i] > 0) {
                    start = nodes[i];
                    break;
                }
            }
        }
        findCircuit(start);

        System.out.println(circuit);
        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("fence.out")));
        for (int i = circuit.size() - 1; i >= 0; i--) {
            fout.println(circuit.get(i));
        }
        fout.close();

    }
}
