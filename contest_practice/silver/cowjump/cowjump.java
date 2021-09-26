import java.io.*;
import java.util.*;
public class cowjump {
    static boolean onSegment(Point p, Point q, Point r) {
        if (q.x <= Math.max(p.x, r.x) && q.x >= Math.min(p.x, r.x) &&
            q.y <= Math.max(p.y, r.y) && q.y >= Math.min(p.y, r.y))
            return true;
        return false;
    }

    static int orientation(Point p, Point q, Point r) {
        long val = (q.y - p.y) * (r.x - q.x) -
            (q.x - p.x) * (r.y - q.y);
        if (val == 0) return 0;
        return (val > 0)? 1: 2;
    }

    static boolean doIntersect(Point p1, Point q1, Point p2, Point q2) {
        int o1 = orientation(p1, q1, p2);
        int o2 = orientation(p1, q1, q2);
        int o3 = orientation(p2, q2, p1);
        int o4 = orientation(p2, q2, q1);

        if (o1 != o2 && o3 != o4)
            return true;
        if (o1 == 0 && onSegment(p1, p2, q1)) return true;
        if (o2 == 0 && onSegment(p1, q2, q1)) return true;
        if (o3 == 0 && onSegment(p2, p1, q2)) return true;
        if (o4 == 0 && onSegment(p2, q1, q2)) return true;

        return false;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("cowjump.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        Point[][] lines = new Point[n][2];
        TreeSet<Point> x_sorted = new TreeSet<Point>(new XSort());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(fin.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            lines[i][0] = new Point(x1, y1, i);
            lines[i][1] = new Point(x2, y2, i);
            x_sorted.add(lines[i][0]);
            x_sorted.add(lines[i][1]);
        }

        int l1 = 0;
        int l2 = 0;
        TreeSet<Integer> active = new TreeSet<Integer>();
        for (Point i: x_sorted) {
            if (active.contains(i.s)) {
                Integer before = active.lower(i.s);
                Integer after = active.higher(i.s);
                if (before != null && after != null) {
                    if (doIntersect(lines[before][0], lines[before][1], lines[after][0], lines[after][1])) {
                        l1 = before;
                        l2 = after;
                        break;
                    }
                }
                active.remove(i.s);
            } else {
                Integer before = active.lower(i.s);
                Integer after = active.higher(i.s);
                if (before != null) {
                    if (doIntersect(lines[i.s][0], lines[i.s][1], lines[before][0], lines[before][1])) {
                        l1 = i.s;
                        l2 = before;
                        break;
                    }
                }
                if (after != null) {
                    if (doIntersect(lines[i.s][0], lines[i.s][1], lines[after][0], lines[after][1])) {
                        l1 = i.s;
                        l2 = after;
                        break;
                    }
                }
                active.add(i.s);
            }
        }

        if (l1 > l2) {
            int temp = l1;
            l1 = l2;
            l2 = temp;
        }
        System.out.println(l1);
        System.out.println(l2);

        int n_l2 = 0;
        for (int i = 0; i < n; i++) {
            if (i != l2 && doIntersect(lines[i][0], lines[i][1], lines[l2][0], lines[l2][1])) {
                n_l2++;
            }
        }

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("cowjump.out")));
        if (n_l2 > 1) {
            fout.print(l2+1);
        } else {
            fout.print(l1+1);
        }
        fout.close();
    }
}

class Point {
    long x;
    long y;
    int s;
    public Point(long x, long y, int s) {
        this.x = x;
        this.y = y;
        this.s = s;
    }
}

class XSort implements Comparator<Point> {
    public int compare(Point a, Point b) {
        if (a.x - b.x < 0) {
            return -1;
        } else if (a.x - b.x > 0) {
            return 1;
        }
        return 0;
    }
}
