import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] ar;
	static long sum; // 누적합
	static long ans = Long.MIN_VALUE;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine()); // N의 범위가 1이상 1000이하 => 브루트포스(O(N)) 하면 에러 발생할듯
		// 배열 입력 및 정렬 후, 현재 보고 있는 추(i번째 추)의 무게, j번째 추의 무게만 더한 무게
		ar = new int[N+1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			ar[i] = Integer.parseInt(st.nextToken());
		}
		ar[N] = Integer.MAX_VALUE;
		Arrays.sort(ar);
		
		for (int i = 0; i <= N; i++) {
			if(ar[i] > sum+1) {
				ans = sum+1;
				break;
			}
			sum += ar[i];
		}
		
		System.out.println(ans);
	}
}
