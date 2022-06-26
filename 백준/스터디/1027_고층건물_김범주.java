import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static long[] ar;
	static long ans = Long.MIN_VALUE;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		ar = new long[N+1];
		for (int i = 1; i <= N; i++) {
			ar[i] = Long.parseLong(st.nextToken());
		}
		for (int i = 1; i <= N; i++) {
//			System.out.println(i);


			ans = Math.max(ans, cal(i));
//			System.out.println(i + "에선 " + val);
		}
		System.out.println(ans);
	}
	
	static int cal(int i) {
		int val = 0;
		
		
		double slope = 0; // 기울기(초기화값)
		
		for (int j = i-1; j >= 1; j--) {
			// j~i 사이의 건물이 있는지 확인
			slope = (1.0)*(ar[i]-ar[j])/(i-j);
			
			if(j == i-1) {
				val++;
			}
			
			for (int k = j+1; k < i; k++) {
//				System.out.println(slope*(i-k));
				if(ar[k] >= ar[i]-(slope*(i-k))) {
					break;
				}
				if(k == i-1) {
					val++;
				}
			}
		}
		
		for (int j = i+1; j <= N; j++) {
			slope = (1.0)*(ar[j]-ar[i])/(j-i);
			if(j == i+1) {
				val++;
			}
			
			for (int k = j-1; k > i; k--) {
				if(ar[k] >= ar[i]+(slope*(k-i))) {
					break;
				}
				if(k == i+1) {
					val++;
				}
			}
		}
		
		return val;
	}
}
