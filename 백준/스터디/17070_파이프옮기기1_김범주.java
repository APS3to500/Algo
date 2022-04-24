// DFS

// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.util.Stack;
// import java.util.StringTokenizer;

// public class 11070_파이프옮기기1 {
// 	static int N;
// 	static Stack<p> stack = new Stack<p>();
// 	static int[] dy = {0,1,1};
// 	static int[] dx = {1,1,0};
// 	static int[][] ar;
// 	static int ans;
// 	public static void main(String[] args) throws Exception{
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		N = Integer.parseInt(br.readLine());
		
// 		ar = new int[N+1][N+1];
		
// 		for (int i = 1; i <= N; i++) {
// 			StringTokenizer st= new StringTokenizer(br.readLine());
// 			for (int j = 1; j <= N; j++) {
// 				ar[i][j] = Integer.parseInt(st.nextToken());
// 			}
// 		}
// 		stack.push(new p(1,2,0));
// 		if(ar[N][N] == 1) {
// 			System.out.println(0); // 너무 양아치 아니냐...
// 			return;
// 		}
		
// 		dfs();
// 		System.out.println(ans);

// 	}
// 	static void dfs() {
// 		while(!stack.isEmpty()) {
// 			p a = stack.pop();
// //			System.out.println(a.y + " " + a.x);
// 			for (int i = 0; i < 3; i++) {
// 				int ny = a.y + dy[i];
// 				int nx = a.x + dx[i];
// 				if(ny <= 0 || ny > N || nx <= 0 || nx > N || ar[ny][nx] == 1) continue;
// 				if(a.d == 0) { //앞쪽 및 대각선만 이동 가능
// 					if(i == 2) continue;
// 				}
// 				else if(a.d == 2) { // 세로일 때 : 아랫쪽및 대각선만 이동 가능
// 					if(i == 0) continue;
// 				}
				
// 				if(i == 1) {
// 					if(ar[a.y][nx] == 1 || ar[ny][a.x] == 1 || ar[ny][nx] == 1) continue;
// 				}

// 				if(ny == N && nx == N) {
// 					ans++;
// 				}
// 				else {
// 					stack.push(new p(ny,nx,i));
// 				}
// 			}
// 		}
// 	}
	
// 	static class p {
// 		int y;
// 		int x;
// 		int d;
// 		public p(int y, int x, int d) {
// 			super();
// 			this.y = y;
// 			this.x = x;
// 			this.d = d;
// 		}
		
		
// 	}
// }

//DP_누적합

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_dp_누적합 {
	static long[][] ar;
	static int N;
	static long ans;
	static long[][][] dp;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		ar = new long[N+1][N+1];
		dp = new long[3][N+1][N+1];
		
		for (int i = 1; i <= N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				ar[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 1; i <= N; i++) {
			if(ar[1][i] == 1) break;
			dp[0][1][i] = 1;
		}
		
			// 0: 가로, 1: 세로, 2 : 대각선
			for (int i = 2; i <= N; i++) {
				for (int j = 3; j <= N; j++) {
					if(ar[i][j] == 1) continue;
						// 가로
						dp[0][i][j] = dp[0][i][j-1]+dp[2][i][j-1];
						
						//세로
						dp[1][i][j] = dp[1][i-1][j]+dp[2][i-1][j];
						
						// 대각선
						if(ar[i-1][j] ==0 && ar[i][j-1] == 0)
						dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1];
					
				}
			}
		
			for (int i = 0; i < 3; i++) {
				ans += dp[i][N][N];
			}
		System.out.println(ans);
	}

	
}

// DP_재귀

// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.util.StringTokenizer;

// public class Main_dp_재귀 {
// 	static int[][] ar;
// 	static int N,ans;
// 	public static void main(String[] args) throws Exception{
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
// 		N = Integer.parseInt(br.readLine());
// 		ar = new int[N+1][N+1];
		
// 		for (int i = 1; i <= N; i++) {
// 			StringTokenizer st = new StringTokenizer(br.readLine());
// 			for (int j = 1; j <= N; j++) {
// 				ar[i][j] = Integer.parseInt(st.nextToken());
// 			}
// 		}
// 		dp(1,2,1);

// 		System.out.println(ans);
// 	}

// 	static void dp(int y,int x,int dir) { // dir의 경우, 1 : 가로, 2 : 대각선, 3 ㅣ 세로
// 		if(y == N && x == N && ar[y][x] != 1) {
// 			ans++;
// 			return;
// 		}
// 		int ny = y+1;
// 		int nx = x+1;
		
// 		// 가로로 갈 수 있는 경우
// 		if(x < N && ar[y][nx] != 1 && dir != 3) dp(y,nx,1);
		
// 		// 대각선으로 갈 수 있는 경우
// 		if(y < N && x < N && ar[ny][x] != 1 && ar[y][nx] != 1 && ar[ny][nx] != 1) dp(ny,nx,2);
// 		// 세로로 갈 수 있는 경우
// 		if(y < N && ar[ny][x] != 1 && dir != 1) dp(ny,x,3);
// 	}
// }
