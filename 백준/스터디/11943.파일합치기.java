import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int T,N;
	static long ans = Long.MAX_VALUE;
	static int sum;
	static long[][] dp;
	static int[] ar;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			ar = new int[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				ar[i] = Integer.parseInt(st.nextToken());
			}
			dp = new long[N][N];
			///ij

			for (int j = 1; j < N; j++) {
				for (int i = j-1; i >= 0; i--) { //[0][2]
					// i와 j의 차이만큼 수를 돌려봐야 함.
					dp[i][j] = Long.MAX_VALUE;
					for (int d = 0; d < j-i; d++) { //1 max(dp[0][0] + dp[1][2] // dp[0][1] + dp[2][2] 
						// [0][3] 구하기, dp[0][0] + dp[1][3] // dp[0][1] + dp[2][3] // dp[0][2] + dp[3][3]
						dp[i][j] = Math.min(dp[i][j], dp[i][i+d] + dp[i+d+1][j]);
					}
					for (int k = i; k <= j; k++) {
						//합치는 박스들 값을 모두 더해줌
						dp[i][j] += ar[k];
					}
				}
			}
			System.out.println(dp[0][N-1]);
		}
		// A : 40, B : 30, C : 30, D : 50
		/*
		 	A	B	C		D
		 	
		 A	0	AB	BC+ABC	AB+CD+ABCD [0][3]
		 
		 B		0	BC		BC+BCD
		 
		 C			0		CD
		 
		 D					0
		 */
		
		/*
		 for (int j = 1; j < N; j++) {
				for (int i = j-1; i >= 0; i--) { //[0][2]
					// i와 j의 차이만큼 수를 돌려봐야 함.
					dp[i][j] = Long.MAX_VALUE;
					for (int d = 0; d < j-i; d++) { 
						// [0][2] 구하기, (dp[0][0] + dp[1][2](BC) // dp[0][1] + dp[2][2](AB) ==> for문으로 구하기
						// [0][3] 구하기, dp[0][0] + dp[1][3] // dp[0][1] + dp[2][3] // dp[0][2] + dp[3][3]
						
						dp[i][j] = Math.min(dp[i][j], dp[i][i+d] + dp[i+d+1][j]);
					}
					for (int k = i; k <= j; k++) {
						//합치는 박스들 값을 모두 더해줌
						dp[i][j] += ar[k];
					}
				}
			}
		 */
	}
}
