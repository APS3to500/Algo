import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static String[] a,b;
	static int max;
	static int[][] ar;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		a = br.readLine().split("");
		b = br.readLine().split("");
		ar = new int[a.length][b.length];
		
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < b.length; j++) {
				if(i == 0) {
					if(a[i].equals(b[j])) ar[i][j] = 1;
				}
				else {
					if(a[i].equals(b[j])) {
						if(j ==0) ar[i][j] = 1;
						else {
							ar[i][j] = ar[i-1][j-1]+1;
						}
					}
				}
				max = Math.max(max, ar[i][j]);
			}
		}
		//두 문자열의 공통 부분 문자열 중 가장 긴 녀석을 꺼내야 함
		/*
		 공통 부분 문자열이 뭐지?
		 문자열의 일부만 꺼내면 그게 결국 부분 문자열인건가?
		 단순 브루트포스 풀이
		 a와 b의 길이를 구하고 둘 중 작은 값을 공통 부분 문쟈열의 최대 길이로 잡음
		 a>b 라 가정하고 슬라이딩 윈도우를 활용하여 문자열을 새로 갱신시킴(부분 문자열이기 때문에 앞의 한글자를 자르고 뒤의 한글자릏 넣는 형식으로)
		 길이 1부터 b의 길이까지 확인하면서 문자열을 검사
		 공통 문자열이 존재함을 확인하면 바로 다음 길이로 넘어가기
		 - 길이 n에서 더이상 공통되는 문자열이 확인되지 않을 경우 n-1이 최대 길이가 됨.
		 최대 길이 4000일 경우, ABCDEA...AAA // ABCDEA...AAA (A문자열==B문자열)일 경우 답은 4000이 되어야 함.
		 */
		// 찾아보니 알고리즘이 따로 있었음!!
		System.out.println(max);
	}

}
