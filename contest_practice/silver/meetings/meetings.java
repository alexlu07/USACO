public class meetings {
    public static void main(String args[]) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("meetings.in"));
        StringTokenizer st = new StringTokenizer(fin.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        

        PrintWriter fout = new PrintWriter(new BufferedWriter(new FileWriter("meetings.out")));
        fout.println(result);
        fout.close();
        
    }
}
