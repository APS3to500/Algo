import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int N,M,K;
	// 배열 ar : N*N 배열, M : 나무의 개수(하나의 칸에 여러개의 나무가 있을 수도 있음!)
	static int[][] ar,area;
	static int ans;
	static int[] dy = {-1,-1,-1, 0,0, 1,1,1};
	static int[] dx = {-1,0,1, -1,1, -1,0,1};
	static ArrayList<tree>[][] tr;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		ar = new int[N+1][N+1]; // 매 겨울마다 더해질 양분값을 저장
		area = new int[N+1][N+1]; // 땅
		tr = new ArrayList[N+1][N+1];
		// 시뮬레이션을 막 시작했을 당시엔 각 땅의 양분이 5씩 있으며, 봄부터 시작
		/*
		 봄 : 나이만큼 양분 먹고 나이 1 증가(각 나무는 나무가 있는 1*1 크기의 칸에 있는 양분만 먹을 수 있음)(하나의 칸에 여러 나무가 있으면 나이가 어린 나무부터 양분을 먹음)(양분이 부족해 나이만큼 양분을 못먹으면 즉시 사망)
		 여름 : 봄에 죽은 나무를 양분으로 변하게 함 (각 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨. 소숫점 아래는 버림(int값으로 ㄱㄱ)
		 가을 : 나무가 번식
		 - 나이가 5의 배수(5,10,15 등등)인 나무만 번식 가능.
		 - 인접한 8개의 칸에 나이가 1인 나무가 생김
		 - 상도의 땅을 벗어나는 칸에는 나무가 생기지 않음
		 겨울 : 로봇이 땅을 돌아다니면서 땅에 양분을 추가
		 - 각 칸에 추가되는 양분의 양 : ar[i][j]
		 */
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				ar[i][j] = Integer.parseInt(st.nextToken()); // 매년 겨울마다 [i][j] 땅에는 ar[i][j] 만큼의 양분이 추가됨!
				area[i][j] = 5;
				tr[i][j] = new ArrayList<tree>();
			}
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken()); //나무의 위치 : [y][x]
			int z = Integer.parseInt(st.nextToken()); //나무[y][x]의 나이
			tr[x][y].add(new tree(z,false));
			/*
			 나무 고찰
			 한 땅에 나무가 여러 그루 있을 수도 있음
			 매 봄마다 양분을 얻어먹으며,
			 봄에 [y][x]의 나무들에게 양분을 줘야 함.
			 */
		}
		
		for (int t = 0; t < K; t++) {
			// 0단계 : 봄맞이 준비
			// 각 칸의 나무는 어린 나무부터 양분을 먹게 됨 => 정렬 필요
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					Collections.sort(tr[i][j]);
//					System.out.println(tr[i][j].toString());
				}
			}
			
			// 1단계. 봄 : 나이만큼 양분 먹고 나이 1 증가(각 나무는 나무가 있는 1*1 크기의 칸에 있는 양분만 먹을 수 있음)
			// (하나의 칸에 여러 나무가 있으면 나이가 어린 나무부터 양분을 먹음)
			// (양분이 부족해 나이만큼 양분을 못먹으면 즉시 사망)
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					for (int d = 0; d < tr[i][j].size(); d++) {
						if(area[i][j] >= tr[i][j].get(d).age) {
							area[i][j] -= tr[i][j].get(d).age;
//							System.out.println(tr[i][j].get(d).age);
							tr[i][j].get(d).age +=1;
						}
						else {
							tr[i][j].get(d).dead = true;
						}
					}
				}
			}
			
			// 2단계. 여름 : 봄에 죽은 나무를 양분으로 변하게 함 (죽은 나무임을 알 수 있어야 할듯!
			// (각 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨. 소숫점 아래는 버림)
			// (int값으로 ㄱㄱ)
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					for (int d = 0; d < tr[i][j].size(); d++) {
						if(tr[i][j].get(d).dead) {
							area[i][j] += (tr[i][j].get(d).age/2);
							tr[i][j].remove(d);
							d--;
						}
					}
				}
			}
			
			// 3단계. 가을 : 나무가 번식
			// 나이가 5의 배수(5,10,15 등등)인 나무만 번식 가능.
			// 인접한 8개의 칸에 나이가 1인 나무가 생김
			// 상도의 땅을 벗어나는 칸에는 나무가 생기지 않음
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					for (int d = 0; d < tr[i][j].size(); d++) {
						if(tr[i][j].get(d).age % 5 == 0 && tr[i][j].get(d).age > 0) {
							for (int f = 0; f < 8; f++) {
								int ny = i+dy[f];
								int nx = j+dx[f];
								if(ny <= 0 || ny > N || nx <= 0 || nx > N) continue;
								tr[ny][nx].add(new tree(1,false));
							}
						}
					}
				}
			}
			
			// 4단계. 겨울 : 로봇이 땅을 돌아다니면서 땅에 양분을 추가
			// 각 칸에 추가되는 양분의 양 : ar[i][j]
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					area[i][j] += ar[i][j];
				}
			}
			
		}
		// k년후, 살아남은 나무는 몇그루인가!
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				ans += tr[i][j].size();
			}
		}
		System.out.println(ans);
	}

	static class tree  implements Comparable<tree>{
		int age;
		boolean dead;
		public tree(int age, boolean dead) {
			super();
			this.age = age;
			this.dead = dead;
		}
		
		@Override
		public String toString() {
			return "tree [age=" + age + ", dead=" + dead + "]";
		}

		@Override
		public int compareTo(tree t) {
			if(t.age < age) {
				return 1;
			}
			else if(t.age > age) {
				return -1;
			}
			return 0;
		}
	}
}
