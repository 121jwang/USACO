import java.io.*;
import java.util.*;
public class meeting {
  static int[][] bessieGrid;
  static int[][] elsieGrid;

  static int n;
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader("meeting.in"));
    PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("meeting.out")));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    bessieGrid = new int[n][n];
    elsieGrid = new int[n][n];
    for(int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken())-1;
      int y = Integer.parseInt(st.nextToken())-1;
      bessieGrid[x][y] = Integer.parseInt(st.nextToken());
      elsieGrid[x][y] = Integer.parseInt(st.nextToken());
    }
    boolean[] bessieCan = solve(bessieGrid);
    boolean[] elsieCan = solve(elsieGrid);
    int best = Integer.MAX_VALUE;
    for(int i = 0; i < bessieCan.length; i++) {
      if(bessieCan[i] && elsieCan[i]) {
        best = i;
        break;
      }
    }
    if(best == Integer.MAX_VALUE) {
      pw.println("IMPOSSIBLE");
    }
    else {
      pw.println(best);
    }
    pw.close();
  }

  public static boolean[] solve(int[][] dist) {
    boolean[][] dp = new boolean[n][100*n+1];
    dp[0][0] = true;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < dp[i].length; j++) {
        if(!dp[i][j]) continue;
        for(int k = i+1; k < n; k++) {
          if(dist[i][k] > 0) {
            dp[k][j + dist[i][k]] = true;
          }
        }
      }
    }
    return dp[n-1];
  }
}
