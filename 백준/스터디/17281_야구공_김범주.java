import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2트성공_1시간20분 {
	static int N,ans,max = Integer.MIN_VALUE; //이닝 수
	static int[][] ar;
	static int[] tgt,selected; // 선수 명단
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		/*
		 9명의 선수가 각 이닝에 몇점을 얻을 지 알고 있음
		 각 이닝별 선수를 어떻게 배치해야 가장 높은 점수를 받을 수 있을까? -> 순서가 필요하기에 순열을 사용
		 배열 입력
		 1번 선수는 무조건 4번째로 타자 진행
		 ex) 3 2 4 1 9 8 7 6 5 이고 1이닝 0 0 1 4 0 0 0 0 0라고 하면
		 3 2 <- 2아웃 , 4 1 <- 2점 득점, 9 <- 3아웃... 이후 8번 선수부터 다음 이닝 진행(타순은 이닝이 변경되어도 순서를 유지해야 한다.)
		 */
		N = Integer.parseInt(br.readLine());
		ar = new int[N+1][10];
		tgt = new int[10]; // 순서를 고르는 배열 ex) tgt[1] = 4 <= 4번 선수가 1번 타자 (tgt[순서] = 선수)
		selected = new int[10];
		for (int t = 1; t <= N; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= 9; i++) {
				ar[t][i] = Integer.parseInt(st.nextToken());
			}
		}
		perm(1);
		System.out.println(max);
	}
	static void perm(int tgtIdx) {
		if(tgtIdx == 10) { // 순서가 다 정해지면
			cal(tgt,0,0,0,0);
			return;
		}
		if(tgtIdx == 4) {
			tgt[tgtIdx] = 1;
			perm(tgtIdx+1);
		}
		else {
			for (int i = 2; i <= 9; i++) {
				if(selected[i] == 1) continue;
				selected[i] = 1;
				tgt[tgtIdx] = i;
				perm(tgtIdx+1);
				selected[i] = 0;
			}
		}
		
	}
	
	static void cal(int[] tgt,int out,int one,int two,int three) {
		int t = 1;
		int score = 0;
			for (int i = 1; i < tgt.length; i++) {
				switch(ar[t][tgt[i]]) {
				case 0:
					out++;
					if(out == 3) {
						t++;
						one = 0;
						two = 0;
						three = 0;
						ans += score;
						score = 0;
						out = 0;
						if(t > N) {
							max = Math.max(ans, max);
							ans = 0;
							return;
						}
					}
					break;
				case 1:
					one++;
					if(three >= 1) {
						score++;
						three--;
					}
					if(two >= 1) {
						three++;
						two--;
					}
					if(one >= 2) {
						two++;
						one--;
					}
					break;
				case 2:
					two++;
					if(three >= 1) {
						score++;
						three--;
					}
					if(one >= 1) {
						three++;
						one--;
					}
					if(two >= 2) {
						score++;
						two--;
					}
					break;
				case 3:
					three++;
					if(one >= 1) {
						score++;
						one--;
					}
					if(two >= 1) {
						score++;
						two--;
					}
					if(three >= 2) {
						score++;
						three--;
					}
					break;
				case 4:
					score++;
					if(one == 1) {
						one = 0;
						score++;
					}
					if(two == 1) {
						two = 0;
						score++;
					}
					if(three == 1) {
						three = 0;
						score++;
					}
					break;
				}
				
				if(i == 9 & out < 3) {
					i = 0;
				}
			}
		
	}
}
