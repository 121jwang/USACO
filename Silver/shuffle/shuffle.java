import java.io.*;
import java.util.*;
public class shuffle {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("shuffle.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("shuffle.out")));
		int n = Integer.parseInt(br.readLine());
		int[] to = new int[n];
		int[] parent = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			to[i] = Integer.parseInt(st.nextToken())-1;
			parent[to[i]]++;
		}
		int ret = n;
		LinkedList<Integer> q = new LinkedList<Integer>();
		for(int i = 0; i < n; i++) {
			if(parent[i] == 0) {
				q.add(i);
				ret--;
			}
		}
		while(!q.isEmpty()) {
			int curr = q.removeFirst();
			if(--parent[to[curr]] == 0) {
				q.add(to[curr]);
				ret--;
			}
		}
		pw.println(ret);
		pw.close();
	}
}
