import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int T;
	static int N,M;
	static int[] coin;
	static int[] dp;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine()); // 동전의 개수
			coin = new int[N+1]; // 동전 정보 기입( 0 : 더미)
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= N; i++) {
				coin[i] = Integer.parseInt(st.nextToken());
			}
			M = Integer.parseInt(br.readLine());
			dp = new int[M+1]; // 우리가 구해야 할 목표값은 dp[M];
			dp[0] = 1; // 해당 동전을 처음 쓸 때의 값은 1이 더해져야 함.
			
			for (int i = 1; i < coin.length; i++) {
				for (int j = coin[i]; j <= M; j++) {
					dp[j] += dp[j-coin[i]];
				}
			}
			System.out.println(dp[M]);
		}
	}
}
